import tkinter as tk
from tkinter import messagebox
import os

# Import game modules
import tic_tac_toe 
import gamegui
import hangman
import rock_paper_scissors


def open_game(game_function):
    try:
        game_function()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def main_screen():
    root = tk.Tk()
    root.title("Game Hub")

    # Fullscreen setup
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda event: root.destroy())

    # Buttons for each game
    tk.Button(root, text="Tic Tac Toe", command=lambda: open_game(
        tic_tac_toe.main), height=5, width=20).pack(pady=20)
    tk.Button(root, text="Connect 4", command=lambda: open_game(
        gamegui.main), height=5, width=20).pack(pady=20)
    tk.Button(root, text="Hangman", command=lambda: open_game(
        hangman.main), height=5, width=20).pack(pady=20)
    tk.Button(root, text="Rock Paper Scissors", command=lambda: open_game(
        rock_paper_scissors.main), height=5, width=20).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main_screen()
