s = "instagram"
# if end index positive end_index-1 if end index is negative end_index+1 
# direction mater most 
# positve left to right 
print(s[0:5]) # insta
print(s[0:5:2]) #isa
print(s[0:5:3]) #it
print(s[0:5:4]) #ia
print(s[0:5:5]) #i
print(s[0:5:6]) #i & so on

# -ve right to  left 
print(s[8:4:-1]) #marg
print(s[6:2:-2]) # ra
print(s[9:7:-3]) #m 
print(s[8:4:-6]) #m because it is out of range start from m end at a step -6 is out of 
print(s[4:8:-1])

# print only t 
print(s[3:4])
print(s[3:8:5])
print(s[-6:-7:-1])


