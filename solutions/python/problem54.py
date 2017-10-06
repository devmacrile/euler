# -*- coding: utf-8 -*-
"""
In the card game poker, a hand consists of five cards and are ranked, from 
owest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the 
highest value wins; for example, a pair of eights beats a pair of fives 
(see example 1 below). But if two ranks tie, for example, both players 
have a pair of queens, then highest cards in each hand are compared (see 
example 4 below); if the highest cards tie then the next highest cards are 
compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two 
players. Each line of the file contains ten cards (separated by a single 
space): the first five are Player 1's cards and the last five are Player 2's 
cards. You can assume that all hands are valid (no invalid characters or 
repeated cards), each player's hand is in no specific order, and in each 
hand there is a clear winner.

How many hands does Player 1 win?
"""

import os
from collections import Counter

from eutil import clock


def load_hands():
    datapath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data/')
    with open(datapath + 'poker.txt') as f:
        hands = f.readlines()
    cleaned = [h.strip().split() for h in hands]
    return [(c[:5], c[5:]) for c in cleaned]


def evaluate(hand1, hand2):
    """
    Returns True if hand1 beats hand2 according to
    the rules of poker.

    Hand-checking subprocedures here are not mutually
    exclusive (i.e. if call is_three_of_a_kind on a
    full house hand, True will be returned), and depend
    on their respective ordering (so full house should
    be checked prior to three-of-a-kind, for example).
    """
    rank_map = {'T': 10,
                'J': 11,
                'Q': 12,
                'K': 13,
                'A': 14 }

    def get_rank(card_string):
        if card_string.isdigit():
            return int(card_string)
        else:
            return rank_map.get(card_string)

    def get_suits(hand):
        return [c[1] for c in hand]

    def get_ranks(hand):
        return [get_rank(c[0]) for c in hand]

    def is_full_house(hand):
        ranks = get_ranks(hand)
        ((r1, c1), (r2, c2)) = Counter(ranks).most_common(2)
        return (c1 == 3 and c2 == 2), r1

    def is_pair(hand):
        ranks = get_ranks(hand)
        rank, max_count = Counter(ranks).most_common(1)[0]
        return max_count == 2, rank

    def is_two_pair(hand):
        ranks = get_ranks(hand)
        ((r1, c1), (r2, c2)) = Counter(ranks).most_common(2)
        return (c1 == 2 and c2 == 2), r1

    def is_three_of_a_kind(hand):
        ranks = get_ranks(hand)
        rank, max_count = Counter(ranks).most_common(1)[0]
        return max_count == 3, rank

    def is_four_of_a_kind(hand):
        ranks = get_ranks(hand)
        rank, max_count = Counter(ranks).most_common(1)[0]
        return max_count == 4, rank

    def is_flush(hand):
        return len(set(get_suits(hand))) == 1, max(get_ranks(hand))

    def is_straight_flush(hand):
        return is_straight(hand)[0] and is_flush(hand)[0], max(get_ranks(hand))

    def is_high_straight(hand):
        ranks = get_ranks(hand)
        return is_straight(hand) and \
                min(ranks) == 10 and \
                max(ranks) == 14

    def is_royal_flush(hand):
        return is_high_straight(hand) and is_flush(hand)[0], 14

    def is_straight(hand):
        ranks = get_ranks(hand)
        mod13 = map(lambda x: x % 13, ranks)  # high-low ace
        return (len(set(ranks)) == 5) and \
               (max(ranks) - min(ranks) == 4 or \
                max(mod13) - min(mod13) == 4), sorted(ranks)[-2]

    def score(hand):
        """
        Return primary score (associate with hand type) and
        secondary score (associate with highest card) as a tuple.
        """
        score_funcs = [is_royal_flush,
                       is_straight_flush,
                       is_four_of_a_kind,
                       is_full_house,
                       is_flush,
                       is_straight,
                       is_three_of_a_kind,
                       is_two_pair,
                       is_pair]
        hand_score = 1
        max_rank = max(get_ranks(hand))
        for i, func in enumerate(score_funcs):
            is_hand, high_card = func(hand)
            if is_hand:
                hand_score = 10 - i
                max_rank = high_card
                break
        return (hand_score, max_rank)


    s1, h1 = score(hand1)
    s2, h2 = score(hand2)
    if s1 == s2:
        if h1 >= h2:
            return True
        else:
            return False
    elif s1 > s2:
        return True
    else:
        return False


@clock
def main():
    hands = load_hands()
    wins = 0
    for p1, p2 in hands:
        if evaluate(p1, p2):
            wins += 1
    return wins


if __name__ == '__main__':
    main()
