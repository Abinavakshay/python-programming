grade=input("enter the employee's grade:")
salary=float(input("enter the salary:"))
bonus_percentage=0
if grade=='A':
    bonus_percentage=0.05
elif grade=='B':
    bonus_percentage=0.10
if salary<=10000:
    bonus_percentage+=0.02
bonus=salary*bonus_percentage
total_salary=salary+bonus
print("Your bonus is:",bonus)
print("Your salary for this month is:",total_salary)
