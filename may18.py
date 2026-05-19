# Write a program to accept cost price & selling price find the profit or loss.
c_price = float(input("Enter cost price : "))
s_price = float(input("Enter selling price : "))

if c_price < s_price :
    profit = s_price - c_price
    print(f"Profit is {profit} ")
    
elif c_price > s_price :
    loss = c_price - s_price
    print(f"Loss is {loss}")
    
else:
    print("No profit No loss")


# check the given number is even or odd      
n = int(input("\nEnter number: "))
if n %2==0 :
    print("The given number is even")
else:
    print("The given number is odd")

# check the given num is +ve, -ve or zero 
num = int(input("\nEnter number: "))

if num > 0:
    print(f"The given {num} is positive")
elif num < 0:
    print(f"The given {num} is negative")
else:
    print(f"The given {num} is zero")
    
# check the given num is divisible by 3 & 7 or not 
number = int(input("\nEnter number : "))

if number%3==0 and number%7==0 :
    print(f"The given {number} is divisible by both 3 and 7")
else:
    print(f"The given {number} is not divisible by both 3 and 7")
    
# accept 2 num and swap them without using 3 variable
first = int(input("\nEnter first number: "))
second = int(input("Enter second number: "))

first , second = second , first
print(f"the swap numbers are {first}, {second}")

"""
Verify given year is leap year or not
> 2020, 2024, 1600 --leap year
> 2025, 2027 , 1700 -- not leap year

""" 
year = int(input("Enter year: "))
if (year%4 == 0 and year%100 != 0) or (year % 400 == 0) :
    print(f"The given year {year} is leap year")
else :
    print(f"The given year {year} is not leap year")

# find max of given 3 num
a = 20
b = 30 
c = 10

print("Maximum number: ",max(a,b,c))
print("Minimum number",min(a,b,c))

# display sum of max and sum of min


# Accept 5 subject marks & print the total & percentage        
sub1 = float(input("Enter subject 1 marks"))
sub2 = float(input("Enter subject 2 marks"))
sub3 = float(input("Enter subject 3 marks"))
sub4 = float(input("Enter subject 4 marks"))
sub5 = float(input("Enter subject 5 marks"))

total = sub1+sub2+sub3+sub4+sub5
per = total / 100

print(f"Total of 5 subject is : {total} ")
print(f"Percentage : {per}")
    
