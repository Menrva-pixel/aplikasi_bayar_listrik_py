import tkinter as tk

class UserPage(tk.Frame):
    def __init__(self, master, username):
        super().__init__(master)
        
        self.label = tk.Label(self, text=f"Welcome, {username}!")
        self.label.pack()
        
        # TODO: Tampilkan tagihan listrik pengguna
