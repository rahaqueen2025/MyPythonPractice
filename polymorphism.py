#poly=multi
#morphism=Appearance

#name="David"
#emails=['user@gmail.com','admin@gmail.com']
#password=("123bnmhjkl")

#print(len(emails))
#print(len(password))


# MRO=Method Resolution Order

class A:
    def introduce(self):
        print("Hi I am A")

class B(A):
    def introduce(self):
        print("Hi I am B") 

class C(B):
    def introduce(self):
        print("Hi I am C")

class D(C,A):   
    pass     
            

#b=B()
#b.introduce()    
#print(B.mro())  

#c=C()
#.introduce() 
#print(C.mro()) 

#print(D.mro())

#c=C()
#print(isinstance(c,A))

b=B()
value=100
#print(isinstance(value,int))
print(issubclass(b,B))


   