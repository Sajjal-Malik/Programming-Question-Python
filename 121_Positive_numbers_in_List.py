numbers_list = [-45,0,67,78,33,-45,82] 

# The for loop body will run for each number in the list from -45 to 82.  Each
# time it runs 'number' will be set to the next number in the list.  We check 
# if the number is greater than 0 (i.e. if it is positive) using an if-statement
# and only output the number if it is positive.
for number in numbers_list:
    if number > 0:
        print(number)