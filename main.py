# -*- coding: utf-8 -*-
import random
import ctypes
import sys
from pathlib import Path
from tkinter import (
    Tk,
    Canvas,
    Entry,
    PhotoImage,
    END
)

try:
    from PIL import Image, ImageTk
except ImportError:
    Image = None
    ImageTk = None

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")
IMAGE_REFS = []

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def load_photo_image(path: str):
    try:
        image = PhotoImage(file=path)
    except Exception:
        if Image is None or ImageTk is None:
            raise
        image = ImageTk.PhotoImage(Image.open(path))
    IMAGE_REFS.append(image)
    return image

def enable_dpi_awareness():
    if sys.platform != "win32":
        return
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

def center_window(window, width, height):
    window.update_idletasks()
    x = int((window.winfo_screenwidth() - width) / 2)
    y = int((window.winfo_screenheight() - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def find_word():
    try:
        with open("words.txt", "r") as f:
            words = f.read().splitlines()
        clean_words = [w.split("]")[-1].strip().lower() for w in words if w.strip()]
        return random.choice(clean_words)
    except FileNotFoundError:
        return "python"

secret_word = find_word()
guessed_letters = []
attempts = 6

def update_ui():
    current_view = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    canvas.itemconfig(word_display_id, text=current_view)
    
    if "_" not in current_view:
        canvas.itemconfig(attempts_display_id, text="You Win!", fill="#009900")
    elif attempts <= 0:
        canvas.itemconfig(attempts_display_id, text=f"Game Over! Word was: {secret_word}", fill="#FF0000")
    else:
        canvas.itemconfig(attempts_display_id, text=f"Attempts Remaining: {attempts}")

def make_a_guess(event=None):
    global attempts
    if attempts <= 0:
        return
    
    user_guess = entry_1.get().lower().strip()
    entry_1.delete(0, END)

    if not user_guess or len(user_guess) != 1 or not user_guess.isalpha():
        return
    
    if user_guess not in guessed_letters:
        guessed_letters.append(user_guess)
        if user_guess not in secret_word:
            attempts -= 1
            
    update_ui()

def on_key_click(char):
    entry_1.delete(0, END)
    entry_1.insert(0, char)

enable_dpi_awareness()

window = Tk()
window.title("Word Guessing Game")
window.geometry("1052x840")
window.configure(bg="#FFFFFF")
center_window(window, 1052, 840)

<<<<<<< HEAD
window.bind('<Return>', make_a_guess)
=======
        if attempts <= 0:
            return
        
        if user_guess and user_guess not in guessed_letters:
            guessed_letters.append(user_guess)
            if user_guess not in secret_word:
                attempts -= 1
        
        refresh_ui()
>>>>>>> 9dd75547f1736f3cedeb3b957e87a2985ee38a43

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=840,
    width=1052,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

try:
    image_image_1 = load_photo_image(relative_to_assets("element_1.png"))
    image_1 = canvas.create_image(526.0, 420.0, image=image_image_1)
except Exception:
    pass

canvas.create_rectangle(
    387.0, 697.0, 667.0, 774.0,
    fill="#000000", outline="", tags="guess_btn"
)
canvas.create_text(
    423.0, 711.0, anchor="nw",
    text="Guess Letter", fill="#FFFFFF",
    font=("Roboto", 36 * -1, "normal", "roman"), tags="guess_btn"
)
canvas.tag_bind("guess_btn", "<Button-1>", make_a_guess)

attempts_display_id = canvas.create_text(
    403.0, 209.0, anchor="nw",
    text=f"Attempts Remaining: {attempts}",
    fill="#1E1E1E", font=("Inter", 24 * -1, "bold", "roman")
)

try:
    entry_image_1 = load_photo_image(relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(527.5, 314.5, image=entry_image_1)
except Exception:
    pass

entry_1 = Entry(
    window, bd=0, bg="#E0D9D9", fg="#000716",
    insertbackground="#000716", highlightthickness=0,
    font=("Roboto", 28), justify="center"
)
entry_1.place(x=476.0, y=271.0, width=103.0, height=85.0)

def create_key(x1, y1, x2, y2, tx, ty, char):
    canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFBEB", outline="", tags=f"key_{char}")
    canvas.create_text(tx, ty, anchor="nw", text=char, fill="#1E1E1E", font=("Roboto", 24 * -1), tags=f"key_{char}")
    canvas.tag_bind(f"key_{char}", "<Button-1>", lambda e, c=char: on_key_click(c))

create_key(104.0, 396.0, 181.0, 472.0, 133.86, 418.0, "Q")
create_key(191.27, 396.0, 268.27, 472.0, 218.36, 418.0, "W")
create_key(278.55, 396.0, 355.55, 472.0, 309.36, 418.0, "E")
create_key(364.83, 396.0, 441.83, 472.0, 395.86, 418.0, "R")
create_key(452.11, 396.0, 529.11, 472.0, 482.86, 418.0, "T")
create_key(539.39, 396.0, 616.39, 472.0, 569.86, 418.0, "Y")
create_key(626.67, 396.0, 703.67, 472.0, 656.36, 418.0, "U")
create_key(712.95, 396.0, 789.95, 472.0, 747.86, 418.0, "I")
create_key(800.23, 396.0, 877.23, 472.0, 829.86, 418.0, "O")
create_key(887.51, 396.0, 964.51, 472.0, 917.36, 418.0, "P")

create_key(143.0, 490.0, 220.0, 566.0, 173.36, 512.0, "A")
create_key(229.0, 490.0, 306.0, 566.0, 259.58, 512.0, "S")
create_key(315.0, 490.0, 392.0, 566.0, 344.80, 512.0, "D")
create_key(400.0, 490.0, 477.0, 566.0, 431.52, 512.0, "F")
create_key(486.0, 490.0, 563.0, 566.0, 515.74, 512.0, "G")
create_key(572.0, 490.0, 649.0, 566.0, 600.96, 512.0, "H")
create_key(658.0, 490.0, 735.0, 566.0, 688.68, 512.0, "J")
create_key(743.0, 490.0, 820.0, 566.0, 773.40, 512.0, "K")
create_key(829.0, 490.0, 906.0, 566.0, 860.62, 512.0, "L")

create_key(229.0, 584.0, 306.0, 660.0, 259.58, 606.0, "Z")
create_key(315.0, 584.0, 392.0, 660.0, 344.80, 606.0, "X")
create_key(400.0, 584.0, 477.0, 660.0, 430.52, 606.0, "C")
create_key(486.0, 584.0, 563.0, 660.0, 516.24, 606.0, "V")
create_key(572.0, 584.0, 649.0, 660.0, 602.46, 606.0, "B")
create_key(658.0, 584.0, 735.0, 660.0, 686.68, 606.0, "N")
create_key(743.0, 584.0, 820.0, 660.0, 770.90, 606.0, "M")

initial_view = " ".join(["_" for _ in secret_word])
word_display_id = canvas.create_text(
    143.0,
    82.0,
    anchor="nw",
    text=initial_view,
    fill="#000000",
    font=("Roboto", 80 * -1, "normal", "roman")
)

window.resizable(False, False)

if __name__ == "__main__":
    window.mainloop()