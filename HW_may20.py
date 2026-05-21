# perfrom different functions in string
# 45 methods perfrom on string
s = " Instagram "
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
print(s.lstrip())   # remove unwanted characters from the beginning & end of a string
print(s.rstrip())   # remove spce from right
print(s.splitlines())   #['Instagram']
print(s.strip())    # remove space between left and right
print(s.isidentifier()) #False
print(s.isprintable())  #True
print(s.ljust(4))   #  Instagram 
print(s.rjust(2))   #  Instagram 
print(s.zfill(3))    #  Instagram 
print(s.isupper())  # False
print(s.isascii())  # True
print(s.maketrans("y","a")) # {121: 97}
print(s.swapcase()) # iNSTAGRAM 
print(s.rpartition("r"))    # (' Instag', 'r', 'am ')


# find oval from the string 
s2 = input("Enter string : ")
count = 0
for i in s2:
    if i in ['a','e','i','o','u'] :
        count = count +1
print(f"The total count of oval is: ",count)