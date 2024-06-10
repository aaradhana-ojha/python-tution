'''. Write a program in python that accepts a string to setup a passwords. Your entered 
password must meet the following requirements: 
 The password must be at least eight characters long. 
 It must contain at least one uppercase letter. 
 It must contain at least one lowercase letter. 
 It must contain at least one numeric digit. 
Your program should should perform this validation.  '''
#aaradhana@123 = 13
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

password = input("Enter a password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one digit.")





def is_valid_password(password):
    if len(password) > 8:
        print("Password is too short. It must be at least 8 characters long.")
        return True
    if any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return True
    if any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return True
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one numeric digit.")
        return True
    return False

password = input("Enter a password: ")

if is_valid_password(password):
    print("Password is invalid.")
    
else:
    print("Password is valid.")
    
