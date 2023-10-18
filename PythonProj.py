import random

class RouletteGame:
    def __init__(self):
        self.bankroll = int(input("What is your starting balance (in whole $$): "))
        self.slots = {
            "00": "green",
            "0": "green",
            **{str(i): "red" if i % 2 else "black" for i in range(1, 37)},
        }
    global spins
    def spins(self):
        result = random.choice(list(self.slots.keys()))
        return result, self.slots[result]
    global bet_value
    def bet_value(self, bet_type):
        if bet_type == 1:
            return int(input("Is it an EVEN (1) or an ODD (2) bet?: "))
        if bet_type == 2:
            return int(input("Is it a RED (1) or a BLACK (2) bet?: "))
        if bet_type in [8, 9, 10, 11]:
            num_count = 2 if bet_type == 8 else bet_type - 6
            bet_list = [int(input(f"What is your {i} number?: ")) for i in range(1, num_count + 1)]
            return bet_list
        if bet_type == 12:
            return ["00", "0", "1", "2", "3"]
        if bet_type == 13:
            return int(input("What number do you want to choose (00, 0, 1-36)?: "))


    global adjusted_bankroll
    def adjusted_bankroll(self, result, bet_val, bet_type):
        bet = int(input("How much do you want to bet?: "))

        if bet < 10:
            print("Minimum bet is $10. Game over!")
            return
        global prob
        self.bankroll -= bet
        prob = "47.37%"

        if bet_type == 1 and bet_val == 1:
            if (int(result) % 2 == 0) and (int(result) != 0):
                payout = bet
                self.bankroll += bet + payout
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        # Handle other bet types here...
        if (bet_type == 1) and (bet_val == 1):  # Even
            prob = "47.37%"
            if (int(result) % 2 == 0) and (int(result) != 0):
                payout = bet
                self.bankroll += bet + payout
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        if (bet_type == 1) and (bet_val == 2):  # Odd
            prob = "47.37%"
            if int(result) % 2 == 1:
                payout = bet
                self.bankroll += bet + payout
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        # Adjust player balance for red/black bets.
        if (bet_type == 2) and (bet_val == 1):  # Red
            prob = "47.37%"
            if self.slots[result] == "red":
                self.bankroll += 2 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        if (bet_type == 2) and (bet_val == 2):  # Black
            prob = "47.37%"
            if self.slots[result] == "black":
                self.bankroll += 2 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        # Adjust player balance for the set of twelves.
        if bet_type == 3:  # First Twelve
            prob = "31.58%"
            if (int(result) >= 1) and (int(result) <= 12):
                self.bankroll += 3 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        if bet_type == 4:  # Second Twelve
            prob = "31.58%"
            if (int(result) >= 13) and (int(result) <= 24):
                self.bankroll += 3 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        if bet_type == 5:  # Third Twelve
            prob = "31.58%"
            if (int(result) >= 25) and (int(result) <= 36):
                self.bankroll += 3 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        # Adjust the player balance for the first and second set of eighteen.
        if bet_type == 6:  # First Eighteen
            prob = "47.37%"
            if (int(result) >= 1) and (int(result) <= 18):
                self.bankroll += 2 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        if bet_type == 7:  # Second Eighteen
            prob = "47.37%"
            if (int(result) >= 19) and (int(result) <= 36):
                self.bankroll += 2 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        # Adjust for betting multiple numbers at the same time.
        if bet_type == 8:  # Combination of two numbers
            prob = "5.26%"
            if int(result) in bet_val:
                self.bankroll += 18 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        if bet_type == 9:  # Combination of three numbers
            prob = "7.89%"
            if int(result) in bet_val:
                self.bankroll += 12 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        if bet_type == 10:  # Combination of four numbers
            prob = "10.53%"
            if int(result) in bet_val:
                self.bankroll += 9 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        if bet_type == 11:  # Combination of six numbers
            prob = "16.2%"
            if int(result) in bet_val:
                self.bankroll += 6 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        if bet_type == 12:  # Combination of 00-0-1-2-3
            prob = "13.16%"
            if result in bet_val:
                self.bankroll += 7 * bet
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll
        # Adjust player balance if bet on a single number.
        if bet_type == 13:
            prob = "2.63%"
            if result == bet_val:
                payout = 36 * bet
                self.bankroll += payout
                prompt = "Winner! You now have $%s dollars!" % self.bankroll
            else:
                prompt = "Loser! You now have $%s dollars!" % self.bankroll

        return prompt, self.bankroll

total_bets = 0
wins = 0
keep_playing = "yes"
while (keep_playing.lower() == "yes") or (keep_playing.lower() == "y"):
    bet = int(input("How much do you want to bet?: "))
    if bet >= 10:
        bet_type = int(
            input(
                "What type of bet? Choose one of the given numbers:\n"
                "1 = Even/Odd\n"
                "2 = Red/Black\n"
                "3 = First Twelve (1-12)\n"
                "4 = Second Twelve (13-24)\n"
                "5 = Third Twelve (25-36)\n"
                "6 = First Eighteen (1-18)\n"
                "7 = Second Eighteen (19-36)\n"
                "8 = Combination of Two Numbers\n"
                "9 = Combination of Three Numbers\n"
                "10 = Combination of Four Numbers\n"
                "11 = Combination of Six Numbers\n"
                "12 = Combination of 1-2-3-0-00\n"
                "13 = One Number (Straight Up)"
            )
        )
        (prompt, balance) = adjusted_bankroll(spins(), bankroll, bet_value(bet_type))
        print(prompt,"Won with",prob,"Chance of winning this bet type")
        # Update total_bets and wins
        total_bets += 1
        if "Winner" in prompt:
            wins += 1
        # Calculate and print win rate
        win_rate = (wins / total_bets) * 100
        print("Total Bets:", total_bets)
        print("Total Wins:", wins)
        print("Win Rate: {:.2f}%".format(win_rate))
    if bankroll < 10:
        print(
            "Sorry, minimum bet is 10 dollars, please deposit for more fun >_<. Game over!"
                )
        break
    
    else:
        bankroll = balance
        keep_playing = input("Would you like to keep playing? (Y/N): ")