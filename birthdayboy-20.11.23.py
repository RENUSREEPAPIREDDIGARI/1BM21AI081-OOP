'''create a python class called birthdayboy that takes 2 variable:
a.Astring name
b.an interger age
within birthdayboy.create a method called birthday that increases the value of age by 1
once this class has been created,create a instance of the classs then call birthday methods on that to increase its age and print the same''' 

class birthdayboy:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    def birthday(self):
         self.age=self.age+1
         print(self.age)
b1=birthdayboy('Max',19)    
b1.birthday()    
