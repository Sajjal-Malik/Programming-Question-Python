import numpy

def list_multiply(numbers):
    product = 1

    for number in numbers:
        product = product * number
    
    return product

list1 = [1, 2, 3, 4, 5, 6]

print(list_multiply(list1)) # iterative approach

print(numpy.prod(list1)) # numpy.product() method