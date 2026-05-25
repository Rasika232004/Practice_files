'''motu_list = [10,'Rahul',[45,'Priya','Pavan'],'Kiran',True]

# chotu_list
chotu_list = motu_list[2]
print(chotu_list)

# to print i from priya
chotu_list = motu_list[2][1][2]
print(chotu_list)

# print every element in list using fro loop
for i in motu_list:
    print(i)

'''
# task : display index of sita
student_name = ["Sai","Rahul","Sita","Rohit","Gita","Ravi","Kumar"]

print(student_name.index("Sita"))

# without using .index method
index = 0
sita_index = 0
for name in student_name:
    if name == "Sita":
        sita_index = index
    index=+1
print(f"index of sita: {index}")

# by using range datatype 
'''
range: it will return sequence of integer number
always -1 at end
r = range(10) always -1 at end
r = range(start,end)
r = range(start,end,step)

we can use for loop on range
'''






