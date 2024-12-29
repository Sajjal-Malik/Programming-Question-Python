# Returns the sum of the first n natural numbers using recursion
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)    

# Test the function
print(sum(5))

# We can visualize the series of function calls that will occur like this...
#
# sum(5) -> return 5 + sum(4)
# sum(4) -> return 4 + sum(3)
# sum(3) -> return 3 + sum(2)
# sum(2) -> return 2 + sum(1)
# sum(1) -> return 1             (special base case where recursion stops)

# We can then work backwards from the bottom to the top, replacing each
# function call with the relevant return value, and we see how the sum(5)
# will return 15...
#
# sum(5) -> return 5 + 10 -> return 15
# sum(4) -> return 4 + 6 -> return 10
# sum(3) -> return 3 + 3 -> return 6
# sum(2) -> return 2 + 1 -> return 3
# sum(1) -> return 1