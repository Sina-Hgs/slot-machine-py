# GLOBAL VARIABLES

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


# DEPOSIT (THE AMOUNT THE USER BETS)


def deposit():
    while True:
        amount = input("What would you like to deposit? 💲")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("❌ Enter an amount greater than 0!")
        else:
            print("❌ Please enter a number.")

    return amount


# SLOT LINES (THE NUMBER OF LINES THE USER BETS ON THE SLOT MACHINE)


def get_number_of_line():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")🎰❔"
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("❌ Enter a valid number of lines!")
        else:
            print("❌ Please enter a number.")

    return lines


# MAIN FUNCTION


def main():
    balance = deposit()
    lines = get_number_of_line()
    print(balance, lines)


main()
