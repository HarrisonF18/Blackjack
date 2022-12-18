#letsgooo

import random

class Deck:
    deck = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]

class Dealer:
    cards = []
    score = 0

class Player:
    name = ""
    cards = []
    score = 0
    cash = 1000

print("Welcome to the Blackjack table")


player1 = Player()

def set_player_name(player):
    set_player_name_complete = False
    while set_player_name_complete == False:
        input_name = input("Enter player name:")
        correct_name_confirmation = input(input_name + ". Is this correct? (y/n)")
        if correct_name_confirmation != "y" and correct_name_confirmation != "n":
            print("Invaild choice")
            continue
        if correct_name_confirmation == "y":
            player.name = input_name
            set_player_name_complete = True