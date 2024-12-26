def count_uppercase(text):
    count = 0
    for character in text:
        if character.isupper():
            count += 1

    return count


text = input("Enter the text: ")

count = count_uppercase(text)

print("Upper case chars in the given string are: ", count)