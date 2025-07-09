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
            flash("> 1! now out","success")
            return redirect("/")
        
        #
        elif ("no" in request.form):
            flash("> 2! still in","success")
            return redirect("/")
        
        #
        else:
            flash("> YZ! cannot logout","error")
            return redirect("/")