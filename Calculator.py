# def addThree():
#     pass ("write some code to") # pass : used to reserve the code for future purpose.placeholder. or you dont know what to write use. 

# print(print(print(10,end=" "), end=" "), end=" ") # attribute end = "" output in single line 

# from now in interwiew write function 

'''
print("Welcome to program")
def addition(num1,num2,num3):
    print("inside function")
    sum = num1+num2+num3
    print("sum",sum) # to print none
    print("End of function")

print("Calling function")
add = addition(10,20,30)
print(add)  # give none
print("End of a program")

Output:  
Welcome to program
Calling function
None

if you don't return 'return' inside function the pvm itself return 'return'
'''
'''
Task1 : A calculator has addition operation which accept 3 numbers from user and compute addition.
'''
def addition(num1,num2,num3):
    return (num1+num2+num3)

add = addition(10,20,30)
print(add)

'''
Task2: A calculator has average operation that accept 3 number from user and compute its average 

# way1
def average(num1,num2,num3):
    return num1+num2+num3/3
result = float(average(2.3,4,6))
print(result)
'''
#way2
def average(num1,num2,num3):
    sum = addition(num1,num2,num3)  # call addition function from task 1 
    avg = sum/3
    return avg

avg = average(100,200,300)
print(avg)

'''
Task3: Write a program to check the given number is even or odd
# way 1
def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

check = check(20)
print(check)

# way 2
def check(num):
    if num % 2 == 0:
        return True
    else:
        return False

if check(20):
    print("Num is even")
else:
    print("Num is odd")
    
# way 3
def check(num):
    if num % 2 == 0:
        return True
    else:
        return False

n = 8
if check(n):
    print(f"{n} Num is even")
else:
    print(f"{n} Num is odd")
    
# way 4
def check(num):
    if num % 2 == 0:
        return True
    else:
        return False

n = 8
res = check(n)
if res:
    print(f"{n} Num is even")
else:
    print(f"{n} Num is odd")
''' 

# way 4
def check(num):
    if num % 2 == 0:
        return True
    else:
        return False

n = 8
res = check(n)
if res:
    print(f"{n} Num is even")
else:
    print(f"{n} Num is odd")
    
    


