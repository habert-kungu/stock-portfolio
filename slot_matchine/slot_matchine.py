import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbol configurations
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

# Function to check winnings based on aligned symbols
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbols = columns[0][line]

        # Check if all symbols in the line are the same
        is_winning_line = all(column[line] == symbols for column in columns)
        
        if is_winning_line:
            # Calculate winnings based on symbol value and bet amount
            winnings += values[symbols] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Function to generate a random slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

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

# Function to print slot machine columns vertically
def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for column in columns:
            print(column[row], end=" | ")
        print()

# Function to get user deposit
def deposit():
    while True:
        amount = input("Deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0")
        else:
            print("Enter a number!")
    return amount

# Function to get the number of lines the user wants to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter NO of lines you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Amount should be between 1 and", MAX_LINES)
        else:
            print("Enter a number!")
    return lines

# Function to get the bet amount from the user
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be between $ {MIN_BET} - $ {MAX_BET}.")
        else:
            print("Enter a number!")
    return amount

# Function to simulate a slot machine spin and update the balance
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient balance: $ {balance}")
        else:
            break

    print(f"You are betting $ {bet} on {lines} lines. Total bet is equal to: $ {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You WON $ {winnings} !!")
    print(f"You WON on lines:", *winning_lines)
    return winnings - total_bet

# Main game loop
def main():
    balance = deposit()
    while True:
        print(f"Current balance is $ {balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
