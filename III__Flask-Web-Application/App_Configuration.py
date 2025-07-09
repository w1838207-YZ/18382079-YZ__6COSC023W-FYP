#
import redis

#
from dotenv import load_dotenv

#
import os

#
import secrets

#
import string




#
app_sub_directory_base = os.path.abspath(os.path.dirname(__file__))

#
load_dotenv()




#
def generate_secret_random_key(length_of_key):

    #
    characters = string.ascii_letters + string.digits + string.punctuation
    
    #
    secret_key = "".join(secrets.choice(characters) for _ in range(length_of_key))
    return secret_key




#
class class_to_configure_app:
    
    #
    try:
        SECRET_KEY = os.environ["SECRET_KEY"]
    except:
        SECRET_KEY = generate_secret_random_key(64)
    
    #
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(app_sub_directory_base,"Database","Database-YZ-DFD.db")
    
    #
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #
    SESSION_TYPE = "redis"
    
    #
    SESSION_PERMANENT = False
    
    #
    SESSION_USE_SIGNER = True
    
    #
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
    
    #
    UPLOAD_FOLDER = os.path.join(app_sub_directory_base,"Static","IMG")