import random 

def dice_roll(dice, sides):
    if(dice <= 0):
        print("Must have atleast one dice!")
        quit()

    if(sides <= 0):
        print("Must have atleast one side!")
        quit()

    roll = []

    for i in range(0, dice):
        face = random.randint(1, sides)
        roll.append(face)

    return roll

dice = int(input("Dice: "))
sides = int(input("Sides: "))

roll = dice_roll(dice, sides)

print(roll)
