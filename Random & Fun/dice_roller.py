import random

print("Dice Roller")

while True:
    choice = input("\nPress Enter to roll or type q to quit: ")

    if choice.lower() == "q":
        break

    try:
        number_of_dice = int(input("How many dice? "))
        sides = int(input("How many sides per die? "))

        if number_of_dice <= 0 or sides <= 0:
            print("Please enter numbers greater than 0.")
            continue

        rolls = []

        for _ in range(number_of_dice):
            rolls.append(random.randint(1, sides))

        total = sum(rolls)

        print(f"\nRolls: {rolls}")
        print(f"Total: {total}")

    except ValueError:
        print("Please enter valid numbers.")