from fastapi import APIRouter, Response, Cookie
from fastapi.responses import RedirectResponse
from typing import Optional

from models.userdata import SignUpData, LoginData, LogoutData, ContactData
from models.database import get_users_collection, get_contacts_collection
from middleware.verification.sendverify import send_verification_email
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

import bcrypt 
import uuid 
import os 
import jwt

router = APIRouter()
load_dotenv()


@router.post('/api/signup')
async def signup(data: SignUpData, response: Response):

    try:
        username = data.username 
        password = data.password 
        email = data.email 
        
        users_collection = get_users_collection()

        user = await users_collection.find_one({ "username": username })

        if user:
            print("User already exists", flush=True)
            response.status_code = 409
            return {"message": "User already exists!"}

        token = str(uuid.uuid4())
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        if not await send_verification_email(email, token):
            print('Unable to send verification email')
            response.status_code = 500
            return {"message": "Unable to send verification email"}

        new_user = {
            "username": username,
            "password": hashed_password, 
            "email": email,
            "verificationToken": token,
            "is_verified": False,
            "created_at": datetime.now(timezone.utc)
        }

        await users_collection.insert_one(new_user)

        response.status_code = 201
        return {"message": "Successfully added user"}
    except Exception as error:
        print('Error adding user', error)
        response.status_code = 500
        return {"message": "Unable to add user"}


@router.post('/api/login')
async def login(data: LoginData, response: Response):
    try:
        email = data.email
        password = data.password 

        users_collection = get_users_collection()
        user = await users_collection.find_one({ "email": email })

        if not user:
            print('Unable to find user')
            response.status_code = 404
            return {"message": "User not found"}

        # Check the value of is_verified 
        if not user["is_verified"]:
            print('User is not verified')
            response.status_code = 403 
            return {"message": "User is not verified"}

        # Get the hashed password field
        hashed_password = user["password"]

        if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print('Passwords do not match')
            response.status_code = 401 
            return {"message": "Passwords do not match"}
        
        # Create Refresh Token 
        payload_refresh = {
            "user_id": str(user["_id"]),
            "exp": datetime.now(timezone.utc) + timedelta(days=7)
        }
        refresh_token = jwt.encode(payload_refresh, os.getenv("REFRESH_TOKEN_SECRET"), algorithm="HS256")

        # Set it as a cookie 
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite='lax',
            max_age=7*24*60*60
        )

        await users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"refreshToken": refresh_token}}
        )

        username_email_pair = {
            "username": user["username"],
            "email": user["email"]
        }

        response.status_code = 200
        return {"user_data": username_email_pair}
    except Exception as error:
        print(error)
        response.status_code = 500
        return {"message": "Internal Server Error"}


@router.post('/api/contact')
async def contact(data: ContactData, response: Response):
    try:
        name = data.name 
        email = data.email 
        subject = data.subject
        message = data.message 

        contact_query = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }

        contact_collection = get_contacts_collection()
        await contact_collection.insert_one(contact_query)
        response.status_code = 200
        return{"message": "Succesfully received contact"}

    except Exception as error:
        print(error)
        response.status_code = 500 
        return {"message": "Error saving contact form"}


@router.post('/api/logout')
async def logout(data: LogoutData, response: Response):
    try:
        email = data.email

        users_collection = get_users_collection()
        user = await users_collection.find_one({ "email": email })

        await users_collection.update_one(
            {"_id": user["_id"]},
            {"$unset": {"refreshToken": ""}}
        )

        response.delete_cookie(key="refresh_token")

        response.status_code = 200
        return {"message": "Successfully Logged Out!"}
    except Exception as error:
        print(error)
        response.status_code = 500
        return {"message": "Unable to logout"}
    
# Works 
@router.get('/api/verify/{verification_token}')
async def verify(verification_token: str, response: Response):
    
    try:
        token = verification_token

        users_collection = get_users_collection()
        user = await users_collection.find_one({ "verificationToken": token })
        
        if not user:
            print("Invalid verification token")
            response.status_code = 500
            return {"message": "Invalid verification token"}

        await users_collection.update_one(
            {"_id": user["_id"]},
            {
                "$set": {"is_verified": True},
                "$unset": {"verificationToken": ""}
            }
        )

        return RedirectResponse(url="http://localhost:5173/login")

    except Exception as error:
        print(error)
        response.status_code = 500
        return {"message": "Unable to find user "}


@router.post("/api/refresh")
async def refresh(response: Response, refresh_token: Optional[str] = Cookie(None)):
    if not refresh_token:
        response.status_code = 401
        return {"message": "No refresh token"}

    try:
        jwt.decode(refresh_token, os.getenv("REFRESH_TOKEN_SECRET"), algorithms="HS256")

        users_collection = get_users_collection()
        user = await users_collection.find_one({ "refreshToken": refresh_token})

        user_email_pair = {
            "username": user["username"],
            "email": user["email"]
        }

        response.status_code = 200
        return {"user_data": user_email_pair}
    
    except jwt.InvalidTokenError:
        print("Refresh token is invalid")
        response.status_code = 500 
        return {"message": "Refresh Token is invalid. Please login again"}
    