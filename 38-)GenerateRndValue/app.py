import random
'''
for i in range(3):
    print(random.randint(10, 20))
'''

members = ["Jhon", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        rollnums = (random.randint(1,6), random.randint(1, 6))
        return rollnums


dice1 = Dice()
print(dice1.roll())
