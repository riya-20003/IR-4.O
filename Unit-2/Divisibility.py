num = int(input("enter a number : "))
if num%5 == 0:
    if num%2 == 0:
     print("number is divisible by 5 and even")
    else:
     print("number is odd and divisible by 5")
else:
    if num%2 == 0:
                print("number is not divisible by 5 but it is even")
    else:
       print("the number neither divisible by nor even")