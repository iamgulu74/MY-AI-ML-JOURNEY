class student:
    def __init__(self, name,cgpa):
        self.name = name
        self.cgpa = cgpa
        
    def get_cgpa(self):
            return self.cgpa

gulu=student("gulu", 9.5)
a=student("a", 9.0)
print(gulu.name, gulu.cgpa)
print(a.name, a.cgpa)

print(gulu.get_cgpa())