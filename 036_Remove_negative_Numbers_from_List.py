
nums = [2,4,6,-1,-4,-6,-8,9,11,10]

filtered = []

for num in nums:
    if num >= 0:
        filtered.append(num)

print(filtered)


def check_number(number):
    return number >= 0

built_in_filtered = list(filter(check_number, nums))

print(built_in_filtered)



in_line_built_in_filtered = list(filter(lambda n: n >= 0, nums))

print(in_line_built_in_filtered)




comprehensive_filtered = [item for item in nums if item >= 0]

print(comprehensive_filtered)