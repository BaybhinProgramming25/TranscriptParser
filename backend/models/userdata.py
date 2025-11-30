from pydantic import BaseModel 

class SignUpData(BaseModel):
    username: str
    password: str 
    email: str 

class LoginData(BaseModel):
    email: str 
    password: str 

class LogoutData(BaseModel):
    username: str 
    email: str 

class ContactData(BaseModel):
    name: str 
    email: str 
    subject: str 
    message: str 
