from abc import ABC,abstractmethod
class car(ABC):
    def __init__(self,mg):
        self.mg=mg
    @abstractmethod
    def mileage(self):
        pass
    
class audi(car):
    def mileage(self):
        print("mileage of audi",self.mg)
c1=audi(40)
c1.mileage()

class BMW(car):
    def mileage(self):
        print("mileage of audi",self.mg)
c1=BMW(60)
c1.mileage()