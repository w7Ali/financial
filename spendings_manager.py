# spendings_manager.py
import tkinter as tk
from tkinter import messagebox
from add_emi_dialog import AddEMIDialog
from add_product_dialog import AddProductDialog

class SpendingsManager:
    def __init__(self, root, bank_accounts):
        self.root = root
        self.bank_accounts = bank_accounts

        spendings_frame = tk.Frame(root, bg="#D1E9FF", pady=10)
        spendings_frame.pack(fill="x")

        tk.Button(spendings_frame, text="Add EMI", command=self.add_emi, bg="#3CB371", fg="#FFFFFF").grid(row=0, column=0, padx=10)
        tk.Button(spendings_frame, text="Add Product", command=self.add_product, bg="#3CB371", fg="#FFFFFF").grid(row=0, column=1, padx=10)

    def add_emi(self):
        add_emi_dialog = AddEMIDialog(self.root, self.bank_accounts)
        self.root.wait_window(add_emi_dialog.top)
        # Handle the result if needed

    def add_product(self):
        add_product_dialog = AddProductDialog(self.root, self.bank_accounts)
        self.root.wait_window(add_product_dialog.top)
        # Handle the result if needed
