#
from flask import render_template, flash, redirect, request

#
from flask_wtf import FlaskForm

#
from wtforms import SubmitField, StringField, EmailField, PasswordField

#
from wtforms.validators import Email

#
import bcrypt

#
from Database.Create_DB import db as app_database

#
from Database.Table_Models import User

#
from View.Supports import Support_Register

#
from View.Routes import Temp_Middleware




#
class RegisterForm(FlaskForm):
    
    #
    forename = StringField("First Name:",validators=[])
    
    #
    surname = StringField("Last Name:",validators=[])
    
    #
    email = EmailField("Email Address:",validators=[Email()])
    
    #
    password = PasswordField("Password:",validators=[])
    
    #
    confirm = PasswordField("Confirm Password:",validators=[])
    
    #
    submit = SubmitField("Sign Up~")




#
def register_page():
    
    #
    register_form = RegisterForm()
    
    #
    if (request.method=="GET"):
        Temp_Middleware.delete_temp_image_data()
        return render_template("Unsigned/Register.html",form=register_form)
    
    #
    elif (request.method=="POST"):
        
        #
        input_forename = register_form.forename.data.strip()
        input_surname = register_form.surname.data.strip()
        input_email = register_form.email.data.strip()
        input_password = register_form.password.data.strip()
        input_confirm = register_form.confirm.data.strip()
        
        #
        if not(Support_Register.input_complete_validation(input_forename,input_surname,input_email,input_password,input_confirm)):
            flash("Error! In order to submit this form, you need to give a full name, valid email, and strong confirmed password.","error")
            return redirect(request.url)
        
        #
        if not(Support_Register.email_space_validation(input_email)):
            flash("Error! In order to submit this form, you need to give a full name, valid email, and strong confirmed password.","error")
            return redirect(request.url)
        
        #
        if not(Support_Register.pattern_valid_validation(input_email)):
            flash("Error! In order to submit this form, you need to give a full name, valid email, and strong confirmed password.","error")
            return redirect(request.url)
        
        #
        if not(Support_Register.password_confirmed_validation(input_password,input_confirm)):
            flash("Error! In order to submit this form, you need to give a full name, valid email, and strong confirmed password.","error")
            return redirect(request.url)
        
        #
        if not(Support_Register.password_strength_validation(input_password)):
            flash("Error! In order to submit this form, you need to give a full name, valid email, and strong confirmed password.","error")
            return redirect(request.url)
        
        #
        bytes_of_input_password = input_password.encode("utf-8")
        password_salt = bcrypt.gensalt()
        password_salted_and_hashed = bcrypt.hashpw(bytes_of_input_password,password_salt)
        
        #
        try:
            new_user = User(userEmail=input_email,userPassword=password_salted_and_hashed,userFirstName=input_forename,userLastName=input_surname)
            app_database.session.add(new_user)
            app_database.session.commit()
            flash("You've successfully created a new user account~ Try to log in from the login page.","success")
            return redirect("/login")
        
        #
        except:
            flash("Error! A user account cannot be created with the credentials provided here.","error")
            return redirect(request.url)