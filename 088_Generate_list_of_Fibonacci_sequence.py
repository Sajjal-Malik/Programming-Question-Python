# Returns a list containing the first n numbers of the Fibonacci sequence
def create_fib_sequence(n):

    # n <= 0 does not make sense, we can return None for this (or [])
    if n <= 0:
        return None
    # Return a list containing the first number of the Fibonacci sequence
    elif n == 1:
        return [0]
    else:
        # Begin with a list of the 2 Fibonacci sequence numbers
        fibs = [0,1]

        # This loop will execute n-2 times, and each time we append the next 
        # number in the Fibonacci sequence by summing the LAST two Fibonacci 
        # sequence numbers in the list.
        for i in range(2,n): 
            fibs.append( fibs[-1] + fibs[-2] )

        # Return the generated list
        return fibs

# Output the list containing the first 10 Fibonacci numbers
print( create_fib_sequence(10) )