#decorators=عملکرد یک فانکشن رو تغییرمیدن بدون اینکه خود اون فانکشن تغییر کنه 
# ورودی فانکشن میگیره   

#        func()
#        print("say hello function called")     
#    return wrapper

#@first_decorator
#def say_hello():
#    print("Hello World")

#@first_decorator
#def say_goodbye():
#    print("Goodbye")    

#say_hello()
#say_goodbye()    


#نوشتن decorator برای فانکشن های با چند ورودی 
#import time

#def first_decorator(func):
#    def wrapper(*args,**kwargs):
#        print("start counting...")
#        started_at = time.time()
#        func(*args ,**kwargs)  #اگر بخوام اسم با حروف بزرگ تایپ بشه
#        finished_at = time.time() 
#        print(f"The {func.__name__} took{finished_at -started_at} seconds to run")
#    return wrapper

#@first_decorator
#def say_hello(name):
#    print(f"Hello {name}")

#@first_decorator
#def say_goodbye(name):
#    print(f"Goodbye {name}")    

#say_hello("ra")
#say_goodbye("Dr")    
                       


#import time                  

#def first_decorator(func):
#    def wrapper(*args,**kwargs):
#        print("start counting...")
#        started_at = time.time()
#        func(*args ,**kwargs)  #اگر بخوام اسم با حروف بزرگ تایپ بشه
#        finished_at = time.time() 
#        print(f"The {func.__name__} took{finished_at -started_at} seconds to run")
#    return wrapper

#@first_decorator
#def sum_numbers():
#    sum = 0
#    for i in range(100000000):
#        sum += i
#        print(f"result is:{sum}")


#sum_numbers()  
     

#walrus operator  شیردریایی
#if (name:= "David") == "David":
#    print("How are you David")

#data = input("Enter a value:")

#while data !='exit':
#    print(f"You entered: {data}")
#    data = input("Enter a value:")
# به جای شکل بالا میتونیم مثل پایین در یک خط بنویسیم

#while (data :=input("Enter a value: ")) !='exit':
#    print(f"You entered:{data}")


#value = len("Hello World")

#if value >5:
#    print(f"The lenght is {value}")

#if (value:= len("Hello World")) > 5:
#    print(f"The length is {value}")