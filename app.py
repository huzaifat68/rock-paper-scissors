import random


def choose():
    print("\nChoose Rock, Paper, or Scissors.")
    choice = input().lower()
    return choice


def random_choice():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return computer_choice


def compare_choices(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    
    else:
        return "computer"


def play_game():
    your_wins = 0
    computer_wins = 0
    tie = 0
    
    while True:
        player_choice = choose()
        computer_choice = random_choice()
        
        print(f"\nPlayer chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = compare_choices(player_choice, computer_choice)
        
        if result == "player":
            print("\nYou win!")
            your_wins += 1
        elif result == "computer":
            print("\nComputer wins!")
            computer_wins += 1
        else:
            print("\nIt's a tie!")
            tie +=1
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        
        if play_again != "y":

            print(f"\nFinal Score:\n\nPlayer Wins: {your_wins}\nComputer Wins: {computer_wins}\nTie : {tie}")
            print("\nThanks for playing!")
            break


play_game()