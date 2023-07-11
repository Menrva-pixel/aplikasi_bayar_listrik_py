import tkinter as tk
from tkinter import messagebox
from login import LoginPage
from register import RegisterPage
from user_page import UserPage
from admin_page import AdminPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Pembayaran Listrik Pascabayar")
        self.geometry("400x300")
        
        self.show_login_page()
    
    def show_login_page(self):
        self.clear_frame()
        login_page = LoginPage(self)
        login_page.pack()
        
    def show_register_page(self):
        self.clear_frame()
        register_page = RegisterPage(self)
        register_page.pack()
    
    def show_user_page(self, username):
        self.clear_frame()
        user_page = UserPage(self, username)
        user_page.pack()
        
    def show_admin_page(self):
        self.clear_frame()
        admin_page = AdminPage(self)
        admin_page.pack()
    
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
