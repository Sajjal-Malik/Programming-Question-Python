def count_vowels(text):
    count = 0
    for char in text:
        if char in "AEIOUaeiou":
            count += 1
    return count

text = input("Enter any text: ")

count = count_vowels(text)

print("Vowels in the above string are: ", count)

