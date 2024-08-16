import random
import os

selectedNum = random.randrange(0,100,1)
os.system('cls')
print(f"Welcome Number Guessing Game!\nHere is the rules\n1-) 50 Guess change between 0 to 100\n2-) If you loose the game you loose nothing except 'C:' drive (just joke... maybe not)\nLets Begin folks!")
hearth = 50

while hearth > 0:
    userNum = input(f"Remaining hearth : {hearth}\nwhats your number : ")
    os.system('cls')
    if int(userNum) > selectedNum:
        hearth -= 1
        print(f"Your number ({userNum}) higher, try again")
    elif int(userNum) < selectedNum:
        hearth -= 1
        print(f"Your number ({userNum}) lower, try again")
    elif int(userNum) == selectedNum:
        print("Conguralitons, you Won Game\nYour driver is safe now :)")
        break
if(hearth <= 0):
    print("You lost the game and driver... upss")

'''
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit
    guess = int(input('Guess: '))
    guess_counr ^= 1
    if guess == secret_number:
    print('You Won!')
    break
else:
print('Sorry, you failed!')
'''