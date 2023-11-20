
class dog:
    def __init__(self,name,size,breed,dob):
        self.name=name
        self.size=size
        self.breed=breed
        self.dob=dob
    def bark(self):
        print('woof')
    def get_name(self):
        print(self.name)
    def set_name(self,new_name):
        if isinstance(new_name,str)and 2<= len(new_name)<=30 and new_name.isalpha():
           self.name=new_name.title()
        else:
            print("invaild name please enter again")
    def dog_years(self):
        birth_year = int(self.dob[-4:])
        current_year=2023
        human_years=current_year-birth_year
        dog_years=human_years*7
        return dog_years
my_dog = dog("Buddy", "Medium", "Golden Retriever", "15/05/2019")
my_dog.set_name("poppy")  
my_dog.get_name()
my_dog.bark()
print(my_dog.dog_years())
          