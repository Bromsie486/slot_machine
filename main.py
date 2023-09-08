import random


ROWS = 3
COLS = 3

balance = 0
row_content = {
    "A": 3,
    "B": 4,
    "C": 7,
    "D": 10
}


def check_results(bet, result):
    global balance
    correct_lines = 0
    multiplier = 1


    #Checking the correct lines
    for item in range(len(result[0])):
        temp_list = []
        for row in result:
            temp_list.append(row[item])
        
        first_item = temp_list[0]
        decider = True

        for entry in temp_list:
            if entry != first_item:
                decider = False
        
        if decider:
            correct_lines += 1
            if temp_list[0] == "A":
                multiplier *= 5
            elif temp_list[0] == "B":
                multiplier *= 3
            elif temp_list[0] == "C":
                multiplier *= 2
            else:
                multiplier *= 1.5

    if correct_lines > 0:
        prize = bet * multiplier
        balance += prize
        print(f"You have won on {correct_lines} lines! You gained ${prize}. Your new balance is {balance}.")
    else:
        print(f"You have lost. Your balance is {balance}.")


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
                print(f"You are betting ${amount}. Your balance is {balance}")
                return amount
            else:
                print(f"Your current balance is {balance}, your bet cannot exceed that.")
        else:
            print("Please enter a number.")
    
    
def main():
    print("Welcome to Skonda Casino!")
    deposit()
    while True:
        bet = get_bet()
        result = get_slot_machine_spin(ROWS, COLS, row_content)
        print_slot_machine(result)
        check_results(bet, result)
        

main()