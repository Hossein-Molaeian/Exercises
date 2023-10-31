"""
All the info about this game is available on Wikipedia.
https://en.wikipedia.org/wiki/War_(card_game)
"""


import random

# Here we will use global variables that we know don't change regardless of the situation

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Card class for each card's attributes


class Card():

    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = values[rank.capitalize()]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck class made up of multiple Card class objects


class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# Player should be able to hold instances of Cards, they should also be able to remove and add Cards from their hand.


class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        # We state index 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

# GAME LOGIC


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

# Split the Deck between 2 players

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:

    round_num += 1
    print(f"Round {round_num}")

    # Check to see if a player is out of cards

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards. Player Two wins!')
        game_on = False
        break

    if len(player_one.all_cards) == 0:
        print('Player Two, out of cards. Player One wins!')
        game_on = False
        break

    # Start a new round and reset current cards "on the table"

    player_one_table_cards = []
    player_one_table_cards.append(player_one.remove_one())
    player_two_table_cards = []
    player_two_table_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_table_cards[-1].value > player_two_table_cards[-1].value:

            player_one.add_cards(player_one_table_cards)
            player_one.add_cards(player_two_table_cards)

            at_war = False

        elif player_one_table_cards[-1].value < player_two_table_cards[-1].value:

            player_two.add_cards(player_one_table_cards)
            player_two.add_cards(player_two_table_cards)

            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war, Player Two wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war, Player One wins!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_table_cards.append(player_one.remove_one())
                    player_two_table_cards.append(player_two.remove_one())
