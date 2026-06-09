class student:
    college_name = "abc college" 
    
    def __init__(self, name, cgpa):
        self.name = name 
        self.cgpa = cgpa 
        
    @classmethod
    def change_college_name(cls, new_name):
        cls.college_name = new_name
        print(f"College name changed to: {cls.college_name}")
        
    @staticmethod
    def is_pass(cgpa):
        return cgpa >= 5.0

student1 = student("gulu", 4.5)
print(f"Student: {student1.name}, CGPA: {student1.cgpa}")
print(f"Is pass? {student1.is_pass(student1.cgpa)}")
student1.change_college_name("xyz college")