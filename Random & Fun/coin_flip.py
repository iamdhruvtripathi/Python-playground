import random

wins = 0
losses = 0
flips = 0
heads = 0
tails = 0
current_streak = 0
longest_streak = 0
streak_result = ""

print("Coin Flip Game")

while True:
    guess = input("\nChoose Heads or Tails, or type q to quit: ").strip().lower()

    if guess == "q":
        break

    if guess not in ["heads", "tails"]:
        print("Please choose Heads or Tails.")
        continue

    result = random.choice(["heads", "tails"])
    flips += 1

    if result == "heads":
        heads += 1
    else:
        tails += 1

    print(f"\nThe coin landed on {result.title()}!")

    if guess == result:
        wins += 1
        print("You win!")

        if streak_result == result:
            current_streak += 1
        else:
            current_streak = 1
            streak_result = result

        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        losses += 1
        print("You lose!")
        current_streak = 0
        streak_result = ""

    print(f"Score: {wins}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Current streak: {current_streak}")
    print(f"Longest streak: {longest_streak}")

print("\n--- Final Results ---")

if flips == 0:
    print("No games were played.")
else:
    heads_percentage = (heads / flips) * 100
    tails_percentage = (tails / flips) * 100
    win_percentage = (wins / flips) * 100

    print(f"Total flips: {flips}")
    print(f"Heads: {heads} ({heads_percentage:.1f}%)")
    print(f"Tails: {tails} ({tails_percentage:.1f}%)")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Win rate: {win_percentage:.1f}%")
    print(f"Longest streak: {longest_streak}")