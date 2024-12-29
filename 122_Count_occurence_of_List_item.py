def count(items_list,value):

    # The function works by looping through each item in the list and checking
    # to see if the item is equal to the value we're looking for it, if it is
    # we increment a running count (total) of the number of occurrences of 
    # that value.  By the the time the loop is done we'll have counted all the 
    # occurrences of the value and we return that count (total).
    total = 0
    for item in items_list:
        if item == value:
            total += 1
    return total


# A test list
items_list = [2,5,7,9,3,5,2,6,8,2]

# Test the function out, counting the occurrences of 2 in the list (3 total)
print( count(items_list, 2) )