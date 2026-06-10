class student:
    college_name = "abc college" # class variable
    
    def __init__(self, name,cgpa):
        self.name = name # instance variable
        self.cgpa = cgpa # instance variable 
        
student1 = student("gulu", 9.5)

print(student1.name) # accessing instance variable