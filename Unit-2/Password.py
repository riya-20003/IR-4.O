password = input("enter your password")
#asdf12345%
spec_char= "@#$%&"

if(len(password)>8 or len(password)<16):
    if password.isalpha() or password.isnumeric():
        print("your password should have both number and alphabets")
    elif password.isalnum():
        print("your password doesn't contain special character")
    elif any(passw in spec_char for passw in password):
        print("valid password")
    else:
         print("invalid password...try again!")
else:
     print("password should have minimum 8 characters and maximum 16 characters")
