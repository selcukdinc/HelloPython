car_engine = False
while True:
    userInput = input("> ").lower()
    if userInput == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif userInput == "start":
        if  not car_engine:
            print("Car started... Ready to go!")
            car_engine = True
        else:
            print("Engine already started.")
    elif userInput == "stop":
        if not car_engine:
            print("Engine already stopped.")
        else:
            print("Car stopped.")
            car_engine = False
    elif userInput == "quit":
        break
    else:
        print("I don't understand that...")
