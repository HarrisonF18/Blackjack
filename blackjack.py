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
    random_deck_index = random.randint(0, (len(deck.cards)-1))
    deck.delt_cards.append(deck.cards[random_deck_index])
    player.cards.append(deck.cards[random_deck_index])
    deck.cards.pop(random_deck_index)

def deal_cards(deck, dealer, player):
    for i in range(1, 3):
        draw_card(deck, player)
    for i in range(1, 3):
        draw_card(deck, dealer)

#to move aces to end of hand in order for compute_hand_score function to properly assign a 1 or 10 value to the ace.
def move_aces_to_end_of_all_players_cards(player, dealer):
    for person in [player, dealer]:
        aces_in_hand = []
        for i in person.cards:
            if i == "A":
                aces_in_hand.append(i)
                person.cards.remove(i)
        for i in aces_in_hand:
            person.cards.append(i)


def compute_hand_score(player):
    hand_score = 0
    for i in player.cards:
        if type(i) == int:
            hand_score += i
        if i == "K" or i == "Q" or i == "J":
            hand_score += 10
        if i == "A":
            if hand_score + 10 > 21:
                hand_score += 1
            else:
                hand_score += 10
    player.score = hand_score