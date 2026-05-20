name = "Rasika Satpute"

#   0    1    2    3    4    5   6   7   8  9   10  11  12  13
#   R    A    S    I    k    A   _   S   A   T   P   U   T   E
#  -14  -13  -12  -11  -10  -9  -8  -7  -6  -5  -4  -3   -2  -1

# +ve +ve +ve
print(name[0:15]) 

# +ve +ve -ve
print(name[0:14:-1])

# -ve -ve +ve
print(name[-14:-1])

# -ve +ve +ve
print(name[-14:14])

# +ve -ve +ve
print(name[0:-1])

# -ve -ve +ve
print(name[-14:-1:1])

# -ve -ve -ve
print(name[-1:-15:-1])