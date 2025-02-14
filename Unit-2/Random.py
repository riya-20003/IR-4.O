import random
print("Heads : 1")
print("Tails : 0")
ch=int(input("Enter your choice : "))
computer=random.randint(0,1)
rev_dict={1 : "Head", 0 : "Tails"}
print(f"Your choice : {rev_dict[ch]}")
print(f"Computer choice : {rev_dict[computer]}")
if computer==ch:
    print("You won!")
else:
    print("You lose!")