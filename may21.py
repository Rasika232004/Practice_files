
varname = ['rose','sunfolwer']
print(type(varname))

list = [1,2,3,45]

for i in varname:
    list.append(i)
print(list) # [1, 2, 3, 45, 'rose', 'sunfolwer']

print(list[1]*list[1])  # 4
print(len(list)) # 6

data = varname[0:1]
print(data) # ['rose']

for i in list:
    print(i)
    
student_name = ["Sai","Rahul","Rohit","Sita","Gita","Ravi","Kumar"]

# Task 1 : Find total students from your class
count = 0
for i in student_name:
    count = count +1
print("Total students in your class is: ",count)
# print("Total students in your class is: ",len(student_name))

# Task 2 : Find total student in the class whose name size is 4 only
count = 0
for i in student_name:
    if len(i) == 4:
        count = count +1
print("Total student in the class whose name size is 4 only: ",count)

# Task 3: Find total students whose name contain letter "i" in it
count = 0
for i in student_name:
    if "i" in i:
        count = count +1
print(f"total students whose name contain letter 'i' in it : {count}")

# Task 4: create a small list of students name start with "R" and print it
list = []
for name in student_name:
    if name[0] == "R":
        list.append(name)
print(f"small list of students name start with 'R' {list}")

# another way
list = []
for name in student_name:
    if name.startswith("R"):
        list.append(name)
print(f"small list of students name start with 'R' {list}")

# Task 5: create a small list of students name end with "a" and print it don't use endswith
list = []
for name in student_name:
    if name[-1] == "a":
        list.append(name)
print(f"List of names ends with 'a' {list}")



