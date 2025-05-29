#
from flask import render_template, request, flash, redirect

#
from flask_wtf import FlaskForm

#
from wtforms import StringField, SubmitField, EmailField, PasswordField

#
from wtforms.validators import Email

#
import re




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
    submit = SubmitField("Register")




#
def register_page(app_database, User, Classification):
    
    #
    register_form = RegisterForm()
    
    #
    if (request.method=="GET"):
        
        #
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
        if ((not(input_forename))or(not(input_surname))or(not(input_email))or(not(input_password))or(not(input_confirm))):
            flash("> A","error")
            return redirect(request.url)
        
        #
        if (" " in input_email):
            flash("> B","error")
            return redirect(request.url)
        
        #
        valid_email_regex_pattern = "/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/"
        if (re.search(valid_email_regex_pattern,input_email)):
            flash("> C","error")
            return redirect(request.url)
        
        #
        if (input_password!=input_confirm):
            flash("> D","error")
            return redirect(request.url)
        
        #
        new_user = User(userEmail=input_email,userPassword=input_password,userFirstName=input_forename,userLastName=input_surname)
        
        #
        app_database.session.add(new_user)
        app_database.session.commit()
        
        #
        flash("> Hello World!","success")
        return redirect("/")