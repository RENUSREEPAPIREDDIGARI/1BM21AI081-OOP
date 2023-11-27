class student:
    counter=0
    def __init__(self,n,m):
        self.name=n
        self.marks=m
        student.counter+=1
    def display(self):
        print(self.name)
        print(self.marks)
        print(student.counter)
    @classmethod  
    def obj_count(cls):
        return cls.counter
if __name__=="__main__":
    s1=student('k',20)
    s2=student('kk',30)
    print("using classmethod")
    print(student.obj_count())
    s2.display()    