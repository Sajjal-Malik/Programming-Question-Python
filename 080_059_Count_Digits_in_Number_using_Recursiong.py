def count_digits(number):
    if number // 10 == 0:
        return 1
    return 1 + count_digits(number // 10)

print(count_digits(1279))

