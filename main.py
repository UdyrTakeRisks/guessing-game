import tkinter as tk
import random
from tkinter import messagebox


generated_number = random.randint(1, 100)


def open_popup():
    win_msg = tk.Toplevel(master=window)
    win_msg.title("Congratulations")
    win_msg.geometry("400x120")

    label_msg = tk.Label(master=win_msg, text="YOU WON!")
    label_msg.pack(pady=20, padx=20)

    btn_restart = tk.Button(
        master=win_msg, text="Restart Game", command=win_msg.destroy
    )
    btn_restart.pack(pady=10)

    global generated_number
    generated_number = random.randint(1, 100)


def guess_number():
    guessed_number = enter_guess.get()
    guessed_number_int = int(guessed_number)
    print(guessed_number_int, generated_number)

    if guessed_number_int < generated_number:
        guess_res_label["text"] = "Your number is too low!"
    elif guessed_number_int > generated_number:
        guess_res_label["text"] = "Your number is too high!"
    else:
        # messagebox.showinfo('Information', 'YOU WON!')
        guess_res_label["text"] = ""
        enter_guess.delete(0, tk.END)
        open_popup()


window = tk.Tk()
window.title("Guessing Game")
window.minsize(width=400, height=100)


frame_entry = tk.Frame(master=window)
enter_guess = tk.Entry(master=frame_entry, width=10)
guess_label = tk.Label(master=frame_entry, text="Enter Your Guess [1-100]: ")


guess_label.grid(row=0, column=0)
enter_guess.grid(row=0, column=2, sticky="e")

# button
btn_enter = tk.Button(
    master=window,
    text="Enter Guess",
    command=guess_number
)

# result
guess_res_label = tk.Label(master=window)


frame_entry.grid(row=0, column=1, padx=85, pady=10)
btn_enter.grid(row=2, column=1)
guess_res_label.grid(row=4, column=1)


window.mainloop()
