def is_pallindrom(string):
    length = len(string)
    for i in range(0, length // 2):
        if (string[i] != string[length - i - 1]):
            return False
    return True

string1 = "racecar"
string2 = "moon"
string3 = "abcdcba"

if(is_pallindrom(string3)):
    print("Given string is Pallindrome")
else:
    print("Given string is not Pallindrome")