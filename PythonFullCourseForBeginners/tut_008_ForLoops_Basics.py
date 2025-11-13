
for item in "Python":
    print(item)
    
for item in["Mosh", "John", "Sarah"]:
    print(item)
    
for item in[1,2,3,4,5,6]:
    print(item)
    
print("-----")
    
for item in range(10):
    print(item)
    
print("-----")
    
for item in range(5,10):
    print(item)
    
print("-----")

for item in range(1,20,2):
    print(item)
    
print("-----")

prices = [10, 20, 30]
total_cost = 0
for price in prices:
    total_cost =+ total_cost+price
print(f"total price is {total_cost}")