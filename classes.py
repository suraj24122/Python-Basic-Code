class Employee:
    company = "HP"  # Class variable
    def get_salary(self):
        return 34000  # Instance variable
    

e1 = Employee(); #an object of Employee class created here
print(e1.get_salary());


e2 = Employee()
print(e2.get_salary()); #accessing class variable using object
 