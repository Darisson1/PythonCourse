
has_high_income = True
has_good_credit = False
has_criminial_record = False

if has_high_income or has_good_credit:
    print("Eligible for loan 1")
    
if has_high_income and has_good_credit:
    print("Eligible for loan 2")

if has_high_income and not has_criminial_record:
    print("Eligible for loan 3")
    
temperature = 30

if temperature >= 30:
    print("its a hot day")
else:
    print("Its not a hot day")
    
    
    
name = input("Write your name: ")

if len(name) < 3:
    print("name must be at least 3 characters long")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good")