def read_specific_line(file_name, line_number):
    try:
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()
    except:
        print("Error reading the File")
        return

    total_lines = len(lines)
    if(line_number > total_lines):
        print(str(total_lines) + " lines in the file")
        print("Can't read line " + str(line_number) + "!")
    else:
        line = lines[line_number - 1].rstrip('\n')
        print(line)


file_name = input("File: ")
line_number = int(input("Line: "))
read_specific_line(file_name, line_number)