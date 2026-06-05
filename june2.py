a = 10
print(a)

a = 20.4
print(a)

t = (1,2,3)
print(t)
print(id(t))

t = (4,5,6)
print(t)
print(id(t))

l = []
print(id(l))
l.append(1)
l.append(2)
print(id(l))
l.insert(2,1)
print(l)
l.extend([3,4,5])
print(l)

# convert list into immutable tuple
list1 = [1,2,3]
tuple1 = tuple(list1)
print("tuple: ",tuple1)

# how to iterate over tuple
tuple2 = (1,2,3,4,5)
for i in tuple2:
    print(i)
    
# way 2
for i in range(len(tuple2)):
    print(tuple2[i])
    
c1 = 'T-Shirt'
c2 = 'cash'
c3 = 'card'
bag = c1,c2,c3
print(bag)
print(type(bag))

bag1 = ('t-shirt','cash','card','gold')
bag2 = ('t-shirt','cash','card','gold')

v1,v2,v3,v4 = bag1
p1,p2,p3,p4 = bag2

print(v1,v2,v3,v4)  # t-shirt cash card gold
print(p1,p2,p3,p4)  # t-shirt cash card gold

'''
a,b = bag1  # error because bag1 has 4 elements but we are trying to unpack into 2 variables
print(a) 
'''


a,*b = bag1 # a will get the first element of bag1 and b will get the rest of the elements as a list
print(a)  # t-shirt

a,*b,c = bag1 # error because we are trying to unpack into 3 variables but bag1 has only 4 elements and we are trying to unpack into 3 variables
print(a)  # t-shirt
print(b)  # ['cash', 'card']
print(c)  # gold

'''
Explanation of the swapping code: 
In the code snippet, we have two variables num1 and num2 with initial values 10 and 20 respectively. 
The line num1 , num2 = num2 , num1 is a Pythonic way to swap the values of num1 and num2 without using a temporary variable.
'''
num1 = 10
num2 = 20
num1 , num2 = num2 , num1  # swapping values of num1 and num2
print(num1)  # 20
print(num2)  # 10