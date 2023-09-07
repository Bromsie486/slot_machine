import random


MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

balance = 0


def deposit():
    global balance
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                balance += amount
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a positive number.")


def get_number_of_lines():
    while True:
        lines = input("Please enter the number of lines to bet on ({}-{}): ".format(MIN_LINES, MAX_LINES))
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                return lines
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")


def get_bet():
    global balance
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET >= amount >= MIN_BET and amount <= balance:
                balance -= amount
                return amount
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")
    

    
def main():
    deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}. Remaining balance: {balance}")




main()