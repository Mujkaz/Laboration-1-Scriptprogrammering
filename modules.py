import random

" Hitta och skriva ut alla tal mellan 1 – 1600 som är delbara med två valda heltal "

" Användaren ska gissa vilken siffra. "

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
print ('hello world'
       )

