class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def add(c1,c2,c3):
        c3.real=c1.real+c2.real
        c3.img=c1.img+c2.img
        print("the sum is :",c3.real,"+i",c3.img)
c1=complex(5,2)
c2=complex(3,2)
c3=complex(0,0)
complex.add(c1,c2,c3)