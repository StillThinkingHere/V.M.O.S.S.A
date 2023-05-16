from plyer import notification
import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
from tkinter import filedialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

    
def Pass_change():
    def changes():
        def change():
            next_changer.destroy()
            print("Done")
        changer.destroy()
        next_changer = tk.Tk()
        login_frame = tk.Frame(next_changer, bd=2, relief=tk.RIDGE)
        login_frame.pack(padx=10, pady=10)

        # Add login fields
        username_label = tk.Label(login_frame, text="New Username:")
        username_label.pack(padx=5, pady=5)
        username_entry = tk.Entry(login_frame)
        username_entry.pack(padx=5, pady=5)
        password_label = tk.Label(login_frame, text="New Password:")
        password_label.pack(padx=5, pady=5)
        password_entry = tk.Entry(login_frame, show="*")
        password_entry.pack(padx=5, pady=5)

        login_button = tk.Button(login_frame, text="Save", command=change)
        login_button.pack(padx=5, pady=5)
            
        next_changer.mainloop()
    changer = tk.Tk()
    login_frame = tk.Frame(changer, bd=2, relief=tk.RIDGE)
    login_frame.pack(padx=10, pady=10)

    # Add login fields
    username_label = tk.Label(login_frame, text="Current Username:")
    username_label.pack(padx=5, pady=5)
    username_entry = tk.Entry(login_frame)
    username_entry.pack(padx=5, pady=5)
    password_label = tk.Label(login_frame, text="Current Password:")
    password_label.pack(padx=5, pady=5)
    password_entry = tk.Entry(login_frame, show="*")
    password_entry.pack(padx=5, pady=5)

    login_button = tk.Button(login_frame, text="Next", command=changes)
    login_button.pack(padx=5, pady=5)
        
    changer.mainloop()
Pass_change()