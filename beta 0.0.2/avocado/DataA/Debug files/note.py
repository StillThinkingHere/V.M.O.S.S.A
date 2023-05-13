import tkinter as tk
from datetime import datetime
root = tk.Tk()
root.geometry("800x600")
wallpaper = tk.Canvas(root, bg="light blue")
wallpaper.pack(fill="both", expand=True)
icon1 = tk.Button(wallpaper, text="My Computer")
icon1.grid(row=0, column=0, padx=10, pady=10)
icon2 = tk.Button(wallpaper, text="Recycle Bin")
icon2.grid(row=0, column=1, padx=10, pady=10)
icon3 = tk.Button(wallpaper, text="My Documents")
icon3.grid(row=0, column=2, padx=10, pady=10)
taskbar = tk.Frame(root, bg="white")
taskbar.pack(side="bottom", fill="x")


def update_clock():
    current_time = datetime.now().strftime("%m/%d/%Y %I:%M %p")
    clock.config(text=current_time)
    root.after(1000, update_clock)


clock = tk.Label(taskbar, bg="white", font=("Arial", 12))
clock.pack(side="right", padx=10)
update_clock()
root.mainloop()
