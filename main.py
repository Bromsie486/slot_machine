MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100



def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
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
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET >= amount >= MIN_BET:
                return amount
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")
    

    
def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(balance, lines, bet)



main()