"""
Task 1:
sensus_date = ['m','m','f','f','f','m','f','m','m','f','f','f','f']
find total count of male and female
"""
# way 1
sensus_date = ['m','m','f','f','f','m','f','m','m','f','f','f','f']
print("Male count",sensus_date.count("m"))
print("Female count",sensus_date.count("f"))

# way2
male = 0
female = 0
for gender in sensus_date:
    if gender == 'm':
        male = male + gender
    else:
        female = female + gender
print(f"Male count: {male}")
print(f"Female count: {female}")

# way 3
male = 0
female = 0
for gender in sensus_date:
    if gender == 'm':
        male = male + 1
print(f"Female count:", len(sensus_date)-male)


# Task 2: Find total count of student whose name start with P
name = ['Ajay','Priya','Viru','Raj','Payl','Rohan']

# way 1
count = 0
for name in name:
    if name.startswith('P'):
        count = count + 1
print(f"Count of student name start with P: {count}")

# way2
count = 0
for names in name:
    if names[0] =="P":
        count = count+1
print(count)

name = [['Ajay','Priya','Pavan'],['Viru','Raj','Payl'],['Rohan']]

# print all names
for chotu_list in name:
    for name in chotu_list:
        for ch in name:
            print(ch)

