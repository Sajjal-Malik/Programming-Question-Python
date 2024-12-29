def is_rotation(s1, s2):
    if (len(s1) != len(s2)):
        return False
    
    temp = s1 + s2

    if s2 in temp:
        return True
    
    return False 

test1 = "python"
test2 = "thonpy"

print(is_rotation(test1, test2))

