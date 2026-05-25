student_name = ["Sai","Rahul","Sita","Rohit","Gita","Ravi","Kumar"]

# Task 1: print Rohit from given list
list = []
for name in student_name:
    if name in ['Rohit','rohit']:
        list.append(name)
print(f"{list}")    #['Rohit']

# another way to print rohit
data = student_name[3]
print(data, type(data))


# Task 2: print Rohit in reverse order
for name in student_name:
    if name in ['Rohit','rohit']:
        print(name[::-1])   # tihoR

# another way
rev_data = data[::-1]
print(f"reverse of rohit: {rev_data}") 

# Task 3: print h from rohit
list3 = []
for name in student_name:
    if name in ['Rohit','rohit']:
        list3.append(name[2])
print(f"{list3}")   # ['h']

# another way
h_word = data[2]
print(f"h from rohit: {h_word}")

# full code in one line
print(student_name[3][::-1][2])
