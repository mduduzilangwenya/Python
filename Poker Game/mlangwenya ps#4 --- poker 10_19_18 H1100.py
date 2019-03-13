import collections
import itertools
import random

import matplotlib.pyplot as plt
import numpy as np

RANK_LIST = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
SUIT_LIST = ("H", "S", "D", "C")
HAND_RANK = ("High-Card", "One-Pair", "Two-Pair", "3-of-a-Kind", "Straight",
             "Flush", "Full-House", "4-of-a-Kind", "Straight-Flush")

class Card:
    """
    Class that defines a particular card.  Each card has a rank and suit.
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.card = self.rank, self.suit
        
    def __repr__(self):
        return self.rank + "-" + self.suit
    
class PokerHand:
    """
    Class that defines a poker hand.
    """
    def __init__(self, card_list):
        self.card_list = card_list

    def get_hand_rank(self):
        rank_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            rank_dict[my_card.rank] += 1
            suit_dict[my_card.suit] += 1

        # check for poker hand
        #
        hand_rank = HAND_RANK[0]

        # check for one pair
        if len(rank_dict) == 4:
            hand_rank = HAND_RANK[1]
        # check for two pair or 3-of-a-kind
        elif len(rank_dict) == 3:
            if 3 in rank_dict.values():
                hand_rank = HAND_RANK[3]
            else:
                hand_rank = HAND_RANK[2]
        # check for Full House or 4-of-a-kind
        elif len(rank_dict) == 2:
            if 2 in rank_dict.values():
                hand_rank = HAND_RANK[6]
            else:
                hand_rank = HAND_RANK[7]
        else:
            # check for Flush and Straight
            straight, flush = False, False
            if len(suit_dict) == 1:
                flush = True
            min_rank = min([RANK_LIST.index(x) for x in rank_dict.keys()])
            max_rank = max([RANK_LIST.index(x) for x in rank_dict.keys()])
            if int(max_rank) - int(min_rank) == 4:
                straight = True
            # see if Ace exists and can be low
            low_straight = set(("A", "2", "3", "4", "5"))
            if not set(rank_dict.keys()).difference(low_straight):
                straight = True
            if straight and not flush:
                hand_rank = HAND_RANK[4]
            elif flush and not straight:
                hand_rank = HAND_RANK[5]
            elif flush and straight:
                hand_rank = HAND_RANK[8]

        enumeration = ",".join([str(x) for x in self.card_list])
        return hand_rank, "{enumeration} ({hand_rank})".format(**locals())
   
class Deck(set):
    """
    Class that defines a standard deck of cards.  Each deck has the standard 52 cards, which
    consists of 13 ranks and 4 suits.  Class inherits from class set.
    """
    def __init__(self):
        """
        Generate a standard deck of cards and add to the set of cards.
        """
        for rank, suit in itertools.product(RANK_LIST, SUIT_LIST):
            self.add(Card(rank, suit))
        
    def get_card(self):
        """
        Return a card from the deck of cards.  This is accomplished by retrieving a random
        sample without replacement.  The chosen card is then removed from the deck.
        :return: Card
        """
        a_card = random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card
    
    def get_hand(self, number_of_cards=5):
        if number_of_cards == 5:
            return PokerHand([self.get_card() for x in range(number_of_cards)])
        else:
            raise NotImplementedError
    
    def get_five_cards(self, number_of_hands, HAND_RANK):
        # counts           
        frequency_hand_rank = {}
        for hand_rank in HAND_RANK:
            frequency_hand_rank[hand_rank] = 0
        for i in range(number_of_hands):
            hand_rank, details = Deck().get_hand().get_hand_rank()
            frequency_hand_rank[hand_rank] += 1
        for rank, count in frequency_hand_rank.items():
            frequency_hand_rank[rank] = count/number_of_hands*100.0
           
        print("\nGET ALL FIVE CARDS AT ONE\n")
        print("With " + str(number_of_hands) + " poker hands dealt")
        print("Poker Hand   Probability")
        for hand, prob in frequency_hand_rank.items():
            print(f"{hand}\t\t{prob:10.4e}")
    
    def conditional_on_two(self, number_of_hands, HAND_RANK):
        deck_set =  list(self)
        first_card = random.sample(deck_set, 1)[0]
        deck_set.remove(first_card)
        second_card  = random.sample(deck_set, 1)[0]
        first_two_cards = [first_card, second_card]
        deck_set.remove(second_card)
        three_cards = list(itertools.combinations(deck_set, 3))

        #get three
        def get_three(deck_set):
            return list(three_cards[random.randint(0, len(three_cards)-1)])
        
        #count combinations
        frequency_hand_rank = {}
        for hand_rank in HAND_RANK:
            frequency_hand_rank[hand_rank] = 0
        for i in range(number_of_hands):
            cards = first_two_cards + get_three(deck_set)
            hand_rank, details = PokerHand(cards).get_hand_rank()
            frequency_hand_rank[hand_rank] += 1
        for rank, count in frequency_hand_rank.items():
            frequency_hand_rank[rank] = count/number_of_hands*100.0    
        
        print("\nCONDITION ON GETTING %s first\n" % str(first_two_cards))
        print("With " + str(number_of_hands) + " poker hands dealt")
        print("Poker Hand   Probability")
        for hand, prob in frequency_hand_rank.items():
            print(f"{hand}\t\t{prob:10.4e}")
                          
#4a get probabilities when getting five cards at once

Deck().get_five_cards(number_of_hands = 100000, HAND_RANK = HAND_RANK)            

#4b get conditional hand rank probability, after the first 2 cards are drawn

Deck().conditional_on_two(number_of_hands = 100000, HAND_RANK = HAND_RANK)            




