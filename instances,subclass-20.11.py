'''write a python to create two empty class,student,marks.now create some instances and check whether they are instances  
of the said classes or not. Also check whether the said classes are subclasses of built in object class or not'''
class Student():
    pass
class Marks():
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))

print(issubclass(Student, object))
print(issubclass(Marks, object))