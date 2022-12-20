#letsgooo

import random
import os
import time

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
    current_bet = 0
    requested_side_bets = []

def start_game():
    player_start = False
    while player_start == False:
        print("Welcome to the Blackjack table!")
        player_ready = input("Enter 'start' to begin.")
        if player_ready.lower() == "start":
            player_start = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
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
    print("Welcome, " + player.name)
    print("Your starting chips value is $1,000")
    time.sleep(3)

def make_bet(player):
    still_setting_bet = True
    while still_setting_bet == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Your current chip value: $" + player.cash)
        input_bet_amount = input("How much would you like to bet on this hand?")
        if type(input_bet_amount) != int:
            print("Invalid Answer.")
            time.sleep(3)
            continue
        if input_bet_amount > player.cash:
            print("That is more money than you have.")
            time.sleep(3)
            continue
        if input_bet_amount <= player.cash:
            player.current_bet = input_bet_amount
            player.cash -= input_bet_amount
    
def draw_card(player, deck):
    random_deck_index = random.randint(0, (len(deck.cards)-1))
    deck.delt_cards.append(deck.cards[random_deck_index])
    player.cards.append(deck.cards[random_deck_index])
    deck.cards.pop(random_deck_index)
    move_aces_to_end_of_all_players_cards()

def deal_cards(player, dealer, deck):
    for i in range(1, 3):
        draw_card(deck, player)
    for i in range(1, 3):
        draw_card(deck, dealer)

def print_cards_during_hand(player, dealer):
    print("Dealer cards: X " + dealer.cards[1])
    print("Dealer score: " + dealer.score)
    print("")
    print(player.name + "'s cards: " + player.cards)
    print(player.name + "'s score: " + player.score)
    print("Bet amount: $" + player.current_bet)
    print("Chips: $" + player.cash)

def print_cards_dealers_turn(player, dealer):
    print("Dealer cards: X " + dealer.cards)
    print(player.name + "'s cards: " + player.cards)

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
            if hand_score + 11 > 21:
                hand_score += 1
            else:
                hand_score += 11
    player.score = hand_score

# Next several functions for side betting.
def check_if_player_can_split(player):
    value_10_cards = ["K", "Q", "J", 10]
    if player.cards[0] == player.cards[1]:
        return True
    if player.cards[0] in value_10_cards and player.cards[1] in value_10_cards:
        return True
    else:
        return False

def check_if_insurance_side_bet_available(dealer):
    if dealer.cards[1] == "A":
        return True
    else:
        return False

def available_side_bets(player, dealer):
    available_side_bets = ["Surrender","Double Down"]
    if check_if_player_can_split(player) == True:
        available_side_bets.append("Split")
    if check_if_insurance_side_bet_available(dealer) == True:
        available_side_bets.append("Insurance")
    available_side_bets.append("No Side Bet")
    return available_side_bets

def set_side_bet(player, dealer):
    setting_side_bet = True
    while setting_side_bet == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_cards_during_hand(player, dealer)
        player_wants_side_bet = input("Would you like to place a side bet? (y/n)")
        if player_wants_side_bet == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            print_cards_during_hand(player, dealer)
            print("Available Side Bets:")
            available_side_bets = available_side_bets(player, dealer)
            for side_bet in available_side_bets:
                print(side_bet)
            selected_side_bet = input("Enter Selection: ")
            if selected_side_bet not in available_side_bets:
                continue
            else:
                setting_side_bet = False
                return selected_side_bet
        if player_wants_side_bet == "n":
            setting_side_bet = False
        else:
            continue

def execute_surrender(player, dealer):
    player.cash += (player.current_bet / 2)
    #insert some way to ed the hand

def execute_double_down(player):
    player.cash -= player.current_bet
    player.current_bet = (player.current_bet * 2)
    #insert way to limit additional cards to 1

def execute_insurance(player, dealer):
    if check_if_insurance_side_bet_available(dealer) == True:
        




def offer_player_to_hit(player):
    answer_submitted = False
    while answer_submitted == False:
        player_wants_hit = input("would you like another card? (y/n)")
        if player_wants_hit == "y":
            draw_card(player)
            answer_submitted = True
        if player_wants_hit == "n":
            answer_submitted = True
        else:
            continue

def dealer_hitting(dealer, deck):
    while dealer.score < 17:
        draw_card(deck, dealer)
        compute_hand_score(dealer)

def end_hand(player, dealer, deck):
    player.cards = []
    player.score = 0
    dealer.cards = []
    dealer.score = 0
    player.current_bet = 0

    for card in deck.delt_cards:
        deck.cards.append(card)
        deck.delt_cards.remove(card)

def game_play(player, dealer, deck):
    make_bet(player)
    deal_cards(player, dealer, deck)
    print_cards_during_hand(player, dealer)
    #insert side 