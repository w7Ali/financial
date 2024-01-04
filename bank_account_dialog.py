import tkinter as tk
from tkinter import messagebox

class BankAccountDialog:
    def __init__(self, parent, existing_accounts):
        self.top = tk.Toplevel(parent)
        self.top.title("Add Bank Account")
        self.top.geometry("600x400")

        self.account_name_var = tk.StringVar()
        self.account_type_var = tk.StringVar()
        self.account_number_var = tk.StringVar()
        self.ifsc_var = tk.StringVar()

        tk.Label(self.top, text="Account Name:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.top, textvariable=self.account_name_var, font=("Helvetica", 12)).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.top, text="Account Type:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.top, textvariable=self.account_type_var, font=("Helvetica", 12)).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.top, text="Account Number:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.top, textvariable=self.account_number_var, font=("Helvetica", 12)).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.top, text="IFSC:", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(self.top, textvariable=self.ifsc_var, font=("Helvetica", 12)).grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.top, text="Add Account", command=self.add_account, font=("Helvetica", 12), bg="#3CB371", fg="#FFFFFF").grid(row=4, column=0, columnspan=2, pady=10)

        self.result = None
        self.existing_accounts = existing_accounts  # Use the existing_accounts passed as an argument

    def add_account(self):
        account_name = self.account_name_var.get()
        account_type = self.account_type_var.get()
        account_number = self.account_number_var.get()
        ifsc = self.ifsc_var.get()

        if not (account_name and account_type and account_number and ifsc):
            messagebox.showerror("Error", "Please fill in all the details.")
            return

        if any(account["account_number"] == account_number for account in self.existing_accounts):
            messagebox.showerror("Error", "Account with this account number already exists.")
            return

        self.result = {
            "account_name": account_name,
            "account_type": account_type,
            "account_number": account_number,
            "ifsc": ifsc,
            "balance": 0
        }

        self.top.destroy()
