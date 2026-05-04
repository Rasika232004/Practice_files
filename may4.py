# 04-05-2026
#input function returns string data by default

# program 1
v1 = input("Enter a number: ")
print("You entered : ", v1) # print number
print("Type of v1 : ", type(v1))    # type of the variable
print("Memory address of v1 : ", id(v1))    #show memory address of the 
print("-----------------------------------------------------------")

# we need to typecast (data conversion) v1 to an integer to perform arithmetic operation
v1 = int(v1)
print("You entered : ", v1)
print("Type of v1 : ", type(v1))
print("Memory address of v1 : ", id(v1)) 
print("-----------------------------------------------------------")

v1 = float(v1)
print("You entered : ", v1)
print("Type of v1 : ", type(v1))
print("Memory address of v1 : ", id(v1)) 
print("-----------------------------------------------------------")

# not converting saperetly we do n = int(input("Enter number: ")) direct type coversion
#saves memory , optimize code
v2 = int(input("Enter number :"))
print("You entered : ", v2)
print("Type", type(v2))
print("Memory address : ", id(v2)) 



