def is_prime(number, divisor = 2):
    if divisor == number:
        return True 

    if number % divisor == 0:
        return False
    return is_prime(number, divisor + 1)

print(is_prime(13))