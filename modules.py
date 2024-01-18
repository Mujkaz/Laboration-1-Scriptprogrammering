import random

def check_divisible():
    """ Hitta och skriva ut alla tal mellan 1 – 1600 som är delbara med två valda heltal """
    # Användaren ska ange två nummer som den vill kolla delbarhet på.
    try:
        divide_one = int(input("Ange det första numret!"))
        divide_two = int(input("Ange det andra numret!"))
        # If-sats där programmet kollar om det är ett heltal (felsökning).
        if divide_one <= 0 or divide_two <= 0:
            print("Var vänlig och ange ett heltal. ")
            return
        # Letar efter siffran användaren har skrivit -
        # - kör igenom for-loopen för att ta reda på vad den är delbar med.
        print(f"Heltal mellan 1 och 1600 som är delbara med både {divide_one} och {divide_two}")
        for i in range(1, 1601):
            if i % divide_one == 0 and i % divide_two == 0:
                print(i)
    # Felhantering.
    except ValueError:
        print("Felaktig inmatning. Ange heltal.")


def guess_game():
    """Gissningsspel - Gissa på en siffra som är slumpmässigt framkallad mellan 1- 60."""
    print("Gissa vilket nummer jag tänker på mellan 1-60!")
    # Siffran blir slumpmässig, sätter parameter till 1 - 60.
    number = random.randint(1, 60)

    guess = -1
    tries = 1
    # While-loop där programmet du får börja gissa på vilket -
    # - nummer som programmet har tagit fram.
    while guess != number:
        guess_string = input("Vilket nummer gissar du på? ")
        guess = int(guess_string)
    # If-sats där det först läggs på en gissning i dina försök.
    # Samt att du får meddelande ifall det är för högt/lågt.
        if guess < number:
            tries = tries + 1
            print("Du svarade fel, försök igen. Det var för lågt.")
        elif guess > number:
            tries = tries + 1
            print("Du svarade fel, försök igen. Det var för högt.")
    # Print där du lyckades gissa rätt, där numret kommer fram.
    # Print där hur många försök det tog för dig att gissa rätt.
    print(f"Du lyckades gissa rätt! Jag tänkte på {number}!")
    print(f"Det tog dig så här många gissningar {tries}!")
