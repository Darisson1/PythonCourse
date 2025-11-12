
#tuples are like lists. but you cant modify them. Get only info from them.
#so you see only tuple.count and tuple.index, not eg tuple.append or sth
numbers = (1, 2, 3, 4, 2, 2)
print(numbers[0]) #get first item

#numbers[0] = 123 #error
print(numbers.count(2)) #3 x 2 in tuple
print(numbers.index(2)) #first time at position 2




coordinates = (1, 2, 3)
coordinatesList = [1, 2, 3]

#not the nicest way:
print(coordinates[0] * coordinates[1] * coordinates[2])

#better:
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x*y*z)

#but even better to use "unpacking":
"""
which does the same as 
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
"""
x, y, z = coordinates
print(x)
print(y)
print(z)
print(x*y*z)

#works with lists:
x, y, z = coordinatesList
print(x)
print(y)
print(z)
print(x*y*z)
