#regular expression            عبارت های منظم
#تو به من یک الگو بده من اون رو از متن یا فایلی که بگی درمیارم مثل بیرون کشیدن تعدادی شماره تلفن که در یک متن هست
#  کاربرد دیگه اش در data validation هست یعنی مثلا طبق الگویی که دادیم بررسی کن این ایمیل الگوی درستی داره یا نه
# www.regex101    
#یادگیری رجکس یعنی یادگییری الگوها

#import re

#pattern = r"\w+@\w+.com"
#text = "This is the email adress alirezamortezaei50@gmail.com."
#result =re.search(pattern,text)
#print(result.span())     #میگه متنی که پیدا کردم از کجا تا کجا ادامه داره
#result = re.search(pattern,text)   در کل جمله دنبالش میگرده
#if result:
#    print("Email found")
#else:
#    print("No result found")    


#pattern = r"\w+@\w+.com"
#text = "alirezamortezaei50@gmail.com.This is the email adress "

#result =re.match(pattern,text)   #اول جمله دنبالش میگرده
#print(result)

#result = re.findall(pattern,text)   هرچندتا ایمیل توی متن باشه پیدا میکنه#
#print(result)

#result = re.sub(pattern,"EMAIL",text)   # برای جایگزین کردن عبارت دلخواه جای الگوی قبل
#print(result)


import re

class Email :
    def __init__(self,email):
        self.email =email
        self.is_valid = self.validate_email()
        
    def validate_email(self):
        pattern = r"^\w+@\w+.com$"
        return bool(re.search(Pattern , self.email)) 
    
    def __str__(self):
        return f"{self.email} validation is {self.is_valid}"

email =input("Enter your email:") 
first_email =Email(email)
print(first_email)    