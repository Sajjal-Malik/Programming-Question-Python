filename = input("Filename: ")
text = input("Text: ")

# Open the file with the provided filename for read access
with open(filename) as file:

    # Read all the contents of the file, store them into contents
    contents = file.read()

    # Count the occurrences of the string text in the file contents
    text_count = contents.count(text)

    # Output the occurrences of the string in the file
    print("Count:", text_count)