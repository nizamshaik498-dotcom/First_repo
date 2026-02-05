#program created using multilevel inheritance

class Animal:                                   #base class
    def speak(self):                   
        print("Animal Sound")
class Dog(Animal):                                 
    def bark(self):                     
        print("Barking sound")
d=Dog()
d.speak()
d.bark()