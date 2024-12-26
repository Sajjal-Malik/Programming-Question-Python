def count_lowercase(text):
    count = 0
    for character in text:
        if (character.islower()):
            count += 1

    return count


text = input("Enter the text: ")

count = count_lowercase(text)

print("Lower case chars in the given string are: ", count)