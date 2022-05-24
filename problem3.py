import numpy as np

employeeNames = np.array(["abc", "asf", "ges", "wag"])
salaries = np.array([10, 20, 30, 40])

while True:
    command = input("Command")
    if command == "Insert":
        employeeName = input()
        salary = float(input())
        employeeName = np.append(employeeNames, employeeName)
        salaries = np.append(salaries, salary)

    elif command == "Change":
        employeeName = input()
        salary = float(input())
        salaries[employeeNames == employeeName] = salary

    elif command == "LookUp":
        employeeName = input()
        print(salaries[employeeNames == employeeName])

    elif command == "IncreaseMoreThan":
        lowestSalary = float(input())
        percentageIncrease = float(input())
        salaries[salaries < lowestSalary] = salaries[salaries < lowestSalary] * (100 + percentageIncrease) / 100

    elif command == "IncreaseLessThan":
        highestSalary = float(input())
        percentageDecrease = float(input())
        salaries[salaries > highestSalary] = salaries[salaries > highestSalary] * (100 - percentageDecrease) / 100
        
    elif command == "MaxSalaryEmployee":
        print(employeeNames[np.argmax(salaries)])
    elif command == "MinSalaryEmployee":
        print(employeeNames[np.argmin(salaries)])
    elif command == "DeleteEmployee":
        employeeName = input()
        salaries = salaries[employeeNames != employeeName]
        employeeNames = employeeNames[employeeNames != employeeName]
    elif command == "EmployeesEarningMoreThan":
        lowestSalary = float(input())
        print(employeeNames[salaries > lowestSalary])
    elif command == "EmployeesEarningLessThan":
        highestSalary = float(input())
        print(employeeNames[salaries < highestSalary])
    else:
        break