
carState = ""

while True:
    command_user = input(">").lower() #direkt alles was eingegeben wird klein
    if command_user == "help":
        print("""
start - to start the car
stop - to stop the car
exit - to exit
        """)
    elif command_user == "start":
        if carState == "started":
            print("Car already started")
        else:
            carState = "started"
            print("Car started...Ready to go")
    elif command_user == "stop":
        if carState == "stopped":
            print("Car already stopped")
        else:
            carState = "stopped"
            print("Car stopped")
    elif command_user == "exit":
        print("Exit game...")
        break
    else:
        print("I dont understand")