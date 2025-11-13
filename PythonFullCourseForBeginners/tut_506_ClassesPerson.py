
class Person:
    
    def __init__(self, name):
        self.name = name #name attrribute of current object to the argument passed to the method
        
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()