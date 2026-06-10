'''
HW: 1] Create a account on Jeera Project Management Software.
    2] write every logical code using functional way.
'''
'''
Task 1 : program to print 1 to 5 number on console
'''
# way1
def numPrint(num):
    return num
num = int(input("Enter number: "))
print(num)

# way2
def element_in_list(num):
    for nums in num:
        print(nums)
        
list = [1,2,3,4,5]
element_in_list(list)

# way 3
def elements(num):
    while num <= 5:
        print(num)
        num += 1
num = int(input("Enter number: "))
elements(num)

# way 4
def elements(num):
    while num <= 5:
        print(num)
        num += 1
num = int(input("Enter number: "))
elements(num)

# way 5
def elements(num):
    while num <= 5:
        print(num)
        num += 1
num = 1
elements(num)

def numberPrint(num):
    for num in range(1,6):
        if num == 3:
            break
        print(num)
        
num = 1
numberPrint(num)

'''
# remove duplicate  from list 
'''
def removeDuplicates(nums):
    for num in nums[:]:
        if nums.count(num) > 1:
            while nums.count(num) > 1:
                nums.remove(num)
    print(nums)
nums = [1,2,2,3,5,65,32,32,5]
removeDuplicates(nums)

def iterator_value(n):
    while n <= 5:
        print(n)
        n += 1
    print("end: ",n)
n = 1
iterator_value(n)  

def number(n):
    while n <= 5:
        n += 1
        print(n)  
        n -= 2 
n = 1
number(n)

'''
find the total number of digits in a number
'''
count = 0
def number_of_digits(num):
    count = 0
    
    while num > 0:
        num = num // 10
        count += 1
    print("Number of digits:", count)
num = 2113
number_of_digits(num)

"""
DATE: may 12
there are 3 students jay, vijay and gabbar.
design a system which checks their age and display who is older among them

"""
def ageChecker(jay_age,vijay_age,gabbar_age):
    # check the given age is not -ve    
    if jay_age>=0 and vijay_age>=0 and gabbar_age>=0:
        if jay_age > vijay_age and jay_age > gabbar_age :
            print(f"Jay is older")
        elif vijay_age > gabbar_age and vijay_age > jay_age :
            print(f"Viay is older")
        elif gabbar_age > jay_age and gabbar_age > vijay_age :
            print(f"Gabbar is older")
        else:
            print("Jay, Vijay and gabbar age is same")
    else:
        print("The age should not be negative enter valid age")

jay_age = int(input("Enter jay age: "))
vijay_age = int(input("Enter vijay age: "))
gabbar_age = int(input("Enter gabbar age: "))
ageChecker(jay_age,vijay_age,gabbar_age)

'''
DATE: may 29
Task 1: l = [45,-7,87, -67, 45,33,-33,91,65,-56]
WAP to print all -ve numbers from the list
'''
# way1
def print_negative_num(list):
    for num in list:
        if num < 0:
            print(num)

list = [45,-7,87, -67, 45,33,-33,91,65,-56]
print_negative_num(list)

'''Task 2 : display count of all even negative numbers from the list'''
def all_even_negative_num(l):
    even_count = 0
    for num in l:
        if num < 0 and num % 2 == 0:
            even_count += 1
    print(f"Count of even negative numbers: {even_count}")
    
l = [45,-7,87, -67, 45,33,-33,91,65,-56]
all_even_negative_num(l)

'''
DATE: may 27
Task 1: Add 18% gst in bill
'''

def bill(units):
    price_per_unit = 8
    total_cost = units*price_per_unit

    gst = total_cost * 0.18
    final_bill = total_cost+gst

    if units >=300 :
        units += 500
        print("Added extra 500 :", units)
    else:
        units += 100
        print("Added extra 100 :", units)

    print("Total bill : ", final_bill)

units = float(input("Enter units : "))
bill(units)

'''
Task 2 : Find common subjects both the students are learning 
ans: python and java are the common subjects both the students are learning
'''
def printSub(student1,student2):
    for subject in student1:
        for subject2 in student2:
            if subject.lower() == subject2.lower(): 
                print(subject) 

student1 = {'Python','Java','SQL','HTML'}
student2 = {'PHP','Python','React','JAVA'}
printSub(student1,student2)

# Hera Pheri
cast1 = ['Akshay Kumar','Suniel Shetty','Paresh Rawal','Tabu']
# Bhool Bhulaiyaa
cast2 = ['Akshay Kumar','Vidya Balan','Shiney Ahuja','Rajpal Yadav']
# Welcome
cast3 = ['Akshay Kumar','Katrina Kaif','Nana Patekar','Anil Kapoor']
# Dhamaal
cast4 = ['Sanjay Dutt','Arshad Warsi','Javad Jaffery','Riteish Deshmukh']
# Andaz Apna Apna
cast5 = ['Aamir Khan','Salman Khan','Raveena Tandon','Paresh Rawal']

movie_db = {
    "Hera Pheri": cast1,
    "Bhool Bhulaiyaa":cast2,
    "Welcome":cast3,
    "Dhamaal":cast4,
    "Andaz Apna Apna": cast5
}

'''
Task 1 : display the name of movie one by one from your movie_db

'''
def title(movie_db):
    for title in movie_db.keys():
        print(title)
        
title(movie_db)

'''
Task2: Display movie name who is having 'Akshay Kumar' init.
'''
def title(movie_db):
    for title, cast in movie_db.items():
        if 'Akshay Kumar' in cast:
            print(title)
title(movie_db)
