import pyautogui
import time
import keyboard
import customtkinter as ctk
from tkinter import messagebox

# CustomTkinter Settings
ctk.set_appearance_mode("dark")  # Dark theme
ctk.set_default_color_theme("green")  # Green highlights

# Send Message Function
def start():
    global message
    message = message_entry.get()
    messagebox.showinfo("Info", "Your messages will be sent in 10 seconds.\nPress 'q' to stop.")
    time.sleep(10)
    
    while True:
        if keyboard.is_pressed('q'):
            print("Loop stopped.")
            messagebox.showinfo("Info", "Message sending process has been stopped!")
            break
        pyautogui.write(message)
        pyautogui.press("enter")
        time.sleep(0.1)

# Close Animation
def close_animation():
    for i in range(100, 0, -5):  # Decrease opacity
        root.attributes("-alpha", i / 100)
        root.update()
        time.sleep(0.02)
    root.destroy()

# Open Animation
def open_animation():
    root.attributes("-alpha", 0)
    for i in range(0, 101, 5):  # Increase opacity
        root.attributes("-alpha", i / 100)
        root.update()
        time.sleep(0.02)

# Main Window
root = ctk.CTk()
root.title("Auto Message Spam Bot")
root.attributes("-fullscreen", True)  # Auto Fullscreen
root.bind("<Escape>", lambda e: close_animation())  # Close with ESC

# Start opening animation
open_animation()

# Main Frame
frame = ctk.CTkFrame(root, corner_radius=20)
frame.pack(expand=True, padx=40, pady=40)

# Title
title_label = ctk.CTkLabel(frame, text="Message Spam Bot", font=("Arial", 26, "bold"))
title_label.pack(pady=20)

# Message entry box
message_entry = ctk.CTkEntry(frame, placeholder_text="Enter your message...", font=("Arial", 20), width=400, height=50)
message_entry.pack(pady=10)

# Start Button
send_button = ctk.CTkButton(frame, text="Start", command=start, font=("Arial", 20), width=250, height=50, corner_radius=10)
send_button.pack(pady=20)

# Exit Button
exit_button = ctk.CTkButton(frame, text="Exit", command=close_animation, font=("Arial", 20), fg_color="red", width=250, height=50, corner_radius=10)
exit_button.pack(pady=10)

# Footer (Made by em41py)
footer_label = ctk.CTkLabel(root, text="Made by em41py", font=("Arial", 24), text_color="gray")
footer_label.place(relx=0.5, rely=0.95, anchor="center")

root.mainloop()
