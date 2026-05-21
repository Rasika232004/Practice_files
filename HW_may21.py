# Task 1: print Rohit from given list
student_name = ["Sai","Rahul","Sita","Rohit","Gita","Ravi","Kumar"]

list = []
for name in student_name:
    if name in ['Rohit','rohit']:
        list.append(name)
print(f"{list}")    #['Rohit']

# Task 2: print Rohit in reverse order
for name in student_name:
    if name in ['Rohit','rohit']:
        print(name[::-1])   # tihoR


# Task 3: print h from rohit
list3 = []
for name in student_name:
    if name in ['Rohit','rohit']:
        list3.append(name[2])
print(f"{list3}")   # ['h']
