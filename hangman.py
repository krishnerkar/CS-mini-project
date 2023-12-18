import tkinter as tk
from tkinter import messagebox
import random


def main():
# Define the list of words
    global guesses  # Declare guesses as a global variable
    global guessed_letters
    words = ["The Shawshank Redemption","The Godfather","The Dark Knight","Pulp Fiction","Forrest Gump","Inception","The Matrix","The Lord of the Rings",
            "Star Wars","Jurassic Park","Titanic","Avatar","The Silence of the Lambs","Fight Club","The Avengers",
            "Gladiator","The Lion King","The Dark Knight Rises","Inglourious Basterds","The Departed","Saving Private Ryan","The Prestige",
            "The Green Mile","The Usual Suspects","The Sixth Sense","The Terminator","Goodfellas","The Social Network","Back to the Future","The Shining","The Exorcist","Psycho","The Breakfast Club","The Grand Budapest Hotel",
            "Interstellar","The Incredibles","Blade Runner","The Princess Bride","A Clockwork Orange","Reservoir Dogs","The Revenant","Toy Story","Die Hard","Whiplash","The Truman Show","Casablanca","The Sound of Music","Jaws","Fargo","The Graduate","Gone with the Wind",
            "La La Land","The Wizard of Oz","Rocky","The Great Gatsby","The Bridge on the River Kwai","Lawrence of Arabia","Gravity","No Country for Old Men",
            "Million Dollar Baby","The Big Lebowski","The Maltese Falcon","Chinatown","The Hustler","Network","Trainspotting","Heat","Gone Girl","The Martian","The Shawshank Redemption","The Godfather","The Dark Knight","Pulp Fiction","Forrest Gump"]


    # Choose a random word from the list
    word1 = random.choice(words)
    word=word1.lower()
    # Initialize the number of guesses and the list of guessed letters
    guesses = 6
    guessed_letters = []


    # Create the main window
    root = tk.Tk()
    root.title("Hangman")

    # Create the canvas for drawing the hangman
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.grid(column=0, row=0)

    # Draw the scaffold
    canvas.create_line(20, 280, 120, 280)
    canvas.create_line(70, 280, 70, 20)
    canvas.create_line(70, 20, 170, 20)
    canvas.create_line(170, 20, 170, 50)

    # Create a label for displaying the word
    word_label = tk.Label(root, text=" ".join(["_" for letter in word]))
    word_label.grid(column=0, row=1)

    # Create a label for displaying the number of guesses remaining
    guesses_label = tk.Label(root, text="Guesses remaining: {}".format(guesses))
    guesses_label.grid(column=0, row=2)

    # Create a label for displaying the letters guessed so far
    guessed_label = tk.Label(root, text="Guessed letters: ")
    guessed_label.grid(column=0, row=3)

    # Create an entry for the user to guess a letter
    guess_entry = tk.Entry(root)
    guess_entry.grid(column=0, row=4)
    # Define a function to check the user's guess
    def check_guess():
        global guesses  # Declare guesses as a global variable
        global guessed_letters
        guess = guess_entry.get()
        guess_entry.delete(0, tk.END)

        # Declare guessed_letters as global before usage

        # Check if the guess is a single letter
        if len(guess) != 1:
            return

        if guess.isdigit():
            return

        # Check if the guess has already been guessed
        if guess in guessed_letters:
            return

        guessed_letters.append(guess)
        guessed_label.config(text="Guessed letters: {}".format(" ".join(guessed_letters)))

        # Check if the guess is in the word
        if guess in word:
            word_list = list(word_label["text"])
            for i in range(len(word)):
                if word[i]== guess:
                    word_list[i*2] = guess
            word_label.config(text="".join(word_list))

            # Check if the user has won
            if "_" not in word_list:
                #make popup saying wrong
                messagebox.showinfo("Hangman", "You win!")
                retry_button.grid(column=0, row=5)
                exit_button.grid(column=0, row=6)
                guess_entry.config(state=tk.DISABLED)
                return

        # If the guess is not in the word, decrement the number of guesses remaining
        else:
            guesses -= 1
            guesses_label.config(text="Guesses remaining: {}".format(guesses))

            # Draw the hangman
            if guesses == 5:
                canvas.create_oval(140, 50, 200, 110)
            elif guesses == 4:
                canvas.create_line(170, 110, 170, 170)
            elif guesses == 3:
                canvas.create_line(170, 130, 140, 140)
            elif guesses == 2:
                canvas.create_line(170, 130, 200, 140)
            elif guesses == 1:
                canvas.create_line(170, 170, 140, 190)
            elif guesses == 0:
                canvas.create_line(170, 170, 200, 190)
                messagebox.showinfo("Hangman", "You lose! The word was '{}'".format(word))
                retry_button.grid(column=0, row=5)
                exit_button.grid(column=0, row=6)
                guess_entry.config(state=tk.DISABLED)

    def retry_game():
        word = random.choice(words)
        guesses = 6
        guessed_letters = []

        word_label.config(text=" ".join(["_" for letter in word]))
        guesses_label.config(text="Guesses remaining: {}".format(guesses))
        guessed_label.config(text="Guessed letters: ")
        guess_entry.config(state=tk.NORMAL)
        canvas.delete("all")
        canvas.create_line(20, 280, 120, 280)
        canvas.create_line(70, 280, 70, 20)
        canvas.create_line(70, 20, 170, 20)
        canvas.create_line(170, 20, 170, 50)
        retry_button.grid_forget()
        exit_button.grid_forget()

    def exit_game():
        root.destroy()

    retry_button = tk.Button(root, text="Retry", command=retry_game)

    exit_button = tk.Button(root, text="Exit", command=exit_game)

    root.bind("<Return>", lambda event: check_guess())

    root.mainloop()


if __name__ == "__main__":
    main()