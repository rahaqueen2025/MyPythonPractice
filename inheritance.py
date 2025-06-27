class Person:
    """" Most relate attributes to each person"""
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
        
    def introduce(self):
        return f"Hi , I am {self.get_full_name()},and I am {self.age} years old"

    def __str__(self):
        return self.introduce()
    
class Staff(Person):     #inheritance from Person
    """" Most related attributes to each staff"""  
    def __init__(self, first_name, last_name, age,national_id,experience):
        super().__init__(first_name, last_name, age)
        self.national_id=national_id
        self.experience=experience

    def introduce(self):
        inherited_string = super(). introduce() 
        return f"This is inherited string: {inherited_string}"   
          
    


person_1=Person("David","Doe",45)
person_2=Person("Robert","Robinson",26)

print(person_1)
print(person_2)


staff_1=Staff("John","Stark",32,"89562134",5)
print(staff_1)
print(staff_1.first_name)
print(staff_1.national_id)
print(staff_1.experience)



