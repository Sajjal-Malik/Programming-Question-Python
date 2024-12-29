def count(lst, value):
    if not lst:
        return 0
    elif lst[0] == value:
        return 1 + count(lst[1:], value)
    else:
        return count(lst[1:], value)


# Test the function with a list of numbers, count the occurrences of 4 (2).
#
numbers = [4,1,4,2]
print( count(numbers, 4) )