def check_prime(number):
    is_prime = True

    if number > 1:
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break
        return is_prime
    else:
        return False

number = int(input("Enter Number: "))

if check_prime(number):
    print("Number is prime")
else:
    print("Number is not prime")
