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
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.\n")

    play_again = input("Do you want to toss the coins? (y/n): ").lower()

    while play_again == 'y':
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed: {side1}")
        print(f"{player2.get_name()} tossed: {side2}")

        if side1 == side2: #Match. Player 1 wins a coin.
            player1.win_coin()
            player2.lose_coin()
            print(f"... {player1.get_name()} wins a coin.")
        else: #No match. Player 2 wins a coin.
            player2.win_coin()
            player1.lose_coin()
            print(f"... {player2.get_name()} wins a coin.")
        
        print(f"\n{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.\n")

        if player1.get_wallet() == 0:
            print(f"Game Over! {player1.get_name()} is out of coins.")
            break
        elif player2.get_wallet() == 0:
            print(f"Game Over! {player2.get_name()} is out of coins.")
            break

        play_again = input("Do you want to toss the coins again? (y/n): ").lower()

    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()} coins.")
    print(f"{player2.get_name()}: {player2.get_wallet()} coins.")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins the game!")
    else:
        print("It's a draw !")

if __name__ == "__main__":
    main()