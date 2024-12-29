def digit_counter(number):

    number = abs(number)
    count = 0

    while number != 0:
        number //= 10
        count += 1

    return count 

print("Digit Total:", digit_counter(-123))