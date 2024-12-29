integer = int(input("Integer: "))

for i in range(1, integer + 1):
    if (integer % i == 0):
        print(i)