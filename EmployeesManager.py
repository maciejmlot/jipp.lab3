import os
import Employee

class EmployeesManager:
    def __init__ (self):
        self.employeeList = self.loadEmployees()
    
    def loadEmployees(self):
        if not os.path.exists("employees_list.txt"):
            return []
        with open("employees_list.txt", "r") as file:
            return [Employee.Employee.from_file_string(line) for line in file.readlines()]

    def saveEmployees(self):
        with open("employees_list.txt", "w") as file:
            file.writelines(f"{emp.name},{emp.age},{emp.salary}\n" for emp in self.employeeList)

    def addEmployee (self, name, age, salary):
        employee = Employee.Employee (name, age, salary)
        self.employeeList.append(employee)
        self.saveEmployees()

    def printEmployees (self):
        i = 1
        for emp in self.employeeList:
            print(str(i) + ". " + emp.name + ", "+ str(emp.age) + "yo, $"+ str(emp.salary))
            i += 1
    
    def removeAgeRangeFromList (self, start, end):
        self.employeeList = [emp for emp in self.employeeList if not (start <= emp.age <= end)]
        self.saveEmployees()

    def findEmployeeByName (self, name):
        for emp in self.employeeList:
            if emp.name == name:
                return emp
        print ("Nie znaleziono pracownika.")
        return None
    
    def raiseByName (self, name, rise):
        emp = self.findEmployeeByName(name)
        if emp:
            emp.salary += rise
            self.saveEmployees()
