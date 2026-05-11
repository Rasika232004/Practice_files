# 08-05-26
# tasks on string formatting
"""
#Task 1 : Accept student info as : Student name, marks, per and display as student name is rahul scored marks 450 with 90.0% percentage 
name = input("Enter student name : ")
marks = float(input("Enter student marks : "))
per = float(input("Enter student percentage : "))

print(f"Student name is {name} scored {marks} with {per:.2f}% percentage")

# task 2
age = int(input("Enter your age: "))
age += 10
print(f"Your age after 10 years is {age}")

#Task 3
name = input("Enter name : ")
marks = float(input("Enter marks : "))

print("-" *16)
print("| Name | Marks |")
print("-" *16)
print(f"| {name:^4} | {marks:^5} |")
"""
# Task 4 : make a report card 
# heading : The kiran academy Report card 
# student name: raj patil 
#subject name : python,java,html,css,sql   marks:91,90,88,95,96
# total 470 grade is A   

name = "Raj Patil"
sub1 = "Python"
sub2 = "Java"
sub3 = "HTML"
sub4 = "CSS"
sub5 = "SQL"
mark1 = 91
mark2 = 90
mark3 = 88
mark4 = 95
mark5 = 96
total = mark1+mark2+mark3+mark4+mark5
per = total/100

print("*" *50)
print("*" *50)
print(f"The Kiran Academy Report Card")
print("-" *50)

print(f"\nStudent Name : {name}")
print("-" *50)
print(f"| {'Subject Name':^20} | {'Marks':^20} | ")
print("-" *50)
print(f"| {sub1:^20} | {mark1:^20} |")
print("-" *50)
print(f"| {sub2:^20} | {mark2:^20} |")
print("-" *50)
print(f"| {sub3:^20} | {mark3:^20} |")
print("-" *50)
print(f"| {sub4:^20} | {mark4:^20} |")
print("-" *50)
print(f"| {sub5:^20} | {mark5:^20} |")

print("-" *50)
print("-" *50)
print(f"| {'Total':^15} | {mark1+mark2+mark3+mark4+mark5:^25} |")
print("-" *50)
print(f"| {'Percentage':^15} | {per:^25} |")
print("-" *50)

print("*" *50)
print("*" *50)



