class User:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    @property       # for change this function to attribute
    def password(self):
        return self._password.upper()    
    
    @password.setter
    def password(self,value):
        if len(value) > 8:
            self._password=value



user_1=User("my_username","998wrutkfg")
#print(user_1.password)
#user_1.password="wertyuiopk"
#print(user_1.password)
print(user_1._User__password)
        