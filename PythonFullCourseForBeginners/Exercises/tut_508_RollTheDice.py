import random


class Dice:
    def roll(self):
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        # return (num1, num2) without the parenthesis,
        # it automaticalley gets created as a tuple
        return num1, num2

    def hans(self):
        return

    def okay(self):
        return


dice = Dice()
print(dice.roll())
