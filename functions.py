#def say_hello():                                   #تعریف فانکشن
#    print("hello world")

#say_hello()                                         #فراخوانی فانکشن
#say_hello()

#def say_hello(name):
#    print(f"Hello ,{name}")

#say_hello("raha")

#def say_hello(name):
#    print(f"Hello ,{name}")

#my_name=input("enter your name:")   #متغیری که تعریف کردم فقط توی همون تابع  میتونم ازش استفاده کنم#scoop                
#say_hello("raha")

#value=10
#def say_hello(name):
#    print(f"Hello ,{name},and your value is:{value}")

#my_name=input("enter your name:")
#say_hello(value)

#def product_of_two_numbers(first_number:int,second_number:int):
#    value=first_number*second_number
#    print(value)

#product_of_two_numbers(25,3) 

#ساخت فانکشن ماشین حساب ساده که چهار عمل اصلی رو انجام بده   
#def calculator(first_number:int,second_number:int,operation_type:str):

# make the operation type clear

#    operation_type=operation_type.lower()
#    operation_type=operation_type.strip()
    
#conditions section
#    if operation_type=="sum":
#        value=first_number + second_number
#    elif operation_type=="sub":
#        value=first_number - second_number
#    elif operation_type=="devision":
#        value=first_number//second_number
#    elif operation_type=="mult":
#        value=first_number*second_number
#    else:
#        value="please enter a valid value as operation type"
#    print(value)

# Gather input from user
#first_number=int(input("plese enter the first number:"))  
#second_number=int(input("please enter the second number:")) 

#operation_type=input("please enter the operation type:")

#calculator(first_number,second_number,operation_type)

#def sum_values(*args):
#    print(args)
#sum_values(5,4,3,2,1)   

#def sum_values(*args):
#    for value in args:
#        print(value) 
#sum_values(5,4,3,2,1)   

#def say_hello(*names):
#    for name in names:
#        print(f"Hello,{name}")
        
#say_hello("John","David","Robert")  

#def say_hello(first_name,last_name):
#    print(first_name,last_name)
#say_hello(last_name="Doe",first_name="John")   
 
#def say_hello(**values):
#    print(values)
#say_hello(last_name="Doe",first_name="John")    
# *args= give tuple data
# **args=give dictionary data
#def say_hello(first_name,age,*args,**values):
#    print(first_name)
#    print(age)
#    print(args)
#    print(values)
#say_hello("john",41,"Hello",last_name="Doe")    

#def sum_values(first_value,second_value):
#    final_value= first_value + second_value
#    return final_value
#print(sum_values(2,5))
# other type of writting code line 94 is like line 96-97 
#value=sum_values(2,5)  
#print(value)   

#def calculator(first_value,second_value):
#    sum_value= first_value + second_value
#    subtract_value=first_value - second_value
#    return sum_value,subtract_value

#value= calculator(2,5) 
#print(value)   


#def area_calculator(lenght,width):
#    return area

#lenght=int(input("Enter the lenght of rectangel:"))
#width=int(input("Enter the width of rectangel:"))

#area=area_calculator(lenght,width)
#print(area)

#my_function=lambda x:x**2
#print(my_function(4))

#my_list=list(range(20))
#print(my_list)
#def filter_function(number):
#    if number % 2:
#        return False
#    return True

#even_values=list(filter(filter_function,my_list))
#print(even_values)
# instead above rewrite with lambda see buttom 
#my_list=list(range(20))   
#ven_values=list(filter(lambda number: not number % 2,my_list))
#print(even_values)  


#def map_function(number):
#    return str(number)

#my_list=list(range(20))  
#my_str_list=list(map(map_function,my_list))
#print(my_str_list)
# یا به صورت زیر
#my_str_list=list(map(lambda number:number*2,my_list))
#print(my_str_list)


#def say_hello(name):
#    pass
#def say_hello(name):
#    ...


#def power(*args):
    #even_values=list(filter(lambda number:not number % 2,args))
    #return_value=list(map(lambda number:number**2,args)) 
    #return return_value

#numbers=input("Enter some values:")
#numbers=numbers.split()
#numbers=list(map(lambda number:int(number),numbers))

#final_value=power(*numbers)
#print(*final_value,sep="\n")




          

