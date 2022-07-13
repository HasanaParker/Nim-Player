""""
Hasana Parker & Elly Rokeach
CS51A: Assignment 11
April 18th, 2022
                                                      NimGame
"""
from nimsupport import *
import random

# TeamName:
# Name??

"""
Writeup:

2–3 paragraphs as a multiline string at the top of your file. You should discuss two things: 1) a
description of your player’s strategy and 2) how you came to that strategy. For the second part of
this question, you should discuss what are the other things you tried, experiments you ran, etc.

"""


def nim_strategy(piles):
    num_piles = len(piles)
    piles_greater_than_zero = 0
    pile_number = 0
    num_to_move = 0

    for num in range(num_piles):
        if piles[num] > 0:
            piles_greater_than_zero += 1

    if piles_greater_than_zero > 3:
        for num in range(num_piles):
            if piles[num] > 1:
                pile_number = num
                num_to_move = piles[num]

    elif piles_greater_than_zero == 1:
        for num in range(num_piles):
            if piles[num] >= 1:
                pile_number = num
                num_to_move = piles[num]

    elif piles_greater_than_zero <= 3:
        list_of_piles = []
        for num in range(num_piles):
            if piles[num] >= 1:
                list_of_piles.append(num)
                pile_number = random.choice(list_of_piles)
                num_to_move = 1

    move_to_make = (pile_number, num_to_move)

    return move_to_make


# play_nim(human_player, nim_strategy, NimGame([100] * 10))

# play_nim(nim_strategy, random_nim_strategy, NimGame([10]*5))

