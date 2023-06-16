import tkinter as tk
from tkinter import messagebox

def check_guess():
    global guess_count
    guess = int(guess_entry.get())
    guess_count += 1
    
    if guess == secret_number:
        messagebox.showinfo("Result", "Congratulations! You guessed it right!")
        window.quit()  # Exit the GUI event loop
    elif guess_count == guess_limit:
        messagebox.showinfo("Result", "Sorry, you've reached the maximum number of guesses.")
        window.quit()  # Exit the GUI event loop
    else:
        messagebox.showinfo("Result", "Sorry, wrong guess. Try again.")

    guess_entry.delete(0, tk.END)  # Clear the guess entry field

# Create the main window
window = tk.Tk()
window.title("Guessing Game")
window.geometry("600x400")
window.configure(bg="#E0E0E0")


# Set up labels and entry field
name_label = tk.Label(window, text="What's your name:", bg="#E0E0E0", font=("Arial", 14))
name_label.pack(pady=10)
name_entry = tk.Entry(window, font=("Arial", 14))
name_entry.pack()

instructions_label = tk.Label(window, text="Instructions:", bg="#E0E0E0", font=("Arial", 14))
instructions_label.pack(pady=10)
instruction1_label = tk.Label(window, text="1. Guess a number between 0 and 9", bg="#E0E0E0", font=("Arial", 14))
instruction1_label.pack()
instruction2_label = tk.Label(window, text="2. You can only guess three times", bg="#E0E0E0", font=("Arial", 14))
instruction2_label.pack()

guess_label = tk.Label(window, text="Guess:", bg="#E0E0E0", font=("Arial", 14))
guess_label.pack(pady=10)
guess_entry = tk.Entry(window, font=("Arial", 14))
guess_entry.pack()

# Set up the check button
check_button = tk.Button(window, text="Check", command=check_guess, bg="#4CAF50", fg="white", font=("Arial", 14))
check_button.pack(pady=20)

# Define game variables
secret_number = 8
guess_count = 0
guess_limit = 3



# Start the GUI event loop
window.mainloop()