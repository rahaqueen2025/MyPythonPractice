person={
    "first_name":"john",
    "last_name":"Doe",
    "email":"john@gmail.com",
    "age":25,
    "adress":{
         "city":"san francisco",
         "stree":"1st street",
         "floor":"2nd floor",
    }
 }

#print(type(person))
#print(person['adress'])
#print(person['adress']['city'])
#print(person)
#print(person.keys())
#print(person.values())
#print(list(person.values())[-1])
#print(person.items())
#print(list(person.items()))
#print(list(person.items())[2][1])
#print(person.get("full_name"))
#print(person.get("first_name"))
#print(person.get("full_name","No name"))
#print(person.pop("first_name"))
#print(person)
#person.update({"gender":"male"})

person.clear()
print(person)