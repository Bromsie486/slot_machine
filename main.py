import random


ROWS = 3
COLS = 3

balance = 0
row_content = {
    "A": 2,
    "B": 3,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    #Filling up the symbol list
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #Generate columns
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):           
            print(column[row], end=" | ") if i != len(columns) - 1 else print(column[row])     
                     

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



def get_bet():
    global balance
    while True:
        amount = input("How much would you like to bet $")
        if amount.isdigit():
            amount = int(amount)
            if amount <= balance:
                balance -= amount
                return amount
            else:
                print(f"Your current balance is {balance}, your bet cannot exceed that.")
        else:
            print("Please enter a number.")
    

    
def main():
    deposit()
    bet = get_bet()
    print(f"You are betting ${bet}. Remaining balance: {balance}")
    result = get_slot_machine_spin(ROWS, COLS, row_content)
    print_slot_machine(result)


main()