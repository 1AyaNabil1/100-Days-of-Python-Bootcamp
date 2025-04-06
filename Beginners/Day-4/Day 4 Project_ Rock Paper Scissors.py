rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
import time

# List of options
options = [rock, paper, scissors]
# Display the options to the user
print("Welcome to Rock, Paper, Scissors!")
print("Choose your option:")
print("0: Rock")
print("1: Paper")
print("2: Scissors")
# Get the user's choice
user_choice = int(input("Enter your choice (0, 1, or 2): "))
# Validate the user's choice
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
else:
    # Display the user's choice
    print("You chose:")
    print(options[user_choice])
    # Generate a random choice for the computer
    computer_choice = random.randint(0, 2)
    time.sleep(1)
    # Display the computer's choice
    print("Computer chose:")
    print(options[computer_choice])
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == 0 and computer_choice == 2)
        or (user_choice == 1 and computer_choice == 0)
        or (user_choice == 2 and computer_choice == 1)
    ):
        print("You win!")
    else:
        print("You lose!")
