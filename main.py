from art import logo, vs
from game_data import data
from random import randint

def clear():
    print("\n" * 20)
def a_greater_than_b(a_dict, b_dict):
    if a_dict["follower_count"] > b_dict["follower_count"]:
        return True
    elif a_dict["follower_count"] < b_dict["follower_count"]:
        return False
    else:
        return False


def start():

    game_on = True
    score = 0
    while game_on:
        clear()
        print("Welcome! 😁")
        #print the logo
        print(logo)
        # retrieve & assign a random entry from game_data
        a = data[randint(0, len(data) - 1)]
        # a is now a dictionary
        # print(a)

        print(f"Compare A: {a['name']}, a {a['description']}, from  {a['country']}.")
        b = data[randint(0, len(data) - 1)]
        # b is now a dictionary
        # print(a)
        print(vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from  {b['country']}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': \t")
        m = a_greater_than_b(a, b)
        if user_choice.lower() == 'a' and m is True:
            if a["follower_count"] > b['follower_count']:
                print("a > b")
            score += 1
            continue
        elif user_choice.lower() == 'a' and m is False:
            game_on = False
        elif user_choice.lower() == 'b' and m is True:
            game_on = False
        elif user_choice.lower() == 'b' and m is False:
            if a["follower_count"] < b['follower_count']:
                print("b > a")
            score += 1
            continue
    print(f"Sorry, that's wrong. Final Score = {score}")


start()
