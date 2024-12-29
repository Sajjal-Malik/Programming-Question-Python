import random

def lotter_num_generator(s, e, amount):
    if(amount <= 0):
        print("Amount must be positive!")
        quit()
    
    if(end - start + 1 < amount):
        print("Amount chosen can't exceed available numbers!")
        quit()
    
    numbers = random.sample(range(start, end+1), amount)
    return numbers


start = int(input("Start: "))
end = int(input("End: "))
amount = int(input("Amount: "))

result = lotter_num_generator(start, end, amount)
print(result)