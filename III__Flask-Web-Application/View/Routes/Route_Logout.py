#
from flask import render_template, flash, redirect, request, session

#
from View.Routes import Temp_Middleware




#
def logout_page():
    
    #
    if (request.method=="GET"):
        Temp_Middleware.delete_temp_image_data()
        return render_template("Signed/Logout.html")
    
    #
    elif (request.method=="POST"):
        
        #
        if ("yes" in request.form):
            session.clear()
            flash("You've successfully just logged out of your user account~ We hope you return again in the future!","success")
            return redirect("/")
        
        #
        elif ("no" in request.form):
            flash("No worries~ You're still logged into your user account.","success")
            return redirect("/")
        
        #
        else:
            flash("Error! You need to indicate whether or not you want to log out on the logout page.","error")
            return redirect("/")