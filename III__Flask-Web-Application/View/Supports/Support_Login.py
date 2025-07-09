#
import re

#
import bcrypt

#
from Database.Table_Models import User




#
def input_complete_validation(input_email, input_password):
    
    #
    if (input_email and input_password):
        return True
    
    #
    else:
        return False




#
def email_space_validation(input_email):
    
    #
    if (any(character.isspace() for character in input_email)):
        return False
    
    #
    else:
        return True




#
def pattern_valid_validation(input_email):
    
    #
    valid_email_regex_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    #
    if (re.match(valid_email_regex_pattern,input_email)):
        return True
    
    #
    else:
        return False




#
def user_exists_validation(input_email):
    
    #
    existing_user = User.query.filter_by(userEmail=input_email).first()
    
    #
    if (existing_user):
        return existing_user
    
    #
    else:
        return False




#
def password_match_validation(input_password, existing_user):
    
    #
    password_hash_from_database = existing_user.userPassword
    
    #
    bytes_of_input_password = input_password.encode("utf-8")
    
    #
    if (bcrypt.checkpw(bytes_of_input_password,password_hash_from_database)):
        return True
    
    #
    else:
        return False