command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("car started.....")
    elif command == "stop":
        if not started:
            print("Car is already stopped..!")
        else:
            started = False
            print("Car stopped..!")
    elif command == "help":
        print('''
start - start the car
stop - stop the car
quit - quit the game''')
    elif command == "quit":
        break
    else:
        print("Sorry, I didn't understand...!")