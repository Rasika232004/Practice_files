#task 1
"""
Title:- Net Salary (Total) calculation of an employee

Accept name & basic salary of an employee. 
HRA = 10%   DA = 20%    PF = 12% ==== Net salary
"""

name = input("Enter employee name: ")
b_salary = float(input("Enter Basic salary of employee: "))

hra = b_salary * 0.10
da = b_salary * 0.20
pf = b_salary * 0.12

net_salary = (b_salary + hra + da)-pf

print("-"*45)
print(f"|{'Name':^20}|{'Net Salary':^20}|")
print("-"*45)
print(f"|{name:^20}|{net_salary:^20}|")
print("-"*45)




