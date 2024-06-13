import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    play_again = tk.messagebox.askyesno("Play Again", "Do you want to play another round?")
    if play_again:
        result_label.config(text="")
    else:
        root.destroy()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")

instructions_label = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Arial", 14))
instructions_label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", font=("Arial", 12), command=lambda: play_game("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", font=("Arial", 12), command=lambda: play_game("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 12), command=lambda: play_game("scissors"))
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
