salary = int(input("Enter Your Salary: "))

if salary<=30000:
    print(f"Your Salary is: {salary}")
    print("Your tax will be: 5%")
    tax = salary*0.005
    finalSalary = salary-tax
    print(f"After applying tax: {tax} your salary is: {finalSalary}")
elif salary<=70000:
    print(f"Your Salary is: {salary}")
    print("Your tax will be: 15%")
    tax = salary*0.015
    finalSalary = salary-tax
    print(f"After applying tax: {tax} your salary is: {finalSalary}")
elif salary>=70000:
    print(f"Your Salary is: {salary}")
    print("Your tax will bex: 25%")
    tax = salary*0.025
    finalSalary = salary-tax
    print(f"After applying tax: {tax} your salary is: {finalSalary}")