import random
import datetime
import time
import json
from pathlib import Path
from typing import List

current_time = datetime.datetime.now()
print(current_time)
time.sleep(0.300)
print("Hello there!!")
time.sleep(0.300)
print("Welcome to the game --> Guess the secret number. <--")
time.sleep(1)


def hard():

    secret = random.randint(1, 30)
    attempts = 0
    score_path: Path = Path(".", "Score", "score_list_hard.txt")
    score_list: List[int] = json.loads(score_path.read_text())

    print("Nice to see you choose Hard level. Let's do it! 😁💪💪")
    time.sleep(1)
    name = input("Please enter your name: \n")
    time.sleep(0.500)
    print(f"Good luck {name}, you will need it.")
    time.sleep(1)

    while True:
        guess = int(
            input(
                "Guess the secret number. Secret number is between 1 and 30. Enter number:  "
            )
        )
        attempts += 1

        if guess == secret:
            print(f"Awessome!! You guessed it! The secret number was {secret}")
            time.sleep(1)
            print(f"Attempts needed {attempts}")
            score_list.append(
                {
                    "Player": name,
                    "Attempts": attempts,
                    "Secret number was": secret,
                    "date": str(datetime.datetime.now()),
                }
            )
            score_list_str = json.dumps(score_list)
            score_path.write_text(score_list_str)

            break

        else:
            print("Wrong wrong!😬😬 Try another one.")


def easy():
    secret_2 = random.randint(1, 50)
    attemts = 0
    score_path: Path = Path(".", "Score", "score_list_easy.txt")
    score_list_2: List[int] = json.loads(score_path.read_text())

    print("Have fun and try Hard level too! 😁😁")
    name = input("Please enter your name: \n")
    time.sleep(0.500)
    print(f"Good luck {name}, you will need it.")
    time.sleep(1)

    while True:
        guess = int(
            input(
                "Guess the secret number. The Secret number is between 1 and 50.\n Enter number: "
            )
        )
        attemts += 1

        if guess == secret_2:
            print(f"Great! You guessed it. The secret number was {secret_2}")
            time.sleep(1)
            print(f"Attempts needed: {attemts}")

            score_list_2.append(
                {
                    "Player": name,
                    "Attempts": attemts,
                    "Secret number was": secret_2,
                    "date": str(datetime.datetime.now()),
                }
            )
            score_list_2_str = json.dumps(score_list_2)
            score_path.write_text(score_list_2_str)

            break

        elif guess > secret_2:
            print("Wrong! Try a smaller number.")
        else:
            print("Wrong! Try a bigger number.")


def score_hard():
    score_path: Path = Path(".", "Score", "score_list_hard.txt")
    score_list: List[int] = json.loads(score_path.read_text())
    score_top_3 = sorted(score_list, key=lambda k: k["Attempts"])[:3]
    while True:
        print(f"Score list level Hard: {score_list}")
        time.sleep(0.500)
        print(f"\nTop scorers on level Hard are: {score_top_3}\n")
        break


def score_easy():
    score_path: Path = Path(".", "Score", "score_list_easy.txt")
    score_list_2: List[int] = json.loads(score_path.read_text())
    score_top_3 = sorted(score_list_2, key=lambda k: k["Attempts"])[:3]
    while True:
        print(f"Score list level Easy: {score_list_2}")
        time.sleep(0.500)
        print(f"\nTop scorers on level Easy are: {score_top_3}\n")
        break


while True:
    selection = input(
        "Please choose what you want to do / see: \n A) Play game (Level- Hard - No help)\n B) Play game (Level - easy - with help)\n C) Check top scorers for Hard and Easy levels\n D) Quit.\n"
    )

    if selection.upper() == "A":
        hard()

    elif selection.upper() == "B":
        easy()

    elif selection.upper() == "C":
        score_hard()
        score_easy()

    else:
        break
