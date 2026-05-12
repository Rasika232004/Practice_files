    
"""
there are 3 students jay, vijay and gabbar.
design a system which checks their age and display who is older among them
"""
jay_age = int(input("Enter jay age: "))
vijay_age = int(input("Enter vijay age: "))
gabbar_age = int(input("Enter gabbar age: "))
if jay_age > vijay_age and jay_age > gabbar_age :
    print(f"Jay is older")
elif vijay_age > gabbar_age and vijay_age > jay_age :
    print(f"Viay is older")
elif gabbar_age > jay_age and gabbar_age > vijay_age :
    print(f"Gabbar is older")
else:
    print("Jay, Vijay and gabbar age is same")
