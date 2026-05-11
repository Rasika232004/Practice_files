# 05-05-26

#evaluation function eval()
# It recognize the input given through the terminal/console & five desired output
# built-in function in python
exp = "10+20*7/4"
res = eval(exp)
print(res)

v1 = eval(input("Enter any number: "))
print("You entered: ", v1)
print("Type: ", type(v1))