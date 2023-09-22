import os
import time
import random

while True:
    os.system('cls')
    secret_number = random.randint(1, 100)
    total_guesses = 0
    while total_guesses <= 7:
        try:
            guess = input("gissa hemliga tal ")
            if guess == "/q" or guess == "/quit":
                exit()
                
            guess = int(guess)
        except ValueError:
            print ("Du måste skriva ett heltal - pröva igen\n")
            continue

        total_guesses += 1

        if guess > secret_number:
            print("för högt")
        
        elif guess < secret_number:
            print("för lågt")
        
        elif guess == secret_number: 
            print(f"Grattis du hittade {secret_number} på {str(total_guesses)}  försök! \n\n")
            break

        if total_guesses ==7:
            print(f"\nTyvärr, du hittade inte hemliga talet: {secret_number}.")
            break

    try_again = input("Vill du spela igen? Enter Ja/Nej")

    if try_again == 'N' or try_again == 'Nej':
        print("Tack för att du spelade!")
        exit()