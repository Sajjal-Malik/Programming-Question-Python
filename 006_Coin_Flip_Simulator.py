import random

def flip_coint():
    return random.choice(["Heads", "Tails"])

# print(flip_coint())

# for i in range(10):
#     print("Flip " + str(i+1) + ": " + flip_coint())

flips = int(input("Flips: "))
total_heads = 0
total_tails = 0

for i in range(flips):
    if flip_coint() == "Heads":
        total_heads += 1
    else:
        total_tails += 1

print("Total Heads: " + str(total_heads) + " Tailheads: " + str(total_tails))