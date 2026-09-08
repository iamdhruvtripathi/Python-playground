import random

heads = 0
tails = 0
flips = 0

print("Coin Flip Simulator")

while True:
    choice = input("\nPress Enter to flip or type q to quit: ")

    if choice.lower() == "q":
        break

    result = random.choice(["Heads", "Tails"])
    flips += 1

    print(f"\n{result}!")

    if result == "Heads":
        heads += 1
    else:
        tails += 1

print("\n--- Results ---")

if flips == 0:
    print("No flips were made.")
else:
    heads_percentage = (heads / flips) * 100
    tails_percentage = (tails / flips) * 100

    print(f"Flips: {flips}")
    print(f"Heads: {heads} ({heads_percentage:.1f}%)")
    print(f"Tails: {tails} ({tails_percentage:.1f}%)")
