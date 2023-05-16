def run():
    import threading,tkinter as tk,keyboard,smtplib
    def send_email(email, message):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpserver:
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('ionapersonal@gmail.com', 'xelyxpkccbsntdnw')
            smtpserver.sendmail('ionapersonal@gmail.com', email, message)


    def update_label(label, entry):
        label.config(text=entry.get())


    def start_update_thread(root, label, entry1, entry2):
        def update():
            update_label(label, entry1)

            if keyboard.is_pressed("enter"):
                email = entry1.get()
                message = entry2.get("1.0", "end-1c")
                send_email(email, message)
                return

            root.after(50, update)  # Modify the delay time to adjust the thread speed

        update()


    def setup_gui():
        root = tk.Tk()
        root.geometry("400x200")
        root.title("Emailer")

        main_frame = tk.Frame(root, pady=20)
        main_frame.pack()

        my_label = tk.Label(main_frame, text="Hello World", bg="red", fg="white", font=("Arial", 16, "bold"))
        my_label.pack(pady=10)

        entry1 = tk.Entry(main_frame, width=30, font=("Arial", 12))
        entry1.pack(pady=10)

        entry2 = tk.Text(main_frame, width=30, height=5, font=("Arial", 12))
        entry2.pack(pady=10)

        start_button = tk.Button(main_frame, text="Start", command=lambda: start_update_thread(root, my_label, entry1, entry2))
        start_button.pack()

        root.mainloop()
    setup_gui()
