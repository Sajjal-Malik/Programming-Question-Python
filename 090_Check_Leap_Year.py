def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# Prompt the user to enter a year, convert the string entered into an int value
# and store it into year
year = int(input("Enter Year: "))

# Call the function to check if the year is a leap year, output appropriate 
# text accordingly
if is_leap_year(year):
    print(year, "is a leap year") 
else:
    print(year, "is not a leap year")

# for loop will run for year = 2020,2021,...,2040, and we output if each year
# in this range is a leap year or not
for year in range(2020,2041):
    if is_leap_year(year):
        print(year, "is a leap year") 
    else:
        print(year, "is not a leap year")