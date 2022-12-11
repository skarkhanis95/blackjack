import random
import art
from os import system, name
card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card_list = []
computer_card_list = []

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def dealCard():
    """Return a Random Card from deck"""
    randomcard = random.choice(card_list)
    return randomcard

def calculate_score(cards):
    sum_of_cards = sum(cards)
    if len(cards) == 2:
        if 11 in cards and 10 in cards:
            return 0
    if 11 in cards:
        if sum_of_cards > 21:
            cards.remove(11)
            cards.append(1)
        sum_of_cards = sum(cards)
    return sum_of_cards

def compare(user_score,computer_score,sent_user_list,sent_computer_list):
    if user_score == computer_score:
        # print(f"User Card List: {user_card_list}")
        # print(f"Computer Card List: {computer_card_list}")
        print(f"User Card List: {sent_user_list}")
        print(f"Computer Card List: {sent_computer_list}")
        print(f"User: {user_score}        Computer:{computer_score}")
        print("It's a Draw! 🥹")
    elif user_score > computer_score and user_score < 21:
        # print(f"User Card List: {user_card_list}")
        # print(f"Computer Card List: {computer_card_list}")
        print(f"User Card List: {sent_user_list}")
        print(f"Computer Card List: {sent_computer_list}")
        print(f"User: {user_score}        Computer:{computer_score}")
        print("User Wins 😀")
    elif computer_score > user_score and computer_score < 21:
        # print(f"User Card List: {user_card_list}")
        # print(f"Computer Card List: {computer_card_list}")
        print(f"User Card List: {sent_user_list}")
        print(f"Computer Card List: {sent_computer_list}")
        print(f"User: {user_score}        Computer:{computer_score}")
        print("Computer Wins 😰")
    elif user_score < 21 and computer_score > 21:
        # print(f"User Card List: {user_card_list}")
        # print(f"Computer Card List: {computer_card_list}")
        print(f"User Card List: {sent_user_list}")
        print(f"Computer Card List: {sent_computer_list}")
        print(f"User: {user_score}        Computer:{computer_score}")
        print("User Wins 😀")


def playBlackJack():
    clear()
    print(art.logo)
    user_card_list = []
    computer_card_list = []

    for _ in range(2):
        user_card_list.append(dealCard())
        computer_card_list.append(dealCard())
    

    user_score = calculate_score(user_card_list)
    computer_score = calculate_score(computer_card_list)
    print(f"User Card List: {user_card_list}")
    temp_comp_list = []
    temp_comp_list.append(computer_card_list[0])
    print(f"Computer Card List: {temp_comp_list}")
    print(f"User: {user_score}        Computer:{temp_comp_list[0]}")
    continue_playing = True
    restart = False


    while continue_playing:
        if user_score == 0 or computer_score == 0:
            if user_score == 0:
                print(f"User Card List: {user_card_list}")
                print(f"Computer Card List: {computer_card_list}")
                print("Black Jack - User Wins")
                continue_playing = False
            else:
                print(f"User Card List: {user_card_list}")
                print(f"Computer Card List: {computer_card_list}")
                print("Black Jack - Computer Wins")
                continue_playing = False
        elif user_score > 21:
            print(f"User Card List: {user_card_list}")
            print(f"Computer Card List: {computer_card_list}")
            print("User Looses")
            continue_playing = False
        elif user_score == 21:
            print(f"User Card List: {user_card_list}")
            print(f"Computer Card List: {computer_card_list}")
            print("Black Jack - User Wins")
            continue_playing = False
        else:
            hit = input("Do you want to draw another card? press 'y' or 'n'").lower()

            if hit == 'y':
                user_card_list.append(dealCard()) 
                user_score = calculate_score(user_card_list)
                print(f"User Card List: {user_card_list}")
                temp_comp_list = []
                temp_comp_list.append(computer_card_list[0])
                print(f"Computer Card List: {temp_comp_list}")
                print(f"User: {user_score}        Computer:{temp_comp_list[0]}")
            else:
                while computer_score <=17:
                    computer_card_list.append(dealCard())
                    computer_score = calculate_score(computer_card_list)
                
                compare(user_score=user_score,computer_score=computer_score,sent_user_list=user_card_list,sent_computer_list=computer_card_list)
                continue_playing = False
    restart = input("Do you want to play another game of Black Jack? y/N: ")
    if restart == 'y':
        playBlackJack()

playBlackJack()
