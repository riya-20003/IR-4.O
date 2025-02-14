bill_amount = float(input("enter bill amount : "))
no_of_person = int(input("enter no of person : "))
percent_tip = float(input("enter percent tip : "))
amt_tip = bill_amount * (percent_tip / 100)
total_bill = amt_tip + bill_amount
print("per person amount is : {}" .format(total_bill/no_of_person))