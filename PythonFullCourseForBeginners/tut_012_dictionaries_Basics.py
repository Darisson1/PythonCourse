
#dictionary for key value pairs

customer = {
    "name": "John Smith",
    "age": 30,
    "isVerified" : True    
}

print(customer["name"])
#print(customer["Name"]) gives an error because we have no "Name" with a capital N --> casesensitive

print(customer.get("name")) #same as print(customer["name"]) but no problem when
print(customer.get("BirthDate")) #the key is not in the dictionary. returns None

print(customer.get("BirthDate", "01.01.2000")) #but you can define a default instead of None


customer["name"] = "Jack Smith" #change values from keys
print(customer.get("name"))

customer["BirthDate"] = "05.05.2002" #new key value pair in the dictionary
print(customer.get("BirthDate"))


