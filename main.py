import tkinter as tk
from tkinter import messagebox

def show_info():
    name = "John Smith"
    address = "123 Placeholder Avenue"
    messagebox.showinfo("Information", f"Name: {name}\nAddress: {address}")

def quit_program():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

# Create the main window
window = tk.Tk()
window.title("Information Program")

# Create a button to show the info
info_button = tk.Button(window, text="Show Info", command=show_info)
info_button.pack(pady=20)

# Create a button to quit the program
quit_button = tk.Button(window, text="Quit", command=quit_program)
quit_button.pack()

# Start the main loop
window.mainloop()
