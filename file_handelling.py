# we do 3 work on files:
#reading data
#writing data    کلا دیتا رو پاک میکنه و از اول مینویسه
#Appending data    مدل دیگه قبلی هست با این تفاوت که اینجا دیتا ی قبلی رو نگه میداره وبهش یه چزی اضافه میکنه

#read()  ,readline() , readllines()
#file_object = open("./my_data.txt", "r")
#print(file_object)
#print(file_object.name)
#print(file_object.mode)
#print(file_object.read())
#content = file_object.read()    # with read method we can read whole content of file
#content = file_object.readline()  #برای خواندن خط به خط  که با هربار نوشتن و اجرا یک خط میخونه 
#content = file_object.readline()  #اجرای مجدد برای خواندن خط دوم
#content = file_object.readlines()   #هر خط فایل رو به صورت  یک آیتم از لیست نشون میده
#print(content)
#for index,line in enumerate(content, 1):
#    print(f"{index}.{line}")


#file_object = open("./my_data.txt", "r")
#content = file_object.readlines()

#for index,line in enumerate(content, 1):
#    line = line.replace('\n','')
#    print(f"{index}.{line}")

#file_object.close()    #حتما وقتی یک فایل رو باز می کنید اون رو بعدش ببندید


#write() , writelines()
#file_object = open("./new_data.txt" , "w")
#file_object.write("This is my first line of writing content to a file\n\n\n")
#lines =(
#    "This is the first line\n",
#    "This is the second line\n",
#    "This is the third line\n"
#)
#file_object.writelines(lines)

#file_object.close()


#file_object = open("./new_data.txt",'a')

#file_object.write("This content is being appended")
#file_object.writelines(['penultimate\n','ultimate line\n'])

#file_object.close()


# آدرس دهی به دوصورت مطلق و نسبی انجام میشه /مطلق از ریشه ای ترین شروع میکنه/نسبی از جایی که بهش بدیم

#import os

#print(os.getcwd())    #absolut address  این نوع آدرس دهی مطمئن تره
#print(os.path.abspath("."))
#print(os.path.abspath("../"))
#print(os.path.abspath("../../"))


#file_object = open("./textual_data/my_data.txt", "r")     #related addressing 
#file_name = "/users/sadra.co/documents/irst.py/textual_data/my_data.txt"
#file_object = open(file_name,"r")
#content = file_object.readlines()

#for index,line in enumerate(content, 1):
#    line = line.replace('\n','')
#    print(f"{index}.{line}")

#file_object.close()


#import os
#print(os.path.basename("/users/sadra.co/documents/irst.py/textual_data/my_data.txt"))




#   فایل ها جیسان دیتا ها در اون به صورت object-value ذخیره می شوند
#و درتبادل اطلاعات بین نرم افزارها و دیوایس ها کاربرد دارند چون خیلی سبک هستند و تحلیل دیتا در آن راحت تر هست
#file_object = open("my_data.json","r")

#content = file_object.read()
#print(content)

#file_object.close()

#  روشی برای اینکه با این فایل جیسون مثل دیکشنری رفتار بشه

import json

#file_object = open("my_data.json","r")
#content = file_object.read()
#json_content = json.loads(content)
#print(json_content)
#print(json_content['first_name'])
#print(json_content['courses'])
#print(json_content['courses'][1])
#file_object.close()

#file_object =open("./textual_data/new_json_value.json","w")

#data = {
#    "full_name" : "Alireza Mortezae",
#    "email": "alirezamortezae50@gmail.com",
#    "is_student": True,
#    "level":"Silver"
#}
#json_content = json.dumps(data)
#print(json_content)
#file_object.write(json_content)

#file_object.close()


#file_object = open("my_data.json" , "r")

#content= file_object.read()
#json_content = json.loads(content)

#json_content["first_name"] = json_content["first_name"] .upper()
#json_content["last_name"] = json_content["last_name"] .upper()
#file_object.close()

#file_object = open("my_data.json",'w')

#content=json.dumps(json_content)
#file_object.write(content)

#file_object.close()

#comma seprated value (csv)
import csv

#file_object = open("data.csv","r")

#reader = csv.reader(file_object)
#for data in reader:
#    print(data)

#file_object.close()

#file_object = open("data.csv","r")

#reader = csv.DictReader(file_object)
#for data in reader:
#    print(data['first_name'])

#file_object.close()

#import csv

#file_object = open("./new_csv_data.csv", "w")

#field_name = ["first_name","last_name","age"]
#writer = csv.DictWriter(file_object,fieldnames=field_name)
#writer.writeheader()
#writer.writerow({"first_name":"Alireza","last_name":"Mortezae","age":23})
#writer.writerow({"first_name":"David","last_name":"Doe","age":45})

#file_object.close()

#import shutil     # modul for copy/paste

#shutil.copy("./new_csv_data.csv", "./textual_data/new_2.csv")
#shutil.move("./my_data.json","./textual_data/new_2.json")

#import os
#os.remove("new_csv_data.csv")

# way of contex manager

#file_object =open("./new_csv_data.csv","w")
import json
with open("./textual_data/new_json_value.json","r") as file_object:
    content=file_object.read()
    json_content = json.loads(content)
    print(json_content)

print(file_object.closed)   # باعث میشه بعد از استفاده از فایل دسترسی به ریسورس فایل بسته بشه