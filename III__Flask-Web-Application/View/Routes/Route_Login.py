#
from flask import render_template, flash, redirect, request, session

#
from flask_wtf import FlaskForm

#
from wtforms import SubmitField, EmailField, PasswordField

#
from wtforms.validators import Email

#
from datetime import datetime

#
from Database.Create_DB import db as app_database

#
from View.Supports import Support_Login

#
from View.Routes import Temp_Middleware




#
class LoginForm(FlaskForm):
    
    #
    email = EmailField("Email Address:",validators=[Email()])
    
    #
    password = PasswordField("Password:",validators=[])
    
    #
    submit = SubmitField("Sign In~")




#
def login_page():
    
    #
    login_form = LoginForm()
    
    #
    if (request.method=="GET"):
        Temp_Middleware.delete_temp_image_data()
        return render_template("Unsigned/Login.html",form=login_form)
    
    #
    elif (request.method=="POST"):
        
        #
        input_email = login_form.email.data.strip()
        input_password = login_form.password.data.strip()
        
        #
        if not(Support_Login.input_complete_validation(input_email,input_password)):
            flash("> A input incomplete","error")
            return redirect(request.url)
        
        #
        if not(Support_Login.email_space_validation(input_email)):
            flash("> B email spaced","error")
            return redirect(request.url)
        
        #
        if not(Support_Login.pattern_valid_validation(input_email)):
            flash("> C empattern invalid","error")
            return redirect(request.url)
        
        #
        existing_user = Support_Login.user_exists_validation(input_email)
        if not(existing_user):
            flash("> D user unidentified","error")
            return redirect(request.url)
        
        #
        if not(Support_Login.password_match_validation(input_password,existing_user)):
            flash("> E user unverified","error")
            return redirect(request.url)
        
        #
        try:
            session["user"] = {
                "id" : existing_user.userID,
                "name" : f"{existing_user.userFirstName} {existing_user.userLastName}",
                "lastLogged" : existing_user.userLastLogged
            }
            existing_user.userLastLogged = datetime.now()
            app_database.session.commit()
            flash(f"> Hello World! logged {session["user"]["name"]}","success")
            return redirect("/")
        
        #
        except:
            flash("> YZ can't log","error")
            return redirect(request.url)