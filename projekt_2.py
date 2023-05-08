"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Pavel Kartin
email: pevelkartin@seznam.cz
discord: KKonaPaul#9430
"""

from random import randint
import math
import time

# [ Hlavní funkce ]
def bulls_and_cows():

    highest_score = 0

    # [ Pozdrav ]
    print("Hi there!")

    # [ Začátek hry ]
    while True:
        guess = ""
        number_of_tries = 0
        start_time = time.perf_counter() # Uložit čas

        print_separator()
        print("I've generated a random 4 digit number for you.")
        print("Let's play a bulls and cows game!")
        print_separator()

        # [ Vytvoření hádanky ]
        riddle = generate_4_digit_number()
        
        # [ == TEST == ]
        #print("[ANSWER]: " + riddle) 

        # [ Hra ]
        while guess != riddle:
            bulls = 0
            cows = 0
            number_of_tries += 1

            # [ Vstup uživatele ]
            guess = get_valid_user_input()

            # [ Hodnocení uživatelského odhadu ]
            for index, guessed_number in enumerate(guess):
                if guessed_number in riddle:
                    # Získat pozici uhodnutého čísla v hádance
                    number_position_in_riddle = riddle.index(guessed_number)

                    if index == number_position_in_riddle:
                        bulls += 1
                    else:
                        cows += 1

            print_progress(bulls, cows)
        
        # [ Konec hry ]
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        score = calculate_score(number_of_tries, elapsed_time)

        new_record = False

        if score > highest_score:
            highest_score = score
            new_record = True

        # [ Zpráva ] 
        if number_of_tries == 1:
            print("First try! Congratulations! You are very lucky.")
        else:
            print("Correct, you've guessed the right number! ")
            print(f"It took you {number_of_tries} guesses.")

        print(f"Your time is {format_time(elapsed_time, 2)} [{format_time(elapsed_time, 1)}]")
        
        if new_record:
            print(f"New record! {score}")
        else:
            print(f"Score: {score}, Highest score: {highest_score}")
        
        print_separator()
        
        if not play_again():
            break
    
# [ Ostatní funkce ]
def calculate_score(tries: int, time: float) -> int:
    base_score = 100000
    try_penalty = 5000
    time_penalty = 2000

    # formula
    score = int(base_score - (math.sqrt(tries) * try_penalty) - int(math.sqrt(time) * time_penalty))
    
    if tries == 1: score *= 2

    score = max(score, 0)

    return score

def print_separator():
    """Tiskne řádek symbolů."""
    print("-" * 47)

def generate_4_digit_number() -> str:
    """
    Vytváří čtyřmístné náhodné číslo s unikátními číslici a začínající 0.
    """
    # Nový list obsahující první číslici od 1 do 9.
    digits = [str(randint(1, 9))]

    # Pokračujte ve generování nových číslic (0-9).
    while len(digits) < 4:
        new_digit = str(randint(0, 9))

        if new_digit not in digits:
            digits.append(new_digit)

    # Převadi list na jediný řetězec
    return ''.join(digits)

def get_valid_user_input() -> str:
    """
    Zajišťuje, aby vstup splňoval nasledujicí podmínky:
    - Pouze 4 znaky
    - Pouze čísla
    - Nesmí začínat nulou
    - Čísla musí být unikatní
    """
    def print_error(message: str):
        """
        Vrácí chybovou zprávu obklopenou oddělovači.
        """
        print_separator()
        print(message)
        print_separator()

    def has_duplicats(string: str) -> bool:
        """
        Kontroluje, zda řetězec obsahuje více stejných znaků.
        """
        seen_chars = set()

        for char in string:
            if char in seen_chars:
                return True
            else:
                seen_chars.add(char)

        return False

    while True:
        user_input = input("Enter a number: ")
        
        if len(user_input) != 4:
            print_error("Input must contain only 4 characters! Try again.")
        elif not user_input.isdigit():
            print_error("Input contains non-numeric characters! Try again.")
        elif user_input[0] == "0":
            print_error("The number can't start with a zero! Try again.")
        elif has_duplicats(user_input):
            print_error("Input must contain unique numbers! Try again.")
        else:
            # "return" Přeruší smyčku jako "break"
            return user_input 

def play_again() -> bool:
    """
    Nabízí zahájení nové hry.
    """
    print("Would you like to play again?")
    user_input = input("(Y/N): ").upper()
    if user_input == "Y":
        return True
    else:
        return False

def print_progress(bulls: int, cows: int):
    """
    Vytiskne množství "bulls" a "cows" a ošetří množné číslo.
    """
    bulls_string = "bulls"
    cows_string = "cows"

    if bulls == 1: bulls_string = "bull"
    if cows == 1: cows_string = "cow"

    print(f"{bulls} {bulls_string}, {cows} {cows_string}")
    print_separator()

def format_time(seconds: float, time_format: int) -> str:
    """
    Převádí napočítané sekundy do čitelného formátu.
    Format 1 -> [00:00:000]
    Format 2 -> X minutes, X seconds and X ms
    """
    # Odděluje minuty a ponechává zbývající sekundy
    minutes, remainder = divmod(seconds, 60)
    # Odděluje sekundy a ponechává zbývající milisekundy
    seconds, milliseconds = divmod(remainder, 1)
    
    # Převést na celá čísla
    minutes = int(minutes)
    seconds = int(seconds)
    milliseconds = int(milliseconds * 1000)

    if time_format == 1:
        return f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}"
    elif time_format == 2:
        if minutes >= 1:
            return f"{minutes} minutes and {seconds} seconds"
        else:
            return f"{seconds} seconds and {milliseconds} ms"

# [ Spustit program ]    
bulls_and_cows()