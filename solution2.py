import random
import art
from os import system, name

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def dealCard():
    """Return a Random Card from deck"""
    card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    randomcard = random.choice(card_list)
    return randomcard

def calculate_score(cards):
    """Returns the Score from provided list of cards"""
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

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "It's a Draw 😓"
    elif computer_score == 0:
        return "😭😭😭 Opponent has Black Jack@ You Loose 😱😭😭"
    elif user_score == 0:
        return "You Win with Black Jack!!!!! 😍"
    elif user_score > 21:
        return "It's Bust. You loose :( 😭😭😭"
    elif computer_score > 21:
        return "Computer is Busted!!! You WIN!!! 😇😇😇"
    else:
        if user_score > computer_score:
            return "😇😇😇 YOU WIN THIS GAMER OF BLACK JACK!!!! 😇😇😇"
        else:
            return "😭😭😭 COMPUTER WINS! 😭😭😭"

def playBlackJack():
    clear()
    print(art.logo)
    user_card_list = []
    computer_card_list = []
    is_game_over = False

    for _ in range(2):
        user_card_list.append(dealCard())
        computer_card_list.append(dealCard())

    while not is_game_over:

        user_score = calculate_score(user_card_list)
        computer_score = calculate_score(computer_card_list)
        print(f"User's Cards: {user_card_list}")
        print(f"User: {user_score}        Computer:{computer_card_list[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit = input("Do you want to draw another card? press 'y' or 'n'").lower()
            if hit == 'y':
                    user_card_list.append(dealCard()) 
                    user_score = calculate_score(user_card_list)
                    print(f"User Card List: {user_card_list}")
                    print(f"User: {user_score}        Computer:{computer_card_list[0]}")
            else:
                is_game_over = True

    while computer_score!=0 and computer_score < 17:
        computer_card_list.append(dealCard())
        computer_score = calculate_score(computer_card_list)

    print(f"Your Final Hand is {user_card_list} and Score is {user_score}")
    print(f"Computer's Final Hand is {computer_card_list} and Score is {computer_score}")
    print(compare(user_score=user_score,computer_score=computer_score))
    restart = input("Do you want to play a game of Black Jack? y/N: ")
    if restart == 'y':
        playBlackJack()

restart = input("Do you want to play a game of Black Jack? y/N: ")
if restart == 'y':
    playBlackJack()