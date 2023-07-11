import tkinter as tk
from tkinter import messagebox
from database import Database

class LoginPage(tk.Frame):
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

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.db.get_user(username)
        if user is None:
            messagebox.showerror("Error", "Invalid username or password")
            return

        db_password = user[2]  # Ambil password dari hasil query
        if password == db_password:
            role = user[3]  # Ambil role dari hasil query
            if role == 'Administrator':
                self.master.show_admin_page()
            elif role == 'Pelanggan':
                self.master.show_user_page(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.master.show_register_page()

    def hide(self):
        self.pack_forget()

    def __del__(self):
        self.db.close()
