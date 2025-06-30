class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print(f "Name: {self.name}, Roll:{self.roll}")
s1=Student("Ravi",15)
s1.display()        
