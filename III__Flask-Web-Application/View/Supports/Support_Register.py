#
import re




#
def find_password_special_character(input_password):
    
    #
    for character in input_password:
        if not(character.isalpha() or character.isdigit() or character.isspace()):
            return True
    
    #
    return False




#
def input_complete_validation(input_forename, input_surname, input_email, input_password, input_confirm):
    
    #
    if (input_forename and input_surname and input_email and input_password and input_confirm):
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
def password_confirmed_validation(input_password, input_confirm):
    
    #
    if (input_password==input_confirm):
        return True
    
    #
    else:
        return False




#
def password_strength_validation(input_password):
    
    #
    password_strength_condition_1 = len(input_password) >= 8
    password_strength_condition_2 = any(character.isupper() for character in input_password)
    password_strength_condition_3 = any(character.islower() for character in input_password)
    password_strength_condition_4 = any(character.isdigit() for character in input_password)
    password_strength_condition_5 = find_password_special_character(input_password)
    
    #
    if (password_strength_condition_1 and password_strength_condition_2 and password_strength_condition_3 and password_strength_condition_4 and password_strength_condition_5):
        return True
    
    #
    else:
        return False