def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n-2) + fib(n-1)


#              fib(3)
#            /      \
#       fib(2)     fib(1)
#      /     \
#  fib(1)    fib(0)
#
#  The above function will result in a "tree" of recursive function calls as 
#  calculating terms n-2 and n-1 may involve further recursive calls, as 
#  calculating fib(2) does in the case of finding fib(3).
#
#  Because there are two recursive function calls we can call this an example 
#  of binary recursion, multiple recursion and/or tree recursion.

# Test out the function by trying to calculate term 8
print(fib(8))

# Try to output the first 16 terms in the sequence
for n in range(0,16):
    print(fib(n))