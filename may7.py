# 07-05-2026
# Topic :- String Formatting
# popular approach is f string 

roll = 3    # static inputs 
name = "jay"
per = 90.344663423

# WAY 1 
a = f"Student roll number {roll} is and name is {name} and percentage got is {per:.2f}. "
print(a)

# WAY 2
b = "Student roll number " + str(roll) + " is and name is " + str(name)
print(b)

#this called file handling (Dynamic)
filename = input("Enter filename:")
path = f"C:/Users/hp/Desktop/{filename}"
print(path)

# want to show roll as 002  
c = f"Student roll number {roll:03d} is and name is {name} and percentage got is {per:.2f}. "
print(c)

# there is one array. Write a program to find maximum number from array.
# shortest way to find max in an array
arr = [1,45,23,54,67]
print(max(arr))

# we can make table by 
# to make it dynamic take input as variable name & value frim console
print("-"*25)   #simple way to create multiple hypne ---- 
print("| Roll | Name | PER |")
print("-"*25)
print(f"| {roll:<4} | {name:^4} | {per:>4.2f} |")

# .format method
s1 = "Student roll number is {} name is {} and percentage is {}".format(roll, name, per)
print(s1)

s2 = "Student roll number is {0} name is {1} and percentage is {2}".format(roll, name, per)
print(s2)

s3 = "Student roll number is {v1} name is {v2} and percentage is {v3}".format(v1=roll,v2=name, v3=per)
print(s3)

s4 = "Student roll number is %d name is %s and percentage is %f"%(roll, name, per)
print(s4)

