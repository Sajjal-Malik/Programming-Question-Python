def delete_line(filename, line_number):
    with open(filename) as file:
        lines = file.readlines()
    if (line_number < len(lines)):
        del lines[line_number - 1]
        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
    else:
        print("Line: ", line_number, " not in file")
        print("File has ", len(lines), " lines")




delete_filename = input("File: ")
delete_line_number = int(input("Line number: "))

delete_line(delete_filename, delete_line_number)