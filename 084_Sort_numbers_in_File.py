filename = input("Filename: ")

with open(filename) as file:
    lines = file.readlines()

numbers = [float(x) for x in lines]

numbers.sort()
# numbers.sort(reverse=True)

print(numbers)

new_lins = [str(x) + "\n" for x in numbers]

print(new_lins)

with open(filename, "w") as file:
    file.write(new_lins)
