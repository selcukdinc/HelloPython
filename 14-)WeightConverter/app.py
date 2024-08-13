onePound = 0.45359237
userWeight = input("Weight : ")
userChoice = input("(L)bl or (K)g :")
userChoice = userChoice. upper()
if userChoice == "L":
    print(f'You are {int(float(userWeight) * onePound)} kilograms')
elif userChoice == "K":
    print(f'You are {int(float(userWeight)  / onePound)} pounds')
else:
    print("Wrong selection, try again")