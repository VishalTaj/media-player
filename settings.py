from dotenv import load_dotenv
from os import environ, path

SECRET_KEY = environ.get('SECRET_KEY')

# load_dotenv()

# # OR, the same with increased verbosity
# load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
# from pathlib import Path  # python3 only
env_path = path.join('.env')
load_dotenv(env_path)

class Config:
  """Set Flask configuration from .env file."""

  # General Config
  SECRET_KEY = environ.get('SECRET_KEY')
  FLASK_APP = environ.get('FLASK_APP')
  FLASK_ENV = environ.get('FLASK_ENV')

  # Database
  SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
  SQLALCHEMY_ECHO = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False