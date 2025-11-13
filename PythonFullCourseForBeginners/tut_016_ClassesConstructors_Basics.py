
#basic types
numbers = 5
strings ="string"
booleans = True

#"other types"
#= classes

#classes first letter upper case and separate words with upper case every word TestClassWithMoreWords
#we got a new type "Point" which is our blueprint:
class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")


#when we get an instance of these class, we create it as an object. So an object is an instance of a class
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
#print(point2.x) Error because not this POint object does not have an attribute x
point2.x = 123 #now it has
print(point2.x)
print("------------ Classes finished, now constructors")

#----------------------
#constructors are functions which are called when creating an object
#point = Point(10, 20) -> when create that point, we want to pass values for x and y 

class PointWithConstructor:
    #the init function gets called whenever we call a new object, so when we get a new instance of that class
    #so this method is called the constructor, its used to construct or create an object
    def __init__(self, x, y): #the self is a reference to the current object. 
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")

        

        
#!Test Warning
#TODO Test Todo
#? makes sense

point = PointWithConstructor(10, 20)
point.x = 12 #can be modified of course
print(point.x)
