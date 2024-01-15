import random

print("Gissa vilket nummer jag tänker på mellan 1-60!")

number = random.randint(1,60)

guess = -1

while guess != number:
    guess_string = input("Vilket nummer gissar du på? ")
    guess = int(guess_string)

    if guess < number:
        print("För lågt, försök igen!")
    elif guess > number:
        print("För högt, försök igen!")

print(f"Du lyckades gissa rätt! Jag tänkte på {number}!")1212

