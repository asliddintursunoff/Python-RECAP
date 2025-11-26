"""
THIS IS FOR PRACTISING PROPERTY METHODS
"""
import datetime

class Profile:
    def __init__(self,first_name,last_name,birth_year):
        self.first_name = first_name
        self.name = first_name+' '+ last_name
        self.birth_year = birth_year

    @property
    def name(self):
        return self._first_name +' '+ self._last_name
    
    @name.setter
    def name(self,name:str):
        if isinstance(name,str):
            self._first_name = name.split()[0]
            self._last_name = name.split()[1]
        else:
            self._first_name = ""
            self._last_name = ""

    @property
    def age(self):
        current_year = datetime.datetime.now().year
        return current_year - self._birth_year
    
    @property
    def birth_year(self):
        return self._birth_year
    @birth_year.setter
    def birth_year(self,year):
        current_year = datetime.datetime.now().year
        if current_year-year<18:
            print("You are not allowed this is for adults!")
            self._birth_year = current_year
        else:
            self._birth_year = year

person1 = Profile("Asliddin","Tursunov",2006)
print(person1.name)
person1.birth_year = 2009
print(person1.age)
