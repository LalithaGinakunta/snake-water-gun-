import random
import tkinter as tk
from tkinter import messagebox

def play(choice):
    choices = {"Snake": 1, "Water": -1, "Gun": 0}
    reverse_choices = {1: "Snake", -1: "Water", 0: "Gun"}
    
    computer = random.choice([-1, 0, 1])
    user_choice = choices[choice]
    
    result = ""
    if computer == user_choice:
        result = "It's a Draw!"
    elif (computer == -1 and user_choice == 1) or \
         (computer == 1 and user_choice == 0) or \
         (computer == 0 and user_choice == -1):
        result = "You Win!"
    else:
        result = "You Lose!"
    
    messagebox.showinfo("Result", f"You chose {choice}\nComputer chose {reverse_choices[computer]}\n{result}")

def create_gui():
    root = tk.Tk()
    root.title("Snake Water Gun Game")
    root.geometry("300x300")
    
    tk.Label(root, text="Choose your option:", font=("Arial", 14)).pack(pady=20)
    
    tk.Button(root, text="Snake", font=("Arial", 12), command=lambda: play("Snake")).pack(pady=5)
    tk.Button(root, text="Water", font=("Arial", 12), command=lambda: play("Water")).pack(pady=5)
    tk.Button(root, text="Gun", font=("Arial", 12), command=lambda: play("Gun")).pack(pady=5)
    
    root.mainloop()

create_gui()
