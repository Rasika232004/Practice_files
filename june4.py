'''
Make a table that what operaters can be perfromed on each datatype with reason and code example
'''
'''
Today session: Dictionary 
insertion order is maintain
'''
'''
This student_db is level 0 dict
'''

student_db = {}
student_db[5] = "Shreya"
student_db[2] = "Jay"
student_db[8] = "Rahul"
student_db[11] = "Priya"

print(student_db)

# print how many students are in dict
print(len(student_db))

print(student_db.keys())
# ew con convert dict in any list set tuple etc
# roll = list(student_db.keys())
# roll = set(student_db.keys())
# print(type(roll))
print(student_db.values())
print(student_db.items())   # give list of tuples
print(student_db.get(8))

# iterate keys
for roll in  student_db:
    print(roll) # print all keys

for roll in student_db.keys() :
    print("\nKeys",roll)
    
# iterate values
for values in student_db.values():
    print("\nvalue",values)
    
for values in student_db:
    print("\nvalue",student_db.values())
    
# iterate items
for item in student_db.items():
    print("\nkey and value",item)

for item in student_db:
    print("\nkey and value",student_db.items())    
    
for item in student_db.items():
    print(item[0], item[1]) 

for item in student_db.items():
    roll, name = item
    print(roll, name) 
    
for roll,name in student_db.items():
    # roll, name = item
    print(roll,name) 
    
'''
print roll numbers of student whose name contain "y" character
'''
student_db = {}
student_db[5] = "Shreya"
student_db[2] = "Jay"
student_db[8] = "Rahul"
student_db[11] = "Priya"

print(student_db)

for roll,name in student_db.items():
    if 'y' in name:
        print("student roll", roll)
    
