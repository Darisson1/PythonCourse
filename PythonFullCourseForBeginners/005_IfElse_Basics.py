

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
BuyerHasGoodCredit = True
DownPayment = 0

if BuyerHasGoodCredit:
    DownPayment = 10
else:
    DownPayment = 20

print(f"Down payment: ${price/100*DownPayment}")