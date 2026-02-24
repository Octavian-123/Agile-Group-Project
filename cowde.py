

def opt1():
    print("\nThis is option 1")

def opt2():
    print("\nThis is option 2")

def opt3():
    print("\nThis is option 3")

def readLogins():
    with open("logins.txt", "r") as f:
        contents = f.readlines()

        newContents = []

        for line in contents:
            fields = line.split(",")
            fields[0] = fields[0].strip()
            fields[1] = fields[1].strip()
            newContents.append(fields)

        return(newContents)

def login(logins):
    while True:
        askUsername = str(input("Input username: "))
        askPassword = str(input("Input password: "))

        for line in logins:
            if line[0] == askUsername and line[1] == askPassword:
                print("Logged in successfully")
                return True

        print("Login failed")

options = {
    1: opt1,
    2: opt2,
    3: opt3
}

logins = readLogins()

if login(logins):
    
    while True:
        try:
            menuSelect = int(input(
                "\nOpt 1 - Press 1"
                "\nOpt 2 - Press 2"
                "\nOpt 3 - Press 3"
                "\nStop - Press 4\n\n"
            ).strip())

            if menuSelect == 4:
               print("\nProgram stopped.")
               break
            elif menuSelect in options:
                options[menuSelect]()
            else:
                print("\nInvalid number")

        except ValueError:
            print("\nPlease input a number (1-4)... try again")
