
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome here")
    
def square(number):
    return number*number
    
def square2(number):
    number*number #no return -> ALL functions return None, when no return in Function is defined/used
    

print("Start")
greet_user(last_name="Smith", first_name="John")
greet_user("Mary", "Smith")
print("Finished")

result = square(9)
print(result)

print(square(5)) #25

print(square2(5)) #None