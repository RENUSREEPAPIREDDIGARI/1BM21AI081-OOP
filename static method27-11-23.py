'''class BMS:
    def display(self):
        self.collegename="BMSCE"
        print(self.collegename)
    def add(n1,n2):
        print(n1+n2)
BMS.add(30,20) '''


#Calculator 

class calculator :
    def __init__(self,version):
        self.version=version
    def display(self):
        print(self.version)
    def add(n1,n2):
        return n1+n2
if __name__=="__main__":
    C1=calculator(4)
    C1.display()
    sum=calculator.add(20,30)
    print(sum)
