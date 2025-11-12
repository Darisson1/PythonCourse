import random

numbers = []

for x in range(20):
    numbers.append(random.randrange(1,50)) #fill the list with random numbers
    
print(f"print original list: {numbers}")

for number in numbers:
    counts = numbers.count(number)
    if counts >= 2:
        print(f"multiplied number found: {number}")
        numbers.remove(number)
                    
print(f"modified list: {numbers}")
#removes ALL doubles. but doesnt keep the first.
#better:


numbers = []
uniqueNumbers =[]
for x in range(20):
    numbers.append(random.randrange(1,50)) #fill the list with random numbers
print(f"print original list: {numbers}")

for number in numbers:
    if number not in uniqueNumbers:
        uniqueNumbers.append(number)
    else:
        print(f"multiplied number found: {number}")
        
print(f"modified list: {uniqueNumbers}")