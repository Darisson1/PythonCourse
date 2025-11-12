
HasHighIncome = True
HasGoodCredit = False
HasCriminalRecord = False

if HasHighIncome or HasGoodCredit:
    print("Eligible for loan 1")
    
if HasHighIncome and HasGoodCredit:
    print("Eligible for loan 2")

if HasHighIncome and not HasCriminalRecord:
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