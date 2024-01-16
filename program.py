import modules

def menu_choice():
    print("[1]  Uppgift 1: Check divisible numbers")
    print("[2]  Uppgift 2: Guessing Game!")
    print("[3]  Uppgift 3: End Program.")

def menu_operator(choice):
    if choice == 1:
        modules.check_divisible()
    elif choice == 2:
        modules.guess_game()
    elif choice == 3:
        exit()
    else:
        print("Ogiltigt val, var vänlig ange rätt alternativ.")

def main():
    while True:
        menu_choice()
        try:
            choice = int(input("Vänligen ange ditt val."))
            menu_operator(choice)
        except ValueError:
            print("Ogiltig inmatning.")


