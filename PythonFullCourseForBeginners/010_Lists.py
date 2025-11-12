#Test Commit
#Test Commit from VsCode extension
import random

names = ["John", "Bob", "Mosh", "Sarah","Mary"]
largestNumber = 0
actualNumber = 0
print(names[-1])
print(names[2])
print(names[2:4])

print(names)

names[0] = "Johnny"
print(names)

listOfNumbers = []
listOfNumbers.clear
for n in range(100):
    listOfNumbers.append(random.randrange(1,1000))
    
for actualNumber in listOfNumbers:
    #print(f"Actual Number:  {actualNumber}")
    if actualNumber > largestNumber:
        largestNumber = actualNumber
        
print(f"largestNumber is: {largestNumber}")

print(f"Now printing real list: {listOfNumbers}")



print("-----------------")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
        
        
numbers = [5, 2, 1, 7, 4]
numbers.append(14)

print(numbers)

numbers.insert(0, 10) #insert 10 at position 0

print(numbers)

numbers.remove(5) #remove the number 5

numbers.clear() #clear all items in list

print(numbers)

numbers = [5, 2, 1, 7, 4, 5, 10]

numbers.pop() #remove last item in the list

print(numbers)

#numbers.remove(51) #remove the number 51 --> gives an error because there is no 51 in the list

print(numbers.index(1)) #gives the index of our number. 1 is on pos 2
#numbers.remove(51) #gives the index of our number. error because 51 not in the list

print(51 in numbers) #checks if number is in list. Boolean

print(numbers.count(5)) #counts, how often the 5 is in the list --> 2

numbers.sort() #sorts list in ascending order (small to big)
print(numbers)
numbers.reverse() #reverses list, in this case big to small
print(numbers)

numbers2 = numbers.copy() #copies the list
numbers.append(123) #append FIRST list
print(numbers2) #print SECOND list, so without 
print(numbers) #print list with the 123
