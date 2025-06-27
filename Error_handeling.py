#while True:
#    try:
#        number = int(input("Enter a number:"))
#    except:
#        print("An error occured")  
#        continue
#    break 

#for _ in range(number):
#    print("Hello World")


#number_of_tries = 3
#is_allowed = False

#while number_of_tries > 0:
#    try:
#        number = int(input("Enter a number:"))
#    except:
#        print("An error occured") 
#        number_of_tries -= 1
#        continue
#    is_allowed = True    # زمانیکه کاربر دیتا درست بده که در اینجا عدد هست
#    break 


#if is_allowed:
#    for _in range(number):
#        print("Hello World")        
#else:
#    print("You have missed your chance")  



#try:
#    number = int(input("Enter a number:"))
#    result = 10 / number
#except ValueError:
#    print("An error ocured")   
#except ZeroDivisionError:
#    print("zeroDivisionError occured")    



#try:
#    number = int(input("Enter a number:"))
#    result = 10 /number
#except Exception as error_messsage:
#    print("This error is:",str(error_messsage))  

#print("Done")      



#try:
#    number = int(input("Enter a number:"))   # بلاکی که باید باشه و کد مد نظرمون در اون هست
#    result = 10 /number
#except Exception as error_messsage:
#    print("This error is:",str(error_messsage))    # به ارور بخوره اجرا میشه
#else:
#    print("No error found")     #به ارور نخوره اجرا میشه
#finally: 
#    print("I am here anyway")      #چه ارور بخوره چه نخوره  این خط اجرا میشه




#number_of_tries = 3
#is_allowed = False

#while number_of_tries > 0:
#    try:
#        number = int(input("Enter a number:"))
#    except:
#        print("An error occured") 
#        number_of_tries -= 1
#        continue
#    else:
#        is_allowed = True    # زمانیکه کاربر دیتا درست بده که در اینجا عدد هست
#        break 


#if is_allowed:
#    for _ in range(number):
#        print("Hello World")        
#else:
#    print("You have missed your chance")


#number = int(input("Enter a number:"))

#if number % 10 ==0:
#    raise ValueError("Input value must not be a coefficient of 10")

#print("A valid input")



#class TenCoefficientError(Exception):
#    def __init__(self,message, *args,**kwargs):
#        super().__init__(message,*args,**kwargs)

#number = int(input("Enter a number:"))   
#if number % 10 == 0:
#    raise TenCoefficientError("Invalid input",number)     