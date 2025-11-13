
try:
    age = int(input("age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError: #divide by 0
    print("Age cant be zero")
except ValueError: #convert non numeric in integer
    print("Invalid Value")