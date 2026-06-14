class employee:
    def get_salary(self):
        print("Employee salary is $50000")
    
class manager(employee):
    def get_salary(self):
        print("Manager salary is $80000")

employee1 = employee()
manager1 = manager()
manager1.get_salary() # Output: Manager salary is $80000