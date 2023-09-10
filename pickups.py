import tkinter as tk
import random

def impress_crush():
    pickup_lines = [
    "Do you have a map? I keep getting lost in your eyes.",
    "Is your name Google? Because you have everything I've been searching for.",
    "Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Excuse me, but I think you dropped something: my jaw.",
    "Is your dad a baker? Because you're a cutie pie!",
    "Do you believe in love at first sight, or should I walk by again?",
    "If you were a vegetable, you'd be a cute-cumber.",
    "Do you have a Band-Aid? I just scraped my knee falling for you.",
    "Are you a camera? Because every time I look at you, I smile.",
    "Is your name Wi-Fi? Because I'm really feeling a connection.",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is your name Cinderella? Because when I see you, everything becomes magical.",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "Is your name Honey? Because you're so sweet.",
    "Do you have a quarter? Because I want to call my mom and tell her I met the love of my life.",
    "Is your name Angel? Because you're out of this world.",
    "Do you have a sunburn, or are you always this hot?",
    "Is your dad an artist? Because you're a masterpiece.",
    "Do you believe in fate? Because I think we were meant to meet.",
    "Is your name Rose? Because you're as beautiful as a flower.",
    "Do you have a name, or can I call you mine?",
    "Is your name Luna? Because you're the moon of my life.",
    "Do you have a twin? No? Then you must be the most beautiful person in the world.",
    "Is your name Autumn? Because you're a real leaf-turner.",
    "Do you have a name, or can I call you mine?",
    "Is your name Luna? Because you're the moon of my life.",
    "Do you have a twin? No? Then you must be the most beautiful person in the world.",
    "Is your name Autumn? Because you're a real leaf-turner.",
    "Do you have a name, or can I call you mine?",
    "Is your name Luna? Because you're the moon of my life.",
    "Do you have a twin? No? Then you must be the most beautiful person in the world.",
    "Is your name Autumn? Because you're a real leaf-turner.",
    "Do you have a name, or can I call you mine?",
    "Is your name Luna? Because you're the moon of my life.",
    "Do you have a twin? No? Then you must be the most beautiful person in the world.",
    "Is your name Autumn? Because you're a real leaf-turner.",
    
]
    
    pickup_line = random.choice(pickup_lines)
    label.config(text=pickup_line)

# Create the main window
window = tk.Tk()
window.title("Howdy, Babe!")
window.geometry("500x100")

# Create a label to display the pickup lines
label = tk.Label(window, text="Click the button for a romantic pickup line!")
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="CLick ME", command=impress_crush)
button.pack()

# Start the main event loop
window.mainloop()
