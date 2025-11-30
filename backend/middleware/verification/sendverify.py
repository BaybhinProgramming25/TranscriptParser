import aiosmtplib 
from email.message import EmailMessage

async def send_verification_email(email: str, verification_token: str):

    message = EmailMessage()
    message["From"] = "no-reply@transcriptqa.com"
    message["To"] = email 
    message["Subject"] = "Account Verification"

    verification_link = f"http://localhost:3000/api/verify/{verification_token}"
    message.set_content(f"Please click on the following link to verify your email: {verification_link}")

    # Send the Email
    try:
        await aiosmtplib.send(
            message,
            hostname='mailhog',
            port=1025,
            start_tls=False,
            validate_certs=False
        )
        print(f"Email sent to {email}")
        return True 
    except Exception as error:
        print(f"Error sending email: {error}")
        return False 