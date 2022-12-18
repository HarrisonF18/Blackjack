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

print("Welcome to the Blackjack table")


# player1 = Player()

# game_prep_complete = False

# while game_prep_complete == False:
    
#     player_name_set = False
#     while player_name_set == False:
#         name = input("Enter name: ")
#         correct_name_confirmation = input(name + ". Is that correct? (y/n)")
#         if correct_name_confirmation == "y":
#             player1.self.name = name
#             player_name_set = True
