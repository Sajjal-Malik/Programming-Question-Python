balance = 0
amount = 0
choice = ""

while True:
    print("1) Deposit: ")
    print("2) WithDraw: ")
    print("3) Print Balance: ")
    print("4) Quit Now!: ")

    choices = input("Enter your choice: ")

    choice = choices.strip()

    if (choice == "1"):
        amount = float(input("Enter amount: "))
        balance += amount
    elif (choice == "2"):
        amount = float(input("Enter amount: "))
        balance -= amount
    elif (choice == "3"):
        print("Balance is: ", balance)
    elif (choice == "4"):
        print(":/ to see you goo!")
        break
    else:
        print("Invalid choice, Please Try Again!")


