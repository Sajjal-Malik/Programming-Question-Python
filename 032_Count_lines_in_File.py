def count_file_lines(filename):
    with open(filename) as file:
        lines = file.readlines()
        total_lines = len(lines)
        return total_lines

count = count_file_lines("text.txt")

print("Total lines: %d" % count)