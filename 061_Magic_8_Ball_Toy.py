import random 

# A list of all the official Magic 8 Ball answers
answers = ["It is certain.",
           "It is decidedly so.",
           "Without a doubt.",
           "Yes definitely.",
           "You may rely on it.",
           "As I see it, yes.",
           "Most likely.",
           "Outlook good.",
           "Yes.",
           "Signs point to yes.",
           "Reply hazy, try again.",
           "Ask again later.",
           "Better not tell you now.",
           "Cannot predict now.",
           "Concentrate and ask again.",
           "Don't count on it.",
           "My reply is no.",
           "My sources say no.",
           "Outlook not so good.",
           "Very doubtful."]

# Will be set to True when the user wants to quit asking questions
quit = False 

# The loop will run indefinitely until the user enters 'quit' and the quit
# variable is set to True (at which point not True --> False)
while not quit:
    
    # Prompt the user to enter their question
    question = input("Yes/No Question (quit to Quit):\n")
    
    # If the user enters 'quit' stop the game by setting quit to True.
    if (question == "quit"):
        quit = True 
    # Otherwise we use the choice function of the random module to select an 
    # answer from the list of answers randomly... the function will return one
    # of the list items randomly and we'll output that answer string along with
    # some text and newlines (\n) for spacing
    else:
        print("\nAnswer:", random.choice(answers), "\n")