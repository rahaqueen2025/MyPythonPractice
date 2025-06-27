#number=0
#THRESHOLD=10
#while number<THRESHOLD:
#    print("Hello world")
#بدترین حلقه هست چون متوقف نمیشه و برای توقف ctrl+c می زنیم 

#while True:
#    print("Hello world")
#    number+=2
#    if number>THRESHOLD:
#        break
    

#while True:
#    print("Hello world")
#    number+=1
#    if  not number % 2:
#        continue
#    print(f"Number is :{number}")
#    if number>THRESHOLD:
#        break

#BASE_NUMBER=32
#while True:
#    user_input=int(input("enter anumber:"))
#    if user_input==BASE_NUMBER:
#        print("congrats")
#        break
#    elif user_input>BASE_NUMBER:
#        print("please enter a smaller value:")
#    else:    
#        print("please enter a larger value:")

#for index in range(10):
#    print(f"value of index is:{index}")
       
#for index in range(10,50,2):
#    print(f"value of index is:{index}")

#     استفاده از str برای مقداردهی به index
#for index in "Hello World":                                        
#    print(f"value of index is:{index}")

#              استفاده از list برای مقدار دهی به index  
#for index in ["hello","world","True",["value"]]:
#    print(f"vale of index is:{index}") 

#for index in {"first_name":"john","last_name":"Doe"}.items():
#    print(f"value of index is:{index}")

#for key,value in {"first_name":"john","last_name":"Doe"}.items():
#    print(f"key is:{key} and value is :{value}")

#for index,value in enumerate(["one","two","three"]):
#    print(f"The index of {value} is {index}")

#in line for loop    متد دیگه برای حلقه for
#value=[index for index in range(10)]
#print(value)

#value=[index*2 for index in range(10)]
#print(value)

#value=[index**2 for index in range(10)]
#print(value)

#for item in ["Hello","world","This","is","python","cause"]:
#    print("starting of nested loop")
#    for char in item:
#        print(char,end='-')

#numbers=[]
#while True:
#    user_input=int(input("enter a number:"))
#    if user_input==-1:
#        break
#    numbers.append(user_input)

#total_value=0
#for value in numbers:
#    total_value +=value
#    print(f"total value is:{total_value}") 
    
#user_input=int(input("enter a number:"))
#is_prime=True
#for number in range(2,int(user_input**0.5) +1):
#    if not user_input%number:
#    if is_prime:
#        print("your number is prime")
#    else:
#        print("your number is not prime")
    
    
