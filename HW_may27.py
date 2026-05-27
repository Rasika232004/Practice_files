'''
Task 1: Add 18% gst in bill
'''
units = float(input("Enter units : "))
price_per_unit = 8
total_cost = units*price_per_unit

gst = total_cost * 0.18
final_bill = total_cost+gst

if units >=300 :
    units += 500
    print("Added extra 500 :", units)
else:
    units += 100
    print("Added extra 100 :", units)

print("Total bill : ", final_bill)


'''
Task 2: if 0<=units<=50 :
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
