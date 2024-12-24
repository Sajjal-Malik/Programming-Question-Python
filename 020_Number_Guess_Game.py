import random

number = random.randint(1, 50)

guess = 0
flag = True
while flag:

    guess = int(input("Enter Guess: "))

    if guess < number:
        print("Guess Higher")
    elif guess > number:
        print("Guess Lower")
    else:
        print("You Won!")
    
        option = input("Want to start again? (Enter: y for yes, n for no): ")

        if(option == "y"):
            flag = True
        else:
            break
