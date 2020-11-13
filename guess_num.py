import random
import datetime
import time
import json
from pathlib import Path


current_time = datetime.datetime.now()
print(current_time)
time.sleep(0.300)
print("Hello there!!")
time.sleep(0.300)
print("Welcome to the game --> Guess the secret number. <--")
time.sleep(1)


while True:
    selection = input(
        "Please choose what you want to do / see: \n A) Play game (Level- Hard - No help)\n B) Play game (Level - easy - with help)\n C) Check top scorers for Hard and Easy levels\n D) Quit.\n"
    )

    if selection.upper() == "A":
        play_game_hard()

    elif selection.upper() == "B":
        play_game_easy()

    elif selection.upper() == "C":
        get_score_hard()
        get_score_easy()

    else:
        break


def play_game_hard():

    secret = random.randint(1, 50)
    attempts = 0
    score_list = get_score_list_hard()
    print("Nice to see you choose Hard level. Let's do it! 😁💪💪")
    name = input("Please enter your name: \n")
    time.sleep(0.500)
    print(f"Good luck {name}, you will need it.")

    while True:
        guess = int(
            input(
                "Please guess the secret number. Secret number is between 1 and 50 : "
            )
        )
        attempts += 1

        if guess == secret:
            score_list.append(
                {
                    "Player": name,
                    "Attempts": attempts,
                    "Secret number was": secret,
                    "date": datetime.datetime.now(),
                }
            )
            with open(".", "Score", "score_list_hard.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

                print(f"Awessome!! You guessed it! The secret number was {secret}")
            break
        else:
            print("Wrong wrong!😬😬 Try another one.")


def play_game_easy():
    secret_2 = random.randint(1, 100)
    attemts = 0
    score_list_2 = get_score_list_easy()
    print("Have fun and try Hard level too! 😁😁")
    name = input("Please enter your name: \n")
    time.sleep(0.500)
    print(f"Good luck {name}, you will need it.")

    while True:
        guess = int(
            input(
                "Please guess the secret number. The Secret number is between 1 and 100.\nEnter number: "
            )
        )
        attemts += 1

        if guess == secret_2:

            score_list_2.append(
                {
                    "Player": name,
                    "Attempts": attemts,
                    "Secret number was": secret_2,
                    "date": datetime.datetime.now(),
                }
            )
            with open(".", "Score", "score_list_easy.txt", "w") as score_file:
                score_file.write(json.dumps(score_list_2))
            print(f"Great! You guessed it. The secret number was {secret_2}")
            time.sleep(1)
            print(f"Attempts needed: {attemts}")

        elif guess > secret_2:
            print("Wrong! Try a smaller number.")
        else:
            print("Wrong! Try a bigger number.")


def get_score_list_hard():
    with open(".", "Score", "score_list_hard.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def get_score_list_easy():
    with open(".", "Score", "score_list_easy.txt", "r") as score_file:
        score_list_2 = json.loads(score_file.read())
        return score_list_2
