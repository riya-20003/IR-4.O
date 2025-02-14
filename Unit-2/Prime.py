n=int(input("enter the number:"))
l=[]

def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            l.append(i)
    if len(l)>0:
         print(f"{n} is not prime number")
    else:
         print(f"{n} is a prime number")

check_prime(n)
if len(l)>0:
    print(l)
