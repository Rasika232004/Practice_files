'''
print(l1-l2)
gives : Traceback (most recent call last):
  File "D:\python 1333 batch ws\may25.py", line 7, in <module>
    print(l1-l2)
          ~~^~~
TypeError: unsupported operand type(s) for -: 'list' and 'list'

print(l1*3.5)
Traceback (most recent call last):
File "D:\python 1333 batch ws\may25.py", line 14, in <module>
print(l1*3.5)
          ~~^~~~
TypeError: can't multiply sequence by non-int of type 'float'

# perform this operations on string over list and create a table

# python work on DRY : Do Not Repeat Your 
'''

# Task 1: add tow lists
l1 = [1,2,3]
l2 = [5,6,7]
print(l1+l2)

#Task 2: account department wants sum of all salary to find total expendeture on employee salary. (don't use sum function)
salary = [67000, 45000, 78000, 55000, 28000]
print(salary[0]+salary[1]+salary[2]+salary[3]+salary[4])    #273000

total = 0
for s in salary:
    total = total +s
print(total)

print(sum(salary))

# Task 3: find sum of odd index salary from given list
salary = [67000, 45000, 78000, 55000, 28000]

t = 0 
for i in range(1,len(salary),2):
    t = t + salary[i]
print(t)

t = 0
for i in range(len(salary)):
    if i % 2 == 1:
        t = t + salary[i]
print(t)

# Task 4: find sum of even index salary from given list
salary = [67000, 45000, 78000, 55000, 28000]

t = 0 
for i in range(0,len(salary),2):
    print(i)
    t = t + salary[i]
print(t)

t = 0
for i in range(len(salary)):
    if i % 2 == 0:
        t = t + salary[i]
print(t)

# Task 5: find sum of first half of the list employees salary
salary = [67000, 45000, 78000, 55000, 28000,44000,33000]
t = 0
half = len(salary)//2
for i in range(half):    # or for i in range(len(salary)//2):
    # print(i)
    t = t + salary[i]
print(t)

# Task 6: find sum of second half of the list employees salary
salary = [67000, 45000, 78000, 55000, 28000,44000,33000]
t = 0
half = len(salary)%2
for i in range(half,len(salary)):  
    # print(i)
    t = t + salary[i]
print(t)

# next half salary
next_half = sum(salary) - t

# Task 7: find first half of the string
s = "instagram"
for i in range(len(s)//2):
    print(s[i])



    