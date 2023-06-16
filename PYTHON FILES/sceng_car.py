import tkinter as tk

def start_car():
    global started, direction
    if started:
        status_label.config(text="Car is already started!")
    else:
        started = True
        status_label.config(text="Car started...")
        move_car()

def stop_car():
    global started
    if not started:
        status_label.config(text="Car is already stopped!")
    else:
        started = False
        status_label.config(text="Car stopped.")

def move_car():
    global car_image
    if started:
        if direction == "forward":
            canvas.move(car_image_item, 5, 0)
        else:
            canvas.move(car_image_item, -5, 0)
        root.after(50, move_car)

def reverse_car():
    global direction
    if started:
        if direction == "forward":
            direction = "reverse"
            status_label.config(text="Car in reverse.")
        else:
            direction = "forward"
            status_label.config(text="Car moving forward.")

root = tk.Tk()
root.title("Sceng Car Game")

started = False
direction = "forward"

# Create GUI elements
status_label = tk.Label(root, text="Car is stopped.", font=("Arial", 16))
canvas = tk.Canvas(root, width=800, height=500)

# Car representation
car_image_file = r"C:\Users\user\Desktop\PYTHON FILES\sceng_car.png"
car_image = None  # Placeholder for car image
car_image_item = None  # Placeholder for car image item

def load_car_image():
    global car_image, car_image_item
    car_image = tk.PhotoImage(file=car_image_file)
    car_image_item = canvas.create_image(100, 300, image=car_image)

load_car_image()  # Load the car image initially

start_button = tk.Button(root, text="Start Car", command=start_car)
stop_button = tk.Button(root, text="Stop Car", command=stop_car)
reverse_button = tk.Button(root, text="Reverse", command=reverse_car)
quit_button = tk.Button(root, text="Quit", command=root.quit)

# Grid layout
status_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
canvas.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
start_button.grid(row=2, column=0, padx=10, pady=10)
stop_button.grid(row=2, column=1, padx=10, pady=10)
reverse_button.grid(row=2, column=2, padx=10, pady=10)
quit_button.grid(row=2, column=3, padx=10, pady=10)

root.mainloop()
