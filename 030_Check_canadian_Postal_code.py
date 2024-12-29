def is_postal_code(code):

    if(len(code) != 7):
        return False

    if(not code[0].isalpha()):
        return False
    if(not code[1] in "0123456789"):
        return False
    if(not code[2].isalpha()):
        return False
    if(not code[3] != " "):
        return False
    if(not code[4] in "0123456789"):
        return False
    if(not code[5].isalpha()):
        return False
    if(not code[6] in "0123456789"):
        return False

    return True

codes = [
    "L4G 6H7",
    "4G 6HP",
    "P4G G6P",
    "P4G GP"
]

for code in codes:
  print(code, is_postal_code(code))
    