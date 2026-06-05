'''
Task 1: l = [45,-7,87, -67, 45,33,-33,91,65,-56]
WAP to print all -ve numbers from the list
'''

# way 1
l = [45,-7,87, -67, 45,33,-33,91,65,-56]
for i in l:
    if i < 0:
        print(i)
        
# way 2
l = [45,-7,87, -67, 45,33,-33,91,65,-56]
negatives = [i for i in l if i < 0]
print(negatives)

'''
Task 2: l = [45,-7,87, -67, 45,33,-33,91,65,-56]
WAP to print all -ve numbers from the list
with -ve numbers print messge as start of for loop print at once should no increament with number, start of if condition, end of if condition, end of for loop 
'''

list = [45,-7,87, -67, 45,33,-33,91,65,-56]
print("\nStart of for loop")
for num in list:
    print("\nStart of if condition")
    if num < 0:
        print("\nNumber",num)
    print("\nEnd of if condition")
print("\nEnd of for loop")

'''
Task 3 : display count of all even negative numbers from the list

'''
even_count = 0
l = [45,-7,87, -67, 45,33,-33,91,65,-56]
for num in l:
    if num < 0 and num % 2 == 0:
        even_count += 1
print(f"Count of even negative numbers: {even_count}")

# way 2
l = [45,-7,87, -67, 45,33,-33,91,65,-56]
even_count = sum(1 for num in l if num < 0 and num % 2 == 0)
print(f"Count of even negative numbers: {even_count}")


