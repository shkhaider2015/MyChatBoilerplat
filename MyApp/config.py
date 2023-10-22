import os
from myApp.my_secrets import my_secrets

class Config:
    SECRET_KEY = "17352015"
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{my_secrets.pg_user}:{my_secrets.pg_password}@{my_secrets.pg_host}:{my_secrets.pg_port}/{my_secrets.pg_name}"
    # SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{my_secrets.pg_user}:{my_secrets.pg_password}@{my_secrets.pg_host}:{my_secrets.pg_port}/{my_secrets.pg_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CORS_HEADERS = 'Content-Type'


    # MAIL_SERVER='smtp.mailtrap.io'
    # MAIL_PORT = 2525
    # MAIL_USERNAME = os.environ.get('MAILTRAP_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAILTRAP_PASSWORD')
    # MAIL_USE_TLS = True
    # MAIL_USE_SSL = False

    # MAIL_SERVER='smtp.gmail.com'
    # MAIL_PORT = 465
    # MAIL_USERNAME = os.environ.get('USER_EMAIL')
    # MAIL_PASSWORD = os.environ.get('USER_PASSWORD')
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True

    @staticmethod
    def get_secret_key(self):
        return self.SECRET_KEY
    @staticmethod
    def get_user_email(self):
        return self.MAIL_USERNAME
