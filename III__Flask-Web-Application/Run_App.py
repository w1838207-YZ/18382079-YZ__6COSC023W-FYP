#
from flask import Flask

#
from App_Configuration import class_to_configure_app

#
from Database.Create_DB import db as app_database

#
from Session.Add_Sessions import server_side_session

#
from View.Routes import Route_Controller, Delete_Middleware

#
import os




#
app = Flask(__name__,template_folder="View/Templates")

#
app.config.from_object(class_to_configure_app)




#
def main():
    
    #
    app_database.init_app(app)
    
    #
    from Database.Table_Models import User, Classification
    
    #
    server_side_session.init_app(app)
    
    #
    with app.app_context():
        app_database.create_all()
        Delete_Middleware.old_classification_record_deletion(app)
    
    
    #
    Route_Controller.outline_app_routes(app)
    
    #
    port = int(os.environ.get("PORT",5000))
    
    #
    app.run(host="0.0.0.0",port=port)




#
if (__name__=="__main__"):
    main()