
weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
print(unit)
if unit.upper() == "L":
    print(f"You are {float(weight)*0.45} kg")
elif unit.upper() == "K":
    print(f"You are {float(weight)/0.45} lbs")
else:
    print("---")