file = open("text.txt", "r")
try:
    content = file.read()
    print(content)
    file.close()
except:
    print("Error reading file ", file)