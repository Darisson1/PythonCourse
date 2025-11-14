
#bad example: same method. When you want to change the method, you have to change it at both classes
class Dog1:
    def walk(self):
        print("walk")
        
        
class Cat1:
    def walk(self):
        print("walk")
        

#better: one mammal class which inherits the method
class Mammal:
    def walk(self):
        print("walk")

        
class Dog(Mammal):
    def bark(self):
            print("bark")
        
class Cat(Mammal):
    pass #we need the pass, that the class is not empty

#so the dog got the additional method bark, which the cat does not. But both have the walk method, which got inherited from the mammal class
dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
