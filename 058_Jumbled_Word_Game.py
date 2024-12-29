import random

words = ["python", "coding", "almost",
         "before", "attack", "chance"]

word = random.choice(words)

letters = list(word)
random.shuffle(letters)
jumbled_word = "".join(letters)

print("Unscramble...", jumbled_word)

while True:
    guess = input("Guess: ")
    if guess.lower() != word.lower():
        print("Incorrect try again!")
    else:
        break
