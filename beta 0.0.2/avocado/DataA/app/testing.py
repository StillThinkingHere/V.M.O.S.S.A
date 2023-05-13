from plyer import notification
import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
from tkinter import filedialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import shutil
import pyperclip
import smtplib
ttt = "©2023 Avocado - https://ionalegoman.wixsite.com/Avocado Verson = Beta 0.0.0 Update name = Pre release Verson 1 creator = Iona .M Code Editor = Iona .M  Code Editor Graphics = Dalle and Iona Sound Effects = Iona .M Sound Effects Cash Debug = Cash 1 = WNUM (Welcome new user message) true = Message show False = Message show False Cash 2 = UN (Username) TextExample Cash 3 = UP (User password) TextExample Cash 4 = CAPD (Copy All Program Data) TextExample Cash 5 - Cash 26 = NCV (No Cash Varuble) Default Ram 1 - Ram 3 = NCV (No Ram Varuble) Default"
pit0 = open("DataA\\app\\Pits\\Pit - a1\\Pit-000.txt", "r")
pit1 = open("DataA\\app\\Pits\\Pit - a1\\Pit-001.txt", "r")
pit2 = open("DataA\\app\\Pits\\Pit - a1\\Pit-002.txt", "r")
pit3 = open("DataA\\app\\Pits\\Pit - a1\\Pit-003.txt", "w")
pit4 = open("DataA\\app\\Pits\\Pit - a1\\Pit-004.txt", "w")
pit5 = open("DataA\\app\\Pits\\Pit - a1\\Pit-005.txt", "w")
pit6 = open("DataA\\app\\Pits\\Pit - a1\\Pit-006.txt", "w")
pit7 = open("DataA\\app\\Pits\\Pit - a1\\Pit-007.txt", "w")
pit8 = open("DataA\\app\\Pits\\Pit - a1\\Pit-008.txt", "w")
pit9 = open("DataA\\app\\Pits\\Pit - a1\\Pit-009.txt", "w")
pit10 = open("DataA\\app\\Pits\\Pit - a1\\Pit-010.txt", "w")
pit11 = open("DataA\\app\\Pits\\Pit - a1\\Pit-011.txt", "w")
pit12 = open("DataA\\app\\Pits\\Pit - a1\\Pit-012.txt", "w")
pit13 = open("DataA\\app\\Pits\\Pit - a1\\Pit-013.txt", "w")
pit14 = open("DataA\\app\\Pits\\Pit - a1\\Pit-014.txt", "w")
pit15 = open("DataA\\app\\Pits\\Pit - a1\\Pit-015.txt", "w")
pit16 = open("DataA\\app\\Pits\\Pit - a1\\Pit-016.txt", "w")
pit17 = open("DataA\\app\\Pits\\Pit - a1\\Pit-017.txt", "w")
pit18 = open("DataA\\app\\Pits\\Pit - a1\\Pit-018.txt", "w")
pit19 = open("DataA\\app\\Pits\\Pit - a1\\Pit-019.txt", "w")
pit20 = open("DataA\\app\\Pits\\Pit - a1\\Pit-020.txt", "w")
pit21 = open("DataA\\app\\Pits\\Pit - a1\\Pit-021.txt", "w")
pit22 = open("DataA\\app\\Pits\\Pit - a1\\Pit-022.txt", "w")
pit23 = open("DataA\\app\\Pits\\Pit - a1\\Pit-023.txt", "w")
pit24 = open("DataA\\app\\Pits\\Pit - a1\\Pit-024.txt", "w")
pit25 = open("DataA\\app\\Pits\\Pit - a1\\Pit-025.txt", "w")
pit26 = open("DataA\\app\\Pits\\Pit - a1\\Pit-026.txt", "w")
ram1 = open("DataA\\app\\Pits\\RAM\\RAM-address-1.txt", "w")
ram2 = open("DataA\\app\\Pits\\RAM\\RAM-address-2.txt", "w")
ram3 = open("DataA\\app\\Pits\\RAM\\RAM-address-3.txt", "w")


def Pyterm():
    class Terminal(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.textbox = tk.Text(self, wrap=tk.WORD)
            self.textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.scrollbar = tk.Scrollbar(self)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.textbox.config(yscrollcommand=self.scrollbar.set)
            self.scrollbar.config(command=self.textbox.yview)

            self.textbox.config(bg="black", fg="white")
            self.textbox.insert(
                tk.END, "Enter code here\nfunctions:\n         callcode / writefile / help / readfile\n")

            self.textbox.bind("<Key>", self.handle_keypress)

            # configure tag for system output
            self.textbox.tag_config(
                "system", foreground="red", font=("Arial", 10, "bold"))

        def handle_keypress(self, event):
            if event.char == "\r":
                self.handle_input()
            else:
                pass

        def handle_input(self):
            input_text = self.textbox.get("end-2l linestart", "end-1c")
            input_line = input_text.split("\n")[-1]
            if not input_line:
                self.textbox.insert(tk.END, "\n")
            elif input_line.startswith("callcode"):
                self.textbox.insert(
                    tk.END, "\nThis is a call for a function that doesn't exist!")

            elif input_line == "help":
                self.textbox.insert(
                    tk.END, "\n\nfunctions:\n         callcode / writefile / help / readfile\nmore information about these functions will be at:\n   https://ionalegoman.wixstite.com/avocado\n\n")
            elif input_line.startswith("readfile[") and input_line.endswith("]"):
                filename = input_line[9:-1]  # extract filename from input line
                try:
                    with open(filename) as f:
                        file_contents = f.read()
                    self.textbox.insert(tk.END, f"\nread{{{file_contents}}}")
                except FileNotFoundError:
                    self.textbox.insert(tk.END, "\nERROR: File not found.\n")
            elif input_line.startswith("writefile[") and input_line.endswith("]"):
                filename, contents = input_line[10:-1].split("(")
                contents = contents[:-1]  # remove closing parentheses
                try:
                    with open(filename, "w") as f:
                        f.write(contents)
                    self.textbox.insert(tk.END, "\nFile written successfully.")
                except Exception as e:
                    self.textbox.insert(tk.END, f"\nERROR: {str(e)}")
                self.textbox.tag_add("system", "end-2l linestart", "end-1c")

            elif input_line.startswith("help[") and input_line.endswith("]"):
                fun = input_line[5:-1]
                if fun == "callcode":
                    self.textbox.insert(
                        tk.END, "\n\nmore information about these functions will be at:\n   https://ionalegoman.wixstite.com/avocado\n\n")

            else:
                self.textbox.insert(tk.END, "\nERROR: Unrecognized command.\n")
            self.textbox.see("end")

        def clear_input(self):
            input_text = self.textbox.get("end-2l linestart", "end-1c")
            input_line = input_text.split("\n")[-1]
            self.textbox.delete(
                "end-" + str(len(input_line) + 1) + "c", tk.END)

    root = tk.Tk()
    root.title("Py Terminal")
    app = Terminal(master=root)
    app.mainloop()


Pyterm()
