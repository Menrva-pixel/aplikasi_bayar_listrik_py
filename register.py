import tkinter as tk
from tkinter import messagebox
from database import Database

class RegisterPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.db = Database()  # Buat objek Database

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.db.get_user(username)
        if user:
            messagebox.showerror("Error", "Username already exists")
            return

        self.db.add_user(username, password, 'user')
        messagebox.showinfo("Success", "Registration successful. Please log in.")
        self.master.show_login_page()

    def __del__(self):
        self.db.close()
