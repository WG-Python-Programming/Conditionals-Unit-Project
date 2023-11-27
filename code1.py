def password_validator(password):
    min_length = 8
    str(min_length) == 8
    special_characters = "!@#$%^&*()-=_+[]{}|;:'\"<>,.?/"

    #looked up the command "len"
    if len(password) < min_length:
        print("Password is too short. It must be at least "+str(min_length)+" characters long.")

    elif not any(character in special_characters for character in password):
        print("Password must contain at least one special character.")

    else:
        print("Password is valid.")
    """
    looked up line 9 up too, i am pretty sure i understand how it works; 
    you can change the variable 'character' to anything as long as you change both of them. 
    so 'any' is a bool to see if any characters in the 'special_characters
    """
# Get user input
print("password must be above 8 characters")
print("password must have one special character")
user_password = input("Enter your password to check the validity : ")

# Validate password
password_validator(user_password)
