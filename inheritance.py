class employee:
    start_time="9:00"
    end_time="5:00"
    
    def change_start_time(self,new_time):
        self.start_time=new_time
        
class teacher(employee):
    def __init__(self,name):
        self.name=name

teacher1=teacher("gulu\n")
teacher1.change_start_time("8:00")
print(f"Teacher Name: {teacher1.name}, Start Time: {teacher1.start_time}, End Time: {teacher1.end_time}")
