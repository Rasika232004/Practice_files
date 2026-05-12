
    
""" 
# if-elif-else 
jay = 23
viru = 34


if jay > viru:
    print("jay pay bill")
elif viru > jay:
    print("Viru will pay the bill")
else:
    print("Both will pay the bill")

Task1 : You need to design a portal for pune.
        check user age for eligibility
        user age is above 18 and below 75 can be eligible for apply rto licence.
        display appropriate msg to user as per age criteria
        for less age display wait for _____ years
        age is above 75 then display you are age bar
        other wise welcome to pune rto portal 
"""
user_age = int(input("Enter you age: "))
if user_age > 0:
    if user_age < 18 :
        print(f"Sorry! You cannot apply wait for {18-user_age} years")
    elif 18<=user_age<=75:
        print(f"Welcome to Pune RTO You are eligible to apply")
    elif user_age>75:
        print(f"The age limit is 18 to 75")
    else:
        print("Enter valid age between 18 to 75")
else :
    print("Age not be negative enter positive age")


    
