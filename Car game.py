command=""
started=False
stopped=False
while True:
    command = input("The Asphalt>").lower()
    if command == "start":
        if started:
            print("The car has already started")
        else:
           started=True
           print("The car has started")
    if command== "stop":
        if stopped:
            print("The car has already stopped")
        else:
            stopped=True
            print("The car has stopped")
    if command == "help":
            print('''             <start-To start the car
                     >stop-To stop the car
                     >quit-To quit the game''')
    if command == "quit":
            break
else:
    print("Sorry I don't understand that")