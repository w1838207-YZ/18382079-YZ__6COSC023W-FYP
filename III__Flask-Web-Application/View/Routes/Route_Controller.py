#
from flask import flash, redirect, session

#
from View.Routes import Route_Upload, Route_Prediction, Route_Register, Route_Login, Route_Savings, Route_Saving, Route_Logout

#
from View.Routes import Delete_Middleware



#
def outline_app_routes(app):
    
    #
    @app.route("/", methods=["GET","POST"])
    def upload_page():
        Delete_Middleware.old_classification_record_deletion(app)
        if (session.get("user")):
            return Route_Upload.signed_upload_page(session["user"])
        else:
            return Route_Upload.unsigned_upload_page()
    
    #
    @app.route("/prediction", methods=["GET","POST"])
    def prediction_page():
        Delete_Middleware.old_classification_record_deletion(app)
        if (session.get("user")):
            return Route_Prediction.signed_prediction_page(session["user"])
        else:
            return Route_Prediction.unsigned_prediction_page()
    
    #
    @app.route("/register", methods=["GET","POST"])
    def register_page():
        Delete_Middleware.old_classification_record_deletion(app)
        if not(session.get("user")):
            return Route_Register.register_page()
        else:
            flash("> Can't access register page when signed in","error")
            return redirect("/")
    
    #
    @app.route("/login", methods=["GET","POST"])
    def login_page():
        Delete_Middleware.old_classification_record_deletion(app)
        if not(session.get("user")):
            return Route_Login.login_page()
        else:
            flash("> Can't access login page when signed in","error")
            return redirect("/")
    
    #
    @app.route("/savings", methods=["GET","POST"])
    def all_savings_page():
        Delete_Middleware.old_classification_record_deletion(app)
        if (session.get("user")):
            return Route_Savings.all_savings_page(session["user"])
        else:
            flash("> Can't access savings page when signed out","error")
            return redirect("/")
    
    #
    @app.route("/saving/<savingID>", methods=["GET"])
    def single_saving_page(savingID):
        Delete_Middleware.old_classification_record_deletion(app)
        if (session.get("user")):
            return Route_Saving.single_saving_page(savingID)
        else:
            flash("> Can't access saving page when signed out","error")
            return redirect("/")
    
    #
    @app.route("/logout", methods=["GET","POST"])
    def logout_page():
        Delete_Middleware.old_classification_record_deletion(app)
        if (session.get("user")):
            return Route_Logout.logout_page()
        else:
            flash("> Can't access logout page when signed out","error")
            return redirect("/")