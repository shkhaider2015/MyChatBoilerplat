from sqlalchemy import create_engine
from sqlalchemy_utils.functions.database import create_database, database_exists
from myApp.my_secrets import my_secrets
from myApp.config import Config

# URL = f"postgresql+psycopg2://{my_secrets.pg_user}:{my_secrets.pg_password}@{my_secrets.pg_host}/{my_secrets.pg_name}"
URL = Config.SQLALCHEMY_DATABASE_URI

def init_db():
    if not database_exists(URL):
        create_database(URL)
