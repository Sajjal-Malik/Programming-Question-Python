number = float(input("Enter Number: "))

# The first branch of the if-elif-else statement checks if the number is 
# negative by checking if it is less than zero, if it is, we output the 
# number is negative using print().  If this condition is not true the condition
# of the elif branch will be checked next, and we check if the number is 
# positive by checking if it is greater than zero.  If it is, we output that 
# the number is positive using print(), if it is not the only possibility left
# is that the number is zero.  The code in the else branch will execute if 
# the elif condition is false, and so we output the number is zero.  Note that 
# the code for each branch is indented, this makes the code a "block" that 
# will execute for the associated branch.
if number < 0:
    print("Number is negative")
elif number > 0:
    print("Number is positive")
else:
    print("Number is zero")