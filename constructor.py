#program created using constructor(parameterized).

class Student:                                              #class name
    def __init__(self,name,age):                            #parameterized constructor
        self.name=name
        self.age=age
        print("This is parameterized constructor")
    def display(self):                                      #method to display                               
        print("My name is: ",self.name)
        print("My age is: ",self.age)
student=Student("Max",30)
student.display()


