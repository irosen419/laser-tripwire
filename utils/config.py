import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    #* Twilio
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_KEY = os.getenv('TWILIO_AUTH_KEY')
    TWILIO_FROM_NUMBER = os.getenv('TWILIO_FROM_NUMBER')
    TWILIO_TO_NUMBER = os.getenv('TWILIO_TO_NUMBER')

    #* MailerSend
    MAILERSEND_API_KEY = os.getenv('MAILERSEND_API_KEY')
    TO_EMAIL = os.getenv('TO_EMAIL')
    FROM_EMAIL = os.getenv('FROM_EMAIL')