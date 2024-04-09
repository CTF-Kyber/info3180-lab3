import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    MAIL_SERVER="sandbox.smtp.mailtrap.io"
    MAIL_PORT=465
    MAIL_USERNAME="e76c3e3a935dc0"
    MAIL_PASSWORD="96d4a62b4242cd"
    SECRET_KEY="runguyrun"
