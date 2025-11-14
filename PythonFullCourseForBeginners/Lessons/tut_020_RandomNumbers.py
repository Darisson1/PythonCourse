
# https://docs.python.org/3/py-modindex.html

import random


for i in range(3):
    print(random.random())
    print(random.randint(10, 20))
    
members = ['John', 'Mary', 'Bob', 'Mosh']
print(f"the leader is: {random.choice(members)}")

