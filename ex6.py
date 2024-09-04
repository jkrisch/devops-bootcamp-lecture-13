import random as r

number = r.randint(1,9)
guessed_number = 9999

while number != guessed_number:
    guessed_number = int(input("Guess a number between 1 and 9: "))
    if guessed_number < number:
        print(f"The number is higher then {guessed_number}")
    
    if guessed_number > number:
        print(f"The number is lower then {guessed_number}")


print(f"YOU WON!")