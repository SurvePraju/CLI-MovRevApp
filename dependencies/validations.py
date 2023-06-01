import re
# Name Validation
def NameValidation(name):
    x=re.match("^[A-Za-z\ ]+$",name)
    if x:
        return True
    else:
        return False
    
# Email Validation 
def EmailValidation(email):
    x=re.match("[a-zA-Z0-9\_\.]+\@[a-z]+\.[com|in|org]+$",email)
    if x:
        return True
    else:
        return False



# Contact Validation
def ContactValidation(contact):
    x=re.match("[6-9][0-9]{9}$",contact)
    if x:
        return True
    else:
        return False


def PasswordValidation(password):
    if len(password)>=8:
        return True  
    else:
        return "Password Too Short ,Minimum 8 characters"


