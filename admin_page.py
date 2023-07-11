import tkinter as tk
from tkinter import messagebox
from database import Database
from login import LoginPage

class AdminPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.db = Database()  # Buat objek Database

        self.label = tk.Label(self, text="Admin Page")
        self.label.pack()

        self.user_listbox = tk.Listbox(self)
        self.user_listbox.pack()

        self.refresh_users()

        self.user_label = tk.Label(self, text="Selected User: ")
        self.user_label.pack()

        self.usage_label = tk.Label(self, text="Electricity Usage:")
        self.usage_label.pack()

        self.bill_label = tk.Label(self, text="Bill Amount: ")
        self.bill_label.pack()

        self.status_label = tk.Label(self, text="Payment Status: ")
        self.status_label.pack()

        self.show_details_button = tk.Button(self, text="Show Details", command=self.show_details)
        self.show_details_button.pack()

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack()

        self.add_button = tk.Button(self, text="Add User", command=self.add_user)
        self.add_button.pack()

        self.edit_button = tk.Button(self, text="Edit User", command=self.edit_user)
        self.edit_button.pack()

        self.delete_button = tk.Button(self, text="Delete User", command=self.delete_user)
        self.delete_button.pack()

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack()

        self.previous_page = None

    def refresh_users(self):
        self.user_listbox.delete(0, tk.END)
        users = self.db.get_all_users()
        for user in users:
            self.user_listbox.insert(tk.END, user[1])  # Menampilkan nama pengguna

    def add_user(self):
        username = messagebox.askstring("Add User", "Enter username:")
        if username:
            password = messagebox.askstring("Add User", "Enter password:")
            if password:
                privilege = messagebox.askstring("Add User", "Enter privilege (Administrator/Pelanggan):")
                if privilege in ['Administrator', 'Pelanggan']:
                    self.db.add_user(username, password, privilege)
                    self.refresh_users()
                else:
                    messagebox.showerror("Error", "Invalid privilege")
            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            messagebox.showerror("Error", "Invalid username")

            
    def show_details(self):
        selected_index = self.user_listbox.curselection()
        if selected_index:
            username = self.user_listbox.get(selected_index)
            user = self.db.get_user(username)
            self.user_label.config(text=f"Selected User: {username}")

            # Ambil data penggunaan listrik dan tagihan listrik pengguna
            user_data = self.db.get_electricity_usage(user[0])
            bill_data = self.db.get_electricity_bill(user[0])

            self.user_label.config(text="Electricity Usage:")
            self.bill_label.config(text="Bill Amount: ")
            self.status_label.config(text="Payment Status: ")

            if user_data:
                self.display_usage(user_data)
            else:
                self.user_label.config(text="Electricity Usage: (empty)")

            if bill_data:
                self.display_bill(bill_data)
            else:
                self.bill_label.config(text="Bill Amount: (empty)")
                self.status_label.config(text="Payment Status: (empty)")
        else:
            messagebox.showerror("Error", "No user selected")

    def display_usage(self, user_data):
        self.user_label.config(text="Electricity Usage:")
        self.user_listbox.delete(0, tk.END)
        for usage in user_data:
            user_str = f"Month: {usage[2]}, Year: {usage[3]}, Usage Amount: {usage[4]}"
            self.user_listbox.insert(tk.END, user_str)

    def display_bill(self, bill_data):
        self.bill_label.config(text=f"Bill Amount: {bill_data[0][4]}")
        self.status_label.config(text=f"Payment Status: {bill_data[0][5]}")

    def edit_user(self):
        selected_index = self.user_listbox.curselection()
        if selected_index:
            username = self.user_listbox.get(selected_index)
            user = self.db.get_user(username)
            new_username = messagebox.askstring("Edit User", "Enter new username:", initialvalue=user[1])
            if new_username:
                new_password = messagebox.askstring("Edit User", "Enter new password:", initialvalue=user[2])
                if new_password:
                    new_privilege = messagebox.askstring("Edit User", "Enter new privilege (Administrator/Pelanggan):",
                                                         initialvalue=user[3])
                    if new_privilege in ['Administrator', 'Pelanggan']:
                        self.db.update_user(user[0], new_username, new_password, new_privilege)
                        self.refresh_users()
                    else:
                        messagebox.showerror("Error", "Invalid privilege")
                else:
                    messagebox.showerror("Error", "Invalid password")
            else:
                messagebox.showerror("Error", "Invalid username")
        else:
            messagebox.showerror("Error", "No user selected")

    def delete_user(self):
        selected_index = self.user_listbox.curselection()
        if selected_index:
            username = self.user_listbox.get(selected_index)
            if messagebox.askyesno("Delete User", f"Are you sure you want to delete user '{username}'?"):
                self.db.delete_user(username)
                self.refresh_users()
        else:
            messagebox.showerror("Error", "No user selected")

    def go_back(self):
        if self.previous_page:
            self.destroy()
            self.previous_page.deiconify()

    def set_previous_page(self, previous_page):
        self.previous_page = previous_page

    def log_out(self):
        self.destroy()
        LoginPage(self.master)

    def __del__(self):
        self.db.close()
