#
from flask import Flask

#
import os

#
import secrets

#
import string

#
from Database.Connection import app_database

#
from View.Routes.Route_Controller import outline_app_routes




#
def generate_secret_random_key(length_of_key):

    #
    characters = string.ascii_letters + string.digits + string.punctuation
    
    #
    secret_key = "".join(secrets.choice(characters) for _ in range(length_of_key))
    
    #
    return secret_key




#
app_sub_directory_base = os.path.abspath(os.path.dirname(__file__))




#
app = Flask(__name__,template_folder="View/Templates")

#
app.config["SECRET_KEY"] = generate_secret_random_key(64)

#
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(app_sub_directory_base,"Database","Database-YZ-DFD.db")

#
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False




#
def main():
    
    #
    app_database.init_app(app)
    
    #
    from Database.Table_Models import User, Classification
    
    #
    outline_app_routes(app,app_database,User,Classification)
    
    #
    with app.app_context():
        app_database.create_all()
    
    #
    app.run(debug=True)




#
if (__name__=="__main__"):
    main()