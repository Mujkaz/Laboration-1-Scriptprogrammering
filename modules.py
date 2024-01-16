import random

def check_divisible():
    """ Hitta och skriva ut alla tal mellan 1 – 1600 som är delbara med två valda heltal """
    try:
        divide_one = int(input("Ange det första numret!"))
        divide_two = int(input("Ange det andra numret!"))

        if divide_one <= 0 or divide_two <= 0:
            print("Var vänlig och ange ett heltal. ")
            return

        print(f"Heltal mellan 1 och 1600 som är delbara med både {divide_one} och {divide_two}")
        for i in range (1, 1601):
            if i % divide_one == 0 and i % divide_two == 0:
                print(i)

    except ValueError:
        print("Felaktig inmatning. Ange heltal.")



def guess_game():


print("Gissa vilket nummer jag tänker på mellan 1-60!")

number = random.randint(1,60)

guess = -1
tries = 1
while guess != number:
    guess_string = input("Vilket nummer gissar du på? ")
    guess = int(guess_string)

    if guess < number:
        tries = tries + 1
        print("Du svarade fel, försök igen. Det var för lågt.")
    elif guess > number:
        tries = tries + 1
        print("Du svarade fel, försök igen. Det var för högt.")

print(f"Du lyckades gissa rätt! Jag tänkte på {number}!")
print(f"Det tog dig så här många gissningar {tries}!")

