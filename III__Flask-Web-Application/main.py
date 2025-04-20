#
#
from flask import Flask

#
#
import secrets

#
#
import string

#
#
from Static.PY import Route_Index, Route_Login, Route_Register




#
#
def generate_secret_random_key(length_of_key):

    #
    characters = string.ascii_letters + string.digits + string.punctuation
    
    #
    secret_key = "".join(secrets.choice(characters) for _ in range(length_of_key))
    
    #
    return secret_key




# An instance of the Flask class is created.
# It represents my web application for Deepfake Detection.
app = Flask(__name__)

#
#
app.config["SECRET_KEY"] = generate_secret_random_key(16)




# This is a route decorator, for the home / index / landing page of the web app.
# The route can answer to HTTP 'Get' and 'Post' requests.
@app.route("/", methods=["GET","POST"])
def index_page():

    #
    return Route_Index.index_page()




# This is a route decorator, for the login page of the web app.
#
@app.route("/login")
def login_page():
    
    #
    return Route_Login.login_page()




# This is a route decorator, for the register page of the web app.
#
@app.route("/register")
def register_page():
    
    #
    return Route_Register.register_page()