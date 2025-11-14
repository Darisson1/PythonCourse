
from tut_018_utils import find_max
import random

random_numbers = []

for num in range(10):
    random_numbers.append(random.randrange(100))

print(find_max(random_numbers))
print(max(random_numbers)) #built in function max