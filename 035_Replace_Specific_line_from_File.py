def replace_line(filename, line_number, text):
    with open(filename) as file:
        lines = file.readlines()

    if (line_number <= len(lines)):
        lines[line_number - 1] = text + "\n"
        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
    else:
        print("Line: ", line_number, " not in file")
        print("File has ", len(lines), " lines")


filename = input("File: ")
line_number = int(input("Line number: "))
text = input("Text: ")

replace_line(filename, line_number, text)