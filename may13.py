#task1
''' Net salary ( total) calculation of an employee
Accept name and basic salary of an employee 
HRA = 10%
DA = 20%
PE = 12%

CALCULATE THE NET SALARY '''

print("---Employee Salary Calculator---")

name =(input("Enter the employee name:"))
basic_salary = int(input("Enter employee basic salary:"))
hra = 10*basic_salary /100
da = 20*basic_salary /100
pe = 12*basic_salary /100

net_salary = basic_salary + hra + da - pe

if net_salary >= 50000:
    grade = "A grade"
elif net_salary >= 30000:
    grade = "B grade"
elif net_salary >=15000:
    grade = "C grade"
else:
    grade = "D grade"

print("\n-----Salary Details-----")    
print("Employee Name :", name)
print("Basic Salary  :", basic_salary)
print("HRA (10%)     :", hra)
print("DA (20%)      :", da)
print("PE (12%)      :", pe)
print("-"*23)
print("Net salary    :", net_salary)
print("-"*23)
print("Salary Grade   :", grade)