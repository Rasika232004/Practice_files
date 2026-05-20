# perfrom different functions in string
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
print(s.casefold()) # instagram
print(s.isspace())  #False
print(s.title())    #Instagram

# find oval from the string 
s2 = input("Enter string : ")
count = 0
for i in s2:
    if i in ['a','e','i','o','u'] :
        count = count +1
print(f"The total count of oval is: ",count)