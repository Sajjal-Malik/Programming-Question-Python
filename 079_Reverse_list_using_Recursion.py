# Returns a reversed version of the list lst using recursion
def reverse(lst):
    if lst == []:
        return []
    return [lst.pop()] + reverse(lst)

# Test list
numbers = [5,6,7,8,9]

# Output the reversed list returned by the reverse() function
print(reverse(numbers))