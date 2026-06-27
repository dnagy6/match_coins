"""
Program Name: Match Coins Game
Author: Dakota Nagy
Purpose: Executes the main game logic for the Match Coins Game, allowing two players to 
compete by tossing their coins and determining a winner based on matching outcomes.
Date: 07/28/2026

"""

from player import Player

def main():
    print("--- COIN MATCH GAME ---")
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play_again = input("Do you want to toss the coins? (y/n): ").lower()

    