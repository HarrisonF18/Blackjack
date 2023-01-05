#letsgooo

import random
import os
import time

class Deck:
    cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    delt_cards = []

class Dealer:
    hand = []
    score = 0

class Player:
    name = ""
    cash = 1000
    initial_bet = 0
    insurance_bet = 0
    #hands 2-4 are for splitting
    hand_1 = []
    hand_2 = []
    hand_3 = []
    hand_4 = []
    hand_1_score = 0
    hand_2_score = 0
    hand_3_score = 0
    hand_4_score = 0
    hands_in_play = []
    available_plays = []
    

def start_game():
    player_start = False
    while player_start == False:
        print("Welcome to the Blackjack table!")
        player_ready = input("Enter 'start' to begin. ")
        if player_ready.lower() == "start":
            player_start = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
def set_player_name(player):
    set_player_name_complete = False
    while set_player_name_complete == False:
        input_name = input("Enter player name: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        correct_name_confirmation = input(input_name + ". Is this correct? (y/n)")
        if correct_name_confirmation != "y" and correct_name_confirmation != "n":
            print("Invaild choice")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if correct_name_confirmation == "y":
            player.name = input_name
            set_player_name_complete = True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome, " + player.name + ".")
    print("Your starting chips value is $1,000")
    time.sleep(3)

def make_bet(player):
    still_setting_bet = True
    while still_setting_bet == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Your current chip value: $" + str(player.cash))
        input_bet_amount = int(input("How much would you like to bet on this hand? "))
        if type(input_bet_amount) != int:
            print("Invalid Answer.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if input_bet_amount > player.cash:
            print("That is more money than you have.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if input_bet_amount <= player.cash:
            player_confirmation = input("$" + str(input_bet_amount) + ". Is this correct?(y/n) ")
            if player_confirmation == "y":
                player.initial_bet = input_bet_amount
                player.cash -= input_bet_amount
                still_setting_bet = False
            else:
                os.system('cls' if os.name == 'nt' else 'clear')


def draw_card(hand, deck):
    random_deck_index = random.randint(0, (len(deck.cards)-1))
    deck.delt_cards.append(deck.cards[random_deck_index])
    hand.append(deck.cards[random_deck_index])
    deck.cards.pop(random_deck_index)

def deal_cards(player, dealer, deck):
    os.system('cls' if os.name == 'nt' else 'clear')
    hands_to_deal = [player.hand_1, dealer.hand]
    for hand in hands_to_deal:
        counter = 0
        while counter < 2:
            draw_card(hand, deck)
            counter += 1
    dealing_animation()

# dealing animation to create real-life feeling
def dealing_animation():
    message = "Dealing"
    print(message)
    counter = 0
    while counter < 3:
        time.sleep(1)
        message = message + "."
        os.system('cls' if os.name == 'nt' else 'clear')
        print(message)
        counter += 1
    os.system('cls' if os.name == 'nt' else 'clear')

# to move aces to end of hand in order for compute_hand_score function to properly assign a 1 or 10 value to the ace.


def move_aces_to_end_of_hand(hand):
    aces_in_hand = []
    for i in hand:
        if i == "A":
            aces_in_hand.append(i)
            hand.remove(i)
    for i in aces_in_hand:
        hand.append(i)


def compute_hand_score(hand):
    move_aces_to_end_of_hand(hand)
    hand_score = 0
    for i in hand:
        if type(i) == int:
            hand_score += i
        if i == "K" or i == "Q" or i == "J":
            hand_score += 10
        if i == "A":
            if hand_score + 11 > 21:
                hand_score += 1
            else:
                hand_score += 11
    return hand_score

def determine_hands_in_play(player):
    possible_hands = [player.hand_1, player.hand_2,player.hand_3, player.hand_4]
    counter = 0
    while counter < 4:
        if len(possible_hands[counter]) > 0:
            player.hands_in_play.append(possible_hands[counter])
            counter += 1
        else:
            counter +=1

def print_player_hands_and_scores(player):
    print(player.name + "'s cards:")
    determine_hands_in_play(player)
    for hand in player.hands_in_play:
        hand_string = ""
        for card in hand:
            hand_string += str(card) + " "
        print(hand_string)
            
    print("Bet: $" + str(player.initial_bet))

    if player.insurance_bet > 0:
        print("Insurance: " + str(player.insurance_bet))
    print("")

            
    
                
def print_dealer_cards_during_hand(dealer):
    print("Dealer's cards:")
    print("X " + str(dealer.hand[1]))

def print_table_during_hand(player, dealer):
    print_dealer_cards_during_hand(dealer)
    print("")
    print_player_hands_and_scores(player)


# Next several functions for side betting.
def check_if_player_can_split(player):
    if player.current_bet > player.cash:
        return False
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

def initial_player_options(player, dealer):
    player.available_plays = ["Hit", "Stand", "Double Down", "Surrender"]
    if check_if_player_can_split(player) == True:
        player.available_plays.insert(3, "Split")
    if check_if_insurance_side_bet_available(dealer) == True:
        if len(player.available_plays) == 4:
            player.available_plays.insert(3, "Insurance")
        if len(player.available_plays) == 5:
            player.available_plays.insert(4, "Insurance")
    print("")
    print("Available Plays:")
    for i in player.available_plays:
        print(i)

# # def execute_player_choice(player, dealer, deck):
# #     play_selected = False
# #     while play_selected == False:
# #         player_choice = input("Enter play: ")
# #         if player_choice not in player.available_plays:
# #             print("Invaild entry.")
# #             time.sleep(2)
# #             print_cards_during_hand(player, dealer)
# #             initial_player_options(player, dealer)
# #             continue

# #         if player_choice.lower() == "hit":
# #             draw_card(player, dealer, deck)
# #             play_selected = True

# #         if player_choice.lower() == "double down":
# #             execute_double_down(player)
# #             play_selected = True

# #         if player_choice.lower() == "split":

        

def execute_surrender(player):
    player.cash += (player.current_bet / 2)
    # insert some way to end the hand

def execute_double_down(player):
    player.cash -= player.current_bet
    player.current_bet = (player.current_bet * 2)
    draw_card(player.hand_1, deck_1)
    #end player turn



def execute_insurance(player):
    player.insurance_bet = (player.current_bet / 2)
    player.available_plays.remove("Insurance")

def execute_split(player, hand):
    player.hand_2.append(player.hand_1)



# def offer_player_to_hit(player):
#     answer_submitted = False
#     while answer_submitted == False:
#         player_wants_hit = input("would you like another card? (y/n)")
#         if player_wants_hit == "y":
#             draw_card(player)
#             answer_submitted = True
#         if player_wants_hit == "n":
#             answer_submitted = True
#         else:
#             continue

# def dealer_hitting(dealer, deck):
#     while dealer.score < 17:
#         draw_card(deck, dealer)
#         compute_hand_score(dealer)

# def print_cards_dealers_turn(player, dealer):
#     print("Dealer cards: " + dealer.cards)
#     print(player.name + "'s cards: " + player.cards)

# def end_hand(player, dealer, deck):
#     player.cards = []
#     player.score = 0
#     dealer.cards = []
#     dealer.score = 0
#     player.current_bet = 0

#     for card in deck.delt_cards:
#         deck.cards.append(card)
#         deck.delt_cards.remove(card)

def game_play(player, dealer, deck):
    make_bet(player)
    deal_cards(player, dealer, deck)
    print_table_during_hand(player, dealer)
#     # print_cards_during_hand(player)
    

####start game####

os.system('cls' if os.name == 'nt' else 'clear')

start_game()

player_1 = Player()
dealer_1 = Dealer()
deck_1 = Deck()

set_player_name(player_1)

game_play(player_1, dealer_1, deck_1)

# print(player_hand_1.cards)
# print(dealer_hand.cards)

# deal_cards(player_1, dealer_1, deck_1)
# print_player_hands_and_scores(player_1)

# print(player_1.hand_1)
# print(dealer_1.hand)
# print(deck_1.cards)
# print(deck_1.delt_cards)