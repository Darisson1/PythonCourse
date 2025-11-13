

is_hot = False
is_cold = False

if is_hot and not is_cold:
    print("It's a hot day")
    print("Drink Water")
elif is_cold and not is_hot:
    print("It's a cold day")
    print("Wear a jacket")
else:
    print("It's a lovely day")
print("Enjoy your day")

price = 1_000_000
buyer_has_good_credit = True
down_payment = 0

if buyer_has_good_credit:
    down_payment = 10
else:
    down_payment = 20

print(f"Down payment: ${price/100*down_payment}")