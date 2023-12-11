class Employee:
    def __init__(self, name, salary):
        self._name = name 
        self.__salary = salary 
    def work(self):
        return f"{self._name} is working."

    def show(self):
        return f"Name: {self._name}, Salary: {self.__salary}"
    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

emp = Employee("renz", 50000)

print(emp.work()) 
print(emp.show()) 

print(emp.get_salary()) 
emp.set_salary(55000)
print(emp.get_salary())  

print(emp.show())  

