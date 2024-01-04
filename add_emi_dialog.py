import tkinter as tk
from tkinter import StringVar, Label, Entry, Button, OptionMenu, messagebox

class AddEMIDialog:
    def __init__(self, parent, bank_accounts):
        self.top = tk.Toplevel(parent)
        self.top.title("Add EMI")
        self.top.geometry("400x250")

        self.selected_account_var = StringVar(value="Cash")
        self.product_name_var = StringVar()
        self.emi_amount_var = StringVar()
        self.emi_total_var = StringVar()
        self.remaining_months_var = StringVar()
        self.payment_method_var = StringVar(value="Cash")

        Label(self.top, text="Select Account or Cash:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10)

        if bank_accounts:
            OptionMenu(self.top, self.selected_account_var, *["Cash"] + [account["account_name"] for account in bank_accounts]).grid(row=0, column=1, padx=10, pady=10)

        Label(self.top, text="Product Name:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10)
        Entry(self.top, textvariable=self.product_name_var, font=("Helvetica", 12)).grid(row=1, column=1, padx=10, pady=10)

        Label(self.top, text="EMI Amount ($):", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10)
        Entry(self.top, textvariable=self.emi_amount_var, font=("Helvetica", 12)).grid(row=2, column=1, padx=10, pady=10)

        Label(self.top, text="EMI Total:", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=10)
        Entry(self.top, textvariable=self.emi_total_var, font=("Helvetica", 12)).grid(row=3, column=1, padx=10, pady=10)

        Label(self.top, text="Remaining Months:", font=("Helvetica", 12)).grid(row=4, column=0, padx=10, pady=10)
        Entry(self.top, textvariable=self.remaining_months_var, font=("Helvetica", 12)).grid(row=4, column=1, padx=10, pady=10)

        Label(self.top, text="Payment Method:", font=("Helvetica", 12)).grid(row=5, column=0, padx=10, pady=10)
        OptionMenu(self.top, self.payment_method_var, "Cash", "Bank").grid(row=5, column=1, padx=10, pady=10)

        Button(self.top, text="Add EMI", command=self.add_emi, font=("Helvetica", 12), bg="#3CB371", fg="#FFFFFF").grid(row=6, column=0, columnspan=2, pady=10)

        self.result = None
        self.bank_accounts = bank_accounts

    def add_emi(self):
        selected_account_name = self.selected_account_var.get()
        product_name = self.product_name_var.get()
        emi_amount = float(self.emi_amount_var.get())
        emi_total = float(self.emi_total_var.get())
        remaining_months =
