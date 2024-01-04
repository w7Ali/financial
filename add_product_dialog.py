# add_product_dialog.py
import tkinter as tk
from tkinter import StringVar, Label, Entry, Button, Radiobutton, messagebox

class AddProductDialog:
    def __init__(self, parent, bank_accounts):
        self.top = tk.Toplevel(parent)
        self.top.title("Add Product")
        self.top.geometry("400x250")

        self.product_name_var = StringVar()
        self.product_price_var = StringVar()
        self.product_description_var = StringVar()
        self.payment_method_var = StringVar(value="Cash")

        Label(self.top, text="Product Name:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5)
        Entry(self.top, textvariable=self.product_name_var, font=("Helvetica", 12)).grid(row=0, column=1, padx=10, pady=5)

        Label(self.top, text="Product Price ($):", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
        Entry(self.top, textvariable=self.product_price_var, font=("Helvetica", 12)).grid(row=1, column=1, padx=10, pady=5)

        Label(self.top, text="Product Description:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5)
        Entry(self.top, textvariable=self.product_description_var, font=("Helvetica", 12)).grid(row=2, column=1, padx=10, pady=5)

        Label(self.top, text="Payment Method:", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=5)
        Radiobutton(self.top, text="Cash", variable=self.payment_method_var, value="Cash", font=("Helvetica", 12)).grid(row=3, column=1, padx=10, pady=5)
        Radiobutton(self.top, text="Bank Account", variable=self.payment_method_var, value="Bank", font=("Helvetica", 12)).grid(row=3, column=2, padx=10, pady=5)

        Button(self.top, text="Add Product", command=self.add_product, font=("Helvetica", 12), bg="#3CB371", fg="#FFFFFF").grid(row=4, column=0, columnspan=2, pady=10)

        self.result = None
        self.bank_accounts = bank_accounts

    def add_product(self):
        product_name = self.product_name_var.get()
        product_price = float(self.product_price_var.get())
        product_description = self.product_description_var.get()
        payment_method = self.payment_method_var.get()

        if not self.bank_accounts or payment_method == "Cash":
            # Handle cash transaction
            messagebox.showinfo("Product Transaction", f"Added {product_name} as cash. Price: ${product_price}")
        else:
            # Handle bank account transaction
            selected_account_name = payment_method
            for account in self.bank_accounts:
                if account["account_name"] == selected_account_name:
                    account["balance"] -= product_price
                    messagebox.showinfo("Product Transaction", f"Added {product_name} to {selected_account_name}. Remaining balance: ${account['balance']}")
                    break

        self.top.destroy()
