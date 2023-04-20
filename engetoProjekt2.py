import random
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Lenka Maresova
email: lenkamaresu@gmail.com
discord: lenka #8806
"""
"""
GAME:  BULLS & COWS
"""


def beginning_of_game(separator: str) -> None:
    """
    Popis:
    Tato funkce vypise pozdrav a pravidla hry.
    """
    print(
        "Hi player",
        separator,
        "Game rule: ",
        "You have to guess all numbers in right order.",
        "Numbers can't repeat.",
        "Let's play bulls and cows game.",
        separator,
        sep="\n"
    )


def how_many_numbers_input() -> int:
    """
    Popis: funkce vraci pocet cisel k hadani, zadane uzivatelem
    """
    return int(input("How many numbers, do you want to guess?:\n"))


def get_numbers_to_guessing(number_of_guessing_numbers: int) -> list:
    """
    popis:
    1. funkce vraci list nahodne vybranych cisel,
    2. prvni cislo neni nula
    3. list je dlouhy podle zadani uzivatele
    """
    numbers = list()
    numbers.append(random.randint(1, 9))
    for _ in range(1, number_of_guessing_numbers):
        while True:
            number = random.randint(0, 9)
            if number in numbers:
                continue
            else:
                numbers.append(number)
                break
    return numbers


def numbers_input(number_of_guessing_numbers: int) -> list:
    """
    Popis:
    1. funkce vraci list cisel zadanych uzivatelem,
    2. pokud uzivatel zada spatny pocet cisel
    nebo neco jineho nez cislo
    nebo vice stejnych cisel -
    tak se zadavani opakuje, dokud neni zadane cislo spravne
    """
    while True:
        numbers = input(f"Write {number_of_guessing_numbers} numbers: ")
        if len(numbers) != number_of_guessing_numbers\
                or not numbers.isnumeric()\
                or len(set(numbers)) != len(numbers):
            print("You write wrong. Try again...")
            continue
        else:
            return list(numbers)


def get_bulls(numbers: list, user_input_numbers: list) -> int:
    """
    Popis: vrati pocet cisel, ktere jsou zcela spravne
    """
    bulls = 0
    for index in range(len(user_input_numbers)):
        if numbers[index] == int(user_input_numbers[index]):
            bulls += 1
    return bulls


def get_cows(numbers: list, user_input_numbers: list) -> int:
    """
    Popis: vrati pocet cisel, ktere jsou pritomne v hadanem cisle, ale jsou na spatnem miste
    """
    cows = 0
    for i in range(len(user_input_numbers)):
        if int(user_input_numbers[i]) in numbers\
                and int(user_input_numbers[i]) != numbers[i]:
            cows += 1
    return cows


def outcome(bulls: int, cows: int) -> None:
    """
    Popis: funkce vypise pocet bulls a cows
    """
    def outcome_bull(bull: int) -> str:
        if bull == 1:
            return "bull"
        elif bull != 1:
            return "bull"

    def outcome_cow(cow: int) -> str:
        if cow == 1:
            return "cow"
        elif cow != 1:
            return "cow"

    outcome_bulls = outcome_bull(bulls)
    outcome_cows = outcome_cow(cows)
    print(f"{bulls} {outcome_bulls}, {cows} {outcome_cows}")


def ending(separator: str, number_of_tries: int) -> str:
    """
    Popis:
    1. funkce vypise "You are WINNER"
    2. vypise na kolik pokusu hrac hledane cislo uhodl
    3. Zepta se hrace, zda chce hrat dalsi hru
    4. vrati hracovu odpoved
    """
    print(
        separator,
        f"You are WINNER {'!' * 5}",
        f"You guessed the number in {number_of_tries} guesses.",
        separator,
        sep="\n")
    end_or_continue = input("Do you want play again? (y/n) ")
    print(separator)
    return end_or_continue


def main():
    separator = "=" * 45
    beginning_of_game(separator)
    while True:
        number_of_tries = 0
        number_of_guessing_numbers = how_many_numbers_input()
        print(separator)
        numbers = get_numbers_to_guessing(number_of_guessing_numbers)
        print(numbers)
        while True:
            number_of_tries += 1
            user_input_numbers = numbers_input(number_of_guessing_numbers)
            bulls = get_bulls(numbers, user_input_numbers)
            cows = get_cows(numbers, user_input_numbers)
            outcome(bulls, cows)
            if bulls == len(numbers):
                break
        end_or_continue = ending(separator, number_of_tries)
        if end_or_continue.lower() == "y":
            continue
        else:
            print("Ending .....", separator, sep="\n")
            break


if __name__ == "__main__":
    main()
