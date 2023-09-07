MAX_LINES = 3


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
        lines = input("Please enter the number of lines to bet on (1-{}): ".format(str(MAX_LINES)))
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")

    
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)



main()