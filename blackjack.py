#letsgooo

import random

class Deck:
    cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    delt_cards = []

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
game_deck = Deck()
dealer1 = Dealer()

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

set_player_name(player1)

def draw_card(deck, player):
    random_deck_index = random.randint(0, (len(deck.cards)))
    deck.delt_cards.append(deck.cards[random_deck_index])
    player.cards.append(deck.cards[random_deck_index])
    deck.cards.pop(random_deck_index)

def deal_cards(deck, dealer, player):
    for i in range(1, 3):
        draw_card(deck, player)
    for i in range(1, 3):
        draw_card(deck, dealer)

    
# deal_cards(game_deck, dealer1, player1)

# print(dealer1.cards)
# print(game_deck.delt_cards)
# print(player1.cards)



