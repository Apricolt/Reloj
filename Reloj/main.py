import tkinter as tk
import math
from Clock import Clock
from datetime import datetime
from tkinter import colorchooser

# Setting up the main window for the interface
window = tk.Tk()
window.title("Retro Analog Clock")
window.geometry("400x500")

# Function to choose a background color using the color chooser
def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        window.config(bg=color)

# Button to select the background color
color_button = tk.Button(window, text="Choose Background Color", command=choose_color, font=("Courier", 12))
color_button.pack(pady=10)

# Canvas for the analog clock
canvas = tk.Canvas(window, width=400, height=400, bg="black", highlightthickness=0)
canvas.pack()

# Initializing the Clock class to control the time
clock = Clock()

# Label for the digital clock
digital_clock = tk.Label(window, text="", font=("Courier", 24), fg="black", bg="white")
digital_clock.pack(pady=10)

# Draws the main numbers on the analog clock
def draw_numbers():
    # Positions of the numbers on the clock
    positions = {
        12: (200, 70),
        3: (320, 200),
        6: (200, 330),
        9: (80, 200)
    }

    # Roman numerals for a retro style
    roman_numerals = {
        12: "XII",
        3: "III",
        6: "VI",
        9: "IX"
    }

    # Draw each number at the designated position
    for number, (x, y) in positions.items():
        canvas.create_text(x, y, text=roman_numerals[number], fill="black", font=("Courier", 18))

# Updates the position of the clock hands and the digital clock
def update_clock():
    clock.tick()
    
    # Update the time on the digital clock
    now = datetime.now()
    digital_time = now.strftime("%H:%M:%S")
    digital_clock.config(text=digital_time)
    
    # Clear the previous hands
    canvas.delete("hands")
    
    # Draw the hour, minute, and second hands
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    draw_hand(hour * 30, 80, "black")   # Hour hand in black
    draw_hand(minute * 6, 120, "black")  # Minute hand in black
    draw_hand(second * 6, 140, "red")     # Second hand in red

    # Call the function again after 1000 ms
    window.after(1000, update_clock)

# Draws a hand at the specified angle and color
def draw_hand(angle, length, color):
    angle = math.radians(angle - 90)
    x = 200 + length * math.cos(angle)
    y = 200 + length * math.sin(angle)
    canvas.create_line(200, 200, x, y, width=4, fill=color, tags="hands")

# Draws the clock outline
canvas.create_oval(50, 50, 350, 350, outline="black", width=6)  # Black outline
canvas.create_oval(55, 55, 345, 345, fill="white")  # White background

# Draws the numbers on the clock
draw_numbers()

# Starts the clock update
update_clock()
window.mainloop()
