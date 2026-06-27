"""
Program Name: Match Coins Game
Author: Dakota Nagy
Purpose: Defines the Coin class to represent a single, tossable coin that tracks its own state of Heads or Tails.
Date: 07/28/2026

"""

import random

class Coin:
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        flip_result = random.randint(0, 1)
        if flip_result == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    
    def get_sideup(self):
        return self.__sideup