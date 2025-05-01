class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary;
        self.name = name;
        self.bond = bond;

    def get_salary(self):
        return self.salary;
    
    def get_info(self):
        print(f"the name of the employee is {self.name} and the bond is {self.bond} years. and self salary is {self.salary}");

e1 = Employee(34000, "John", 2); #an object of Employee class created here
print(e1.get_salary()); #accessing instance variable using object
e1.get_info();







