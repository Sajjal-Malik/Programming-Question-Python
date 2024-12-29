def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:]) 
   

# Test the function with a list of numbers.  Recursion will look like this in
# this case...
#
# sum_list([4,1,3])
#   |
#   4 + sum_list([1,3])
#         |
#         1 + sum_list([3])
#               |
#               3 + sum_list([])
#                     |
#                     0
#
numbers = [4,1,3]
print( sum_list(numbers) )

# Test the function with the empty list
numbers = []
print( sum_list(numbers) )