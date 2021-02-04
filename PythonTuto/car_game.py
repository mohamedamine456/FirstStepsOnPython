started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print("Start - to start the car")
        print("Stop - to stop the car")
        print("Quit - to exit")
    elif command == "start":
        if not started:
            print("Car Started...Ready To Go!")
            started = True
        else:
            print("Car Already Started")
    elif command == "stop":
        if started:
            print("Car Stopped.")
            started = False
        else:
            print("Car Already Stopped")
    elif command == "quit":
        break
    else:
        print("I don't Understand that...")