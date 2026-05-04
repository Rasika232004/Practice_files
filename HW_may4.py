mrp = float(input("Enter MRP of product: "))
discount = float(input("Enter Discount on product: "))

# calculation of selling price
s_price = mrp - ( mrp * discount / 100)
print("Selling price of product is: ", s_price)