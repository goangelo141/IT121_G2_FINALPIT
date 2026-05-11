import random
import tkinter as tk

def play_game():
    words = ['python', 'programming', 'adventure', 'algorithm', 'developer', 'keyboard']
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    window = tk.Tk()
    window.title("Project - Word Game")
    window.geometry("500x400")

    word_display = tk.Label(window, text="", font=("Arial", 20))
    word_display.pack(pady=20)

    info_label = tk.Label(window, text=f"Attempts: {attempts}")
    info_label.pack()

    input_box = tk.Entry(window)
    input_box.pack(pady=10)

    def refresh_ui():
        current_view = ""
        for letter in secret_word:
            if letter in guessed_letters:
                current_view += letter + " "
            else:
                current_view += "_ "
        word_display.config(text=current_view)
        info_label.config(text=f"Attempts remaining: {attempts}")

    def submit_action():
        nonlocal attempts
        user_guess = input_box.get().lower()
        input_box.delete(0, tk.END)

        if user_guess and user_guess not in guessed_letters:
            guessed_letters.append(user_guess)
            if user_guess not in secret_word:
                attempts -= 1
        
        refresh_ui()

    btn_guess = tk.Button(window, text="Guess Letter", command=submit_action)
    btn_guess.pack()

    refresh_ui()
    window.mainloop()

play_game()