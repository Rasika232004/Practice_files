'''
Task 1: there are few order id's in a list.
check whether the order id is even or odd.
order_id = [11,23,43,12,46,78,1211234,7634,734628,9999999]
even_id = []
odd_id = []
for id in order_id:
    
    if id % 2 == 0:
        even_id.append(id)
    else:
        odd_id.append(id)
print(f"Even id's in list: {even_id}")
print(f"Odd id's in list: {odd_id}")

for id in order_id:
    if id % 2 == 0:
        print(f"id are even")
    elif id % 2 != 0:
        print(f"id's are odd")
    else:
        print("the list contain even and odd id's")

''' 

'''
Task 2 : Smart electricity bill generator 
input => number of electricity units
condition -> units >= 300 : Exter subcharges Rs 500
             otherwise surcharges rs 100
             
print total bill 
    bill = units * 8
    
# way 1
units = float(input("Enter units : "))
if units >=300 :
    units += 500
    print("Added exter 500 :", units)
else:
    units += 100
    print("Added exter 100 :", units)
    
print("Total bill : ", units*8)

# way 2
units = float(input("Enter units : "))
price_per_unit = 8
total_cost = units*price_per_unit

if units >=300 :
    units += 500
    print("Added exter 500 :", units)
else:
    units += 100
    print("Added exter 100 :", units)

print("Total bill : ", total_cost)
'''
'''
Task 3: Add 18% gst in bill

units = float(input("Enter units : "))
price_per_unit = 8
total_cost = units*price_per_unit

gst = total_cost * 0.18
final_bill = total_cost+gst

if units >=300 :
    units += 500
    print("Added exter 500 :", units)
else:
    units += 100
    print("Added exter 100 :", units)

print("Total bill : ", final_bill)
'''

'''
Task 4: if 0<=units<=50 :
    print("No bill")
    elif 51<= units <= 100 :
    units *= 5
    print("5 rs per unit")
'''
units = float(input("Enter units : "))
price_per_unit = 8
total_cost = units*price_per_unit

gst = total_cost * 0.18
final_bill = total_cost+gst

if 0<=units<=50 :
    print("No bill")
elif 51<= units <= 100 :
    total_cost = units * 5
elif units >=300 :
    units += 500
    print("Added exter 500 :", units)
else:
    units += 100
    print("Added exter 100 :", units)

print("Total bill : ", final_bill)
