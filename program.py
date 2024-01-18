import modules


# Importerar kod från modules.py filen.

# Funktion som visar meny till användaren
def menu_choice():
    print("[1]  Uppgift 1: Check divisible numbers")
    print("[2]  Uppgift 2: Guessing Game!")
    print("[3]  Uppgift 3: End Program.")


# Användarens alternativ är mellan 1-3.
def menu_operator(choice):
    if choice == 1:
        modules.check_divisible()
    elif choice == 2:
        modules.guess_game()
    elif choice == 3:
        exit()
    else:
        print("Ogiltigt val, var vänlig ange rätt alternativ.")


# Funktion som letar efter vilket val det är som användaren har skrivit in. Kopplad till funktion menu_operator.
def main():
    while True:
        menu_choice()
        try:
            choice = int(input("Vänligen ange ditt val."))
            menu_operator(choice)
        except ValueError:
            print("Ogiltig inmatning.")


# Kontrollerar om python-filen körs direkt eller om den importeras som en modul i ett annat program.
if __name__ == "__main__":
    main()
