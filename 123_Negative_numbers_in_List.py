numbers_list = [5,-67,0,45,-23,-82,95] 

# The for loop body will run for each number in the list from 5 to 95.  Each
# time it runs 'number' will be set to the next number in the list.  We check 
# if the number is less than 0 (i.e. if it is negative) using an if-statement
# and only output the number if it is negative.
for number in numbers_list:
    if number > 0:
        print(number)