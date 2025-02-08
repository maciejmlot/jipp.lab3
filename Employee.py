class Employee:
    def __init__ (self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    @staticmethod
    def from_file_string(line):
        name, age, salary = line.strip().split(",")
        return Employee(name, int(age), float(salary))

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSalary(self):
        return self.salary