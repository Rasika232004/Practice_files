# string methods
s = "Instagram"
s1 = s.upper()

print("upper() : ",s1)  # INSTAGRAM
print("Capitalize : ", s.capitalize())  # Instagram
print(s.startswith("In"))   #True
print(s.startswith("Z"))    #False
print(s.endswith("am")) #True
print(s.count)  #<built-in method count of str object at 0x0000022A1F7ED2B0>
print(s.isalpha())  #True
print(s.islower())  #False
print(s.isdigit())  #False
print(s.find("n"))  #1
print(s.split())    #['Instagram']
print(s.join("hi")) #hInstagrami
print(s.removeprefix("I"))  #nstagram
print(s.removesuffix("m"))  # Instagra
print(s.partition("t")) # ('Ins', 't', 'agram')
print(s.replace("I","G"))   # Gnstagram

# string iteration : for loop on string
""" 
ques: how to access every element from a string
=> for loop

ques: print count of the given string without using len() function
=> use count on string to calculate length of string

ques : Find count of a character in given string
=>  count = 0
    for i in "instagram":
        if i == 'a' :
            count = count +1
    print(count)
    
ques: Find whitespaces in a given string the string is s =" I love python Programming" the output should be total white spaces is {count}
=>  s = input("Enter a string : ")
    count = 0
    for i in s:
        if i == " " :
            count = count +1
    print(f"The total count of whitespace is:  ",count)
    
ques : find the ovals from the string
=>  s4 = input("Enter string : ")
    count = 0
    for i in s4:
        if i in ['a','e','i','o','u'] :
            count = count +1
    print(f"The total count of oval is: ",count)
    

"""
s2 = "Instagram and Facebook"
count = 0
for i in s2 :
    count = count +1
    print(count, i)
    
s3 = input("Enter a string : ")
char = input("Enter a character to find count: ")
count = 0
for i in s3:
    if i == char :
        count = count +1
print(f"The count of {char} is:  ",count)

s4 = input("Enter string : ")
count = 0
for i in s4:
    if i in ['a','e','i','o','u'] :
        count = count +1
print(f"The total count of oval is: ",count)
