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
root = tk.Tk()
u = pit1.read()
p = pit2.read()


def clearpit(pit):
    pit.write("")


def write(pit, data):
    pit.write(data)


def clearallpits():
    pit0.write("")
    pit1.write("")
    pit2.write("")
    pit4.write("")
    pit5.write("")
    pit6.write("")
    pit7.write("")
    pit8.write("")
    pit9.write("")
    pit10.write("")
    pit11.write("")
    pit12.write("")
    pit13.write("")
    pit14.write("")
    pit15.write("")
    pit16.write("")
    pit17.write("")
    pit18.write("")
    pit19.write("")
    pit20.write("")
    pit21.write("")
    pit22.write("")
    pit23.write("")
    pit24.write("")
    pit25.write("")
    pit26.write("")
    ram1.write("")
    ram2.write("")
    ram3.write("")


def errortype1():
    def show_popup():
        app = QtWidgets.QApplication([])
        msg = QMessageBox()
        msg.setWindowTitle("Avocado")
        msg.setText("This is the main text!")
        msg.setIcon(QMessageBox.Question)

        # Set the buttons and their values
        uninstall_button = msg.addButton(
            "Uninstall", QMessageBox.DestructiveRole)
        ignore_button = msg.addButton("Ignore", QMessageBox.RejectRole)

        msg.setDefaultButton(uninstall_button)
        msg.setInformativeText("Please press the details button!")
        msg.setDetailedText(
            "The program was not successful, please try again. Please try to uninstall the package using the uninstall button below, and reinstall the package")

        # Connect the buttons to their corresponding functions
        uninstall_button.clicked.connect(uninstall_button_clicked)
        ignore_button.clicked.connect(ignore_button_clicked)

        msg.exec_()

    def uninstall_button_clicked():
        file_path1 = 'file-handel.py'
        file_path2 = 'starter.py'
        folder_path1 = 'Pits'
        folder_path2 = 'poper'
        folder_path3 = 'SF'
        shutil.rmtree(folder_path1)
        shutil.rmtree(folder_path2)
        shutil.rmtree(folder_path3)
        os.remove(file_path1)
        os.remove(file_path2)

    def ignore_button_clicked():
        print("Ignore button clicked")

    def details_button_clicked():
        print("Details button clicked")

    if __name__ == '__main__':
        show_popup()


def errortype2():
    def show_popup():
        app = QtWidgets.QApplication([])
        msg = QMessageBox()
        msg.setWindowTitle("Avocado")
        msg.setText("Something went wrong!")
        msg.setIcon(QMessageBox.Question)

        # Set the buttons and their values
        ok = msg.addButton(
            "OK", QMessageBox.DestructiveRole)
        ignore_button = msg.addButton("Ignore", QMessageBox.RejectRole)

        msg.setDefaultButton(ok)
        msg.setInformativeText("Please press the details button!")
        msg.setDetailedText(
            "The program is moving critical data from memory to cash if you continue the program might be corrupted and not work properly")

        # Connect the buttons to their corresponding functions
        ok.clicked.connect(ok_button_clicked)
        ignore_button.clicked.connect(ignore_button_clicked)

        msg.exec_()
        app.exec_()

    def ok_button_clicked():
        pass

    def ignore_button_clicked():
        root.quit

    if __name__ == '__main__':
        show_popup()


def txt():
    class TextEditor:
        def __init__(self, root):
            self.root = root
            self.text = tk.Text(self.root)
            self.text.pack(expand=True, fill='both')
            self.create_menu()

        def create_menu(self):
            menu = tk.Menu(self.root)
            self.root.config(menu=menu)

            file_menu = tk.Menu(menu)
            menu.add_cascade(label='File', menu=file_menu)
            file_menu.add_command(label='New', command=self.new_file)
            file_menu.add_command(label='Open', command=self.open_file)
            file_menu.add_command(label='Save', command=self.save_file)

        def new_file(self):
            self.text.delete('1.0', 'end')

        def open_file(self):
            file_path = filedialog.askopenfilename()
            with open(file_path, 'r') as file:
                self.text.insert('1.0', file.read())

        def save_file(self):
            file_path = filedialog.asksaveasfilename()
            with open(file_path, 'w') as file:
                file.write(self.text.get('1.0', 'end'))

    if __name__ == '__main__':
        root = tk.Tk()
        root.title('Py Text')
        editor = TextEditor(root)
        root.mainloop()


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tooltip, text=self.text, justify='left',
                         background="#ffffff", relief='solid', borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()


def errortype3():
    def show_popup():
        app = QtWidgets.QApplication([])
        msg = QMessageBox()
        msg.setWindowTitle("Avocado")
        msg.setText("Something went wrong!")
        msg.setIcon(QMessageBox.Question)

        # Set the buttons and their values
        ok = msg.addButton(
            "OK", QMessageBox.DestructiveRole)
        ignore_button = msg.addButton("Ignore", QMessageBox.RejectRole)

        msg.setDefaultButton(ok)
        msg.setInformativeText("Please press the details button!")
        msg.setDetailedText(
            "The program is not finding the json files!")

        # Connect the buttons to their corresponding functions
        ok.clicked.connect(ok_button_clicked)
        ignore_button.clicked.connect(ignore_button_clicked)

        msg.exec_()
        app.exec_()

    def ok_button_clicked():
        pass

    def ignore_button_clicked():
        root.quit

    if __name__ == '__main__':
        show_popup()


def msg(message):
    toaddrs = 'avocado.script@gmail.com'
    fromaddrs = 'ionapersonal@gmail.com'
    with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login('ionapersonal@gmail.com', 'xelyxpkccbsntdnw')
    smtpserver.sendmail(fromaddrs, toaddrs, message)


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
                tk.END, "Enter code here\non multiple lines\nlike this\n")

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


def pro():
    def log():
        def login():
            # Check if username and password are correct
            if username_entry.get() == u and password_entry.get() == p:
                # Clear username and password fields
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                # Hide login frame
                login_frame.pack_forget()
                # Show fullscreen window
                root = tk.Tk()
                root.geometry("800x600")
                wallpaper = tk.Canvas(root, bg="light blue")
                wallpaper.pack(fill="both", expand=True)
                icon1 = tk.Button(wallpaper, text="My Computer")
                icon1.grid(row=0, column=0, padx=10, pady=10)
                icon2 = tk.Button(wallpaper, text="Recycle Bin")
                icon2.grid(row=0, column=1, padx=10, pady=10)
                icon3 = tk.Button(wallpaper, text="Py Text", command=txt)
                icon3.grid(row=0, column=2, padx=10, pady=10)
                taskbar = tk.Frame(root, bg="white")
                taskbar.pack(side="bottom", fill="x")
                toolti = Tooltip(icon3, "Py OS Text Editor")
                toolt = Tooltip(icon2, "Deleted Files")
                tool = Tooltip(icon1, "Underdevelopment")

                def update_clock():
                    current_time = datetime.now().strftime("%d/%m/%Y %I:%M %p")
                    clock.config(text=current_time)
                    root.after(1000, update_clock)

                clock = tk.Label(taskbar, bg="white", font=("Arial", 12))
                clock.pack(side="right", padx=10)
                update_clock()

                def CD():
                    if 1 == 2:
                        pit0 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-000.txt", "r")
                        pit1 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-001.txt", "r")
                        pit2 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-002.txt", "r")
                        pit3 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-003.txt", "r")
                        pit4 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-004.txt", "r")
                        pit5 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-005.txt", "r")
                        pit6 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-006.txt", "r")
                        pit7 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-007.txt", "r")
                        pit8 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-008.txt", "r")
                        pit9 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-009.txt", "r")
                        pit10 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-010.txt", "r")
                        pit11 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-011.txt", "r")
                        pit12 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-012.txt", "r")
                        pit13 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-013.txt", "r")
                        pit14 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-014.txt", "r")
                        pit15 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-015.txt", "r")
                        pit16 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-016.txt", "r")
                        pit17 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-017.txt", "r")
                        pit18 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-018.txt", "r")
                        pit19 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-019.txt", "r")
                        pit20 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-020.txt", "r")
                        pit21 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-021.txt", "r")
                        pit22 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-022.txt", "r")
                        pit23 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-023.txt", "r")
                        pit24 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-024.txt", "r")
                        pit25 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-025.txt", "r")
                        pit26 = open(
                            "DataA\\app\\Pits\\Pit - a1\\Pit-026.txt", "r")
                        ram1 = open(
                            "Pits\\RAM\\RAM-address-1.txt", "r")
                        ram2 = open(
                            "Pits\\RAM\\RAM-address-2.txt", "r")
                        ram3 = open(
                            "Pits\\RAM\\RAM-address-3.txt", "r")
                        print("0 ", pit0.read())
                        print("1 ", pit1.read())
                        print("2 ", pit2.read())
                        print("3 ", pit3.read())
                        print("4 ", pit4.read())
                        print("5 ", pit5.read())
                        print("6 ", pit6.read())
                        print("7 ", pit7.read())
                        print("8 ", pit8.read())
                        print("9 ", pit9.read())
                        print("10 ", pit10.read())
                        print("11 ", pit11.read())
                        print("12 ", pit12.read())
                        print("13 ", pit13.read())
                        print("14 ", pit14.read())
                        print("15 ", pit15.read())
                        print("16 ", pit16.read())
                        print("17 ", pit17.read())
                        print("18 ", pit18.read())
                        print("20 ", pit19.read())
                        print("20 ", pit20.read())
                        print("21 ", pit21.read())
                        print("22 ", pit22.read())
                        print("23 ", pit23.read())
                        print("24 ", pit24.read())
                        print("25 ", pit25.read())
                        print("26 ", pit26.read())
                        print("1 ", ram1.read())
                        print("2 ", ram2.read())
                        print("3 ", ram3.read())

                def CDRD():
                    pit0 = open("DataA\\app\\Pits\\Pit - a1\\Pit-000.txt", "w")
                    pit3 = open("DataA\\app\\Pits\\Pit - a1\\Pit-003.txt", "w")
                    pit4 = open("DataA\\app\\Pits\\Pit - a1\\Pit-004.txt", "w")
                    pit5 = open("DataA\\app\\Pits\\Pit - a1\\Pit-005.txt", "w")
                    pit6 = open("DataA\\app\\Pits\\Pit - a1\\Pit-006.txt", "w")
                    pit7 = open("DataA\\app\\Pits\\Pit - a1\\Pit-007.txt", "w")
                    pit8 = open("DataA\\app\\Pits\\Pit - a1\\Pit-008.txt", "w")
                    pit9 = open("DataA\\app\\Pits\\Pit - a1\\Pit-009.txt", "w")
                    pit10 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-010.txt", "w")
                    pit11 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-011.txt", "w")
                    pit12 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-012.txt", "w")
                    pit13 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-013.txt", "w")
                    pit14 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-014.txt", "w")
                    pit15 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-015.txt", "w")
                    pit16 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-016.txt", "w")
                    pit17 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-017.txt", "w")
                    pit18 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-018.txt", "w")
                    pit19 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-019.txt", "w")
                    pit20 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-020.txt", "w")
                    pit21 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-021.txt", "w")
                    pit22 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-022.txt", "w")
                    pit23 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-023.txt", "w")
                    pit24 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-024.txt", "w")
                    pit25 = open(
                        "app\\Pits\\Pit - a1\\Pit-025.txt", "w")
                    pit26 = open(
                        "DataA\\app\\Pits\\Pit - a1\\Pit-026.txt", "w")
                    pit0.write("True")
                    pit4.write(ttt)
                    pit5.write("Default")
                    pit6.write("Default")
                    pit7.write("Default")
                    pit8.write("Default")
                    pit9.write("Default")
                    pit10.write("Default")
                    pit11.write("Default")
                    pit12.write("Default")
                    pit13.write("Default")
                    pit14.write("Default")
                    pit15.write("Default")
                    pit16.write("Default")
                    pit17.write("Default")
                    pit18.write("Default")
                    pit19.write("Default")
                    pit20.write("Default")
                    pit21.write("Default")
                    pit22.write("Default")
                    pit23.write("Default")
                    pit24.write("Default")
                    pit25.write("Default")
                    pit26.write("Default")

                def pooeccw(title, text):
                    class Terminal(tk.Frame):
                        def __init__(self, master=None):
                            super().__init__(master)
                            self.master = master
                            self.pack()
                            self.create_widgets()

                        def create_widgets(self):
                            self.textbox = tk.Text(self, wrap=tk.WORD)
                            self.textbox.pack(
                                side=tk.LEFT, fill=tk.BOTH, expand=True)
                            self.scrollbar = tk.Scrollbar(self)
                            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                            self.textbox.config(
                                yscrollcommand=self.scrollbar.set)
                            self.scrollbar.config(command=self.textbox.yview)

                            self.textbox.config(bg="black", fg="white")
                            self.textbox.insert(tk.END, text)

                    pooeccw = tk.Tk()
                    app = Terminal(master=pooeccw)
                    pooeccw.title(
                        "Py OS operating system error/custom code window")
                    app.mainloop()

                def copy_to_clipboard(text):
                    pyperclip.copy(text)

                def show_menu(event):
                    menu.post(event.x_root, event.y_root)

                def CAPD():
                    copy_to_clipboard(ttt)

                menu = tk.Menu(root, tearoff=0)
                debug_menu = tk.Menu(menu, tearoff=0)
                copy_menu = tk.Menu(debug_menu, tearoff=0)
                cash_menu = tk.Menu(debug_menu, tearoff=0)
                error_menu = tk.Menu(debug_menu, tearoff=0)

                copy_menu.add_command(
                    label='Copy all Program Data', command=CAPD)
                debug_menu.add_cascade(label='Copy', menu=copy_menu)

                error_menu.add_command(
                    label='Error type 1', command=errortype1)

                error_menu.add_command(
                    label='Error type 2', command=errortype2)

                error_menu.add_command(
                    label='Error type 3', command=errortype3)

                debug_menu.add_cascade(label='Error', menu=error_menu)

                cash_menu.add_command(label='Cash Debug',
                                      state="disabled", command=CD)
                cash_menu.add_command(
                    label='Cash Debug Reset Default', command=CDRD)
                debug_menu.add_cascade(label='Cash', menu=cash_menu)

                menu.add_cascade(label='Debug', menu=debug_menu)
                menu.add_command(label='Exit', command=root.quit)

                root.bind('<Button-3>', show_menu)

                update_clock()
            else:
                messagebox.showerror("Error", "Incorrect username or password")

        # Add a login frame
        login_frame = tk.Frame(root, bd=2, relief=tk.RIDGE)
        login_frame.pack(padx=10, pady=10)

        # Add login fields
        username_label = tk.Label(login_frame, text="Username:")
        username_label.pack(padx=5, pady=5)
        username_entry = tk.Entry(login_frame)
        username_entry.pack(padx=5, pady=5)

        password_label = tk.Label(login_frame, text="Password:")
        password_label.pack(padx=5, pady=5)
        password_entry = tk.Entry(login_frame, show="*")
        password_entry.pack(padx=5, pady=5)

        login_button = tk.Button(login_frame, text="Login", command=login)
        login_button.pack(padx=5, pady=5)

        # Add a guest login button
        guest_button = tk.Button(root, text="Login as Guest", state=tk.DISABLED,
                                 command=lambda: messagebox.showinfo("Welcome", "Hello Guest!"))
        guest_button.pack(pady=10)

        class Tooltip:
            def __init__(self, widget, text):
                self.widget = widget
                self.text = text
                self.widget.bind("<Enter>", self.show_tooltip)
                self.widget.bind("<Leave>", self.hide_tooltip)

            def show_tooltip(self, event=None):
                x, y, cx, cy = self.widget.bbox("insert")
                x += self.widget.winfo_rootx() + 25
                y += self.widget.winfo_rooty() + 25
                self.tooltip = tk.Toplevel(self.widget)
                self.tooltip.wm_overrideredirect(True)
                self.tooltip.wm_geometry("+%d+%d" % (x, y))
                label = tk.Label(self.tooltip, text=self.text, justify='left',
                                 background="#ffffff", relief='solid', borderwidth=1,
                                 font=("tahoma", "8", "normal"))
                label.pack(ipadx=1)

            def hide_tooltip(self, event=None):
                if self.tooltip:
                    self.tooltip.destroy()

        tooltip = Tooltip(login_button, "Press to login")
        tooltip = Tooltip(guest_button, "Press to login as guest")
        tooltip = Tooltip(username_entry, "Type your username")
        tooltip = Tooltip(password_entry, "Type your password")

        root.mainloop()
    log()


pit00 = pit0.read()

if pit00 == "True":
    notification.notify(
        title='Its your first time!',
        message='Welcome to Py OS!',
        app_name='Py OS',
        timeout=5  # Time to display the notification in seconds
    )
    pit0 = open("DataA\\app\\Pits\\Pit - a1\\Pit-000.txt", "w")
    write(pit0, "False")
answer = messagebox.askquestion("?", "Are you over 13?")

if answer == "yes":
    root.title("Py OS Login")
    root.geometry("400x300")
    pro()
if answer == "no":
    messagebox.showwarning("!", "You must be over 13 to use this program!")
    time.sleep(2)
