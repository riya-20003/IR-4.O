passw=input("enter password:")
if(len(passw)<9 or len(passw)>16):
    print("enter a password with minimum 9 characters and maximum 15 characters")
else:
    if(passw.isalpha()):
        print("use numbers")
    else:
        if(passw.isnumeric()):
            print("USE alphabets")
        else:
            print("Correct")