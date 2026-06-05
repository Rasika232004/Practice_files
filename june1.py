'''
Task 1 : program to print 1 to 5 number on console

# way1
print(1,2,3,4,5)

# way2
print(1)
print(2)
print(3)
print(4)
print(5)

# way3
for num in range(1,6):
    print(num)
    
# way4
list = [1,2,3,4,5]
for num in list:
    print(num)
    
# way 5
num = 1
while num <= 5:
    print(num)
    num += 1
    
# way 6
num = 1
while num <= 5:
    print(num)
    num = num + 1
'''
'''
to print key word in python

import keyword

# Get the total count of keywords
total_keywords = len(keyword.kwlist)
print(f"Total number of keywords: {total_keywords}")

keywords = keyword.kwlist
print("Python Keywords:")
for kw in keywords:
    print(kw)
'''
'''
for i in range(1,6):
    if i == 3:
        break
    print(i)
    
# remove duplicate  from list 
# way 1
l = [1,2,2,3,5,65,32,32,5]
for num in range(len(l)):
    if l.count(num) > 1:
        l.remove(num)
print(l)
'''
'''
num = 1
while num <= 5:
    print(num)
    num += 1
print("end: ",num)  # the value of num is 6 because the loop condition is num <= 5, so when num become 6 the loop will stop and the value of num will be 6.
'''
'''
num = 1 # the value of num is 1 because the loop will start with num = 1 and the loop will continue until num <= 5, so the value of num will be 1 at the start of the loop.
while num <= 5: # the loop will continue until num <= 5, so the loop will run 5 times and the value of num will be 1,2,3,4,5 in each iteration of the loop.
    num += 1    # the value increment by 1
    print(num)  # print the incremented value of num
    num -= 2    # the printed num decrease by 2 and go for while condition 
'''
'''
find the total number of digits in a number
num = 2113
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits:", count)
'''


