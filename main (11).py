class creditcard:
    def __init__(self,balance,limit):
        self.balance=balance
        self.__limit=limit
   
    def get_balance(self):
        print(self.balance)
   
    def withdraw(self,a):
        if(self.balance-a < self.__limit):
            print("no sufficient balance")
        else:
            self.balance=self.balance-a
   
    def deposit(self,a):
        self.balance=self.balance+a
       
    def display(self):
        print(self.__limit)

c1=creditcard(1000,100)

c1.withdraw(1000)
c1.get_balance()

c1.display()