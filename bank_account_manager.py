# bank_account_manager.py
import tkinter as tk
from tkinter import messagebox
from bank_account_dialog import BankAccountDialog
from add_money_dialog import AddMoneyDialog
class BankAccountManager:
    def __init__(self, root):
        self.root = root
        self.bank_accounts = []
        self.selected_account = None

        # Bank Account Section
        bank_account_frame = tk.Frame(root, bg="#D1E9FF", pady=10)
        bank_account_frame.pack(fill="x")

        tk.Label(bank_account_frame, text="Bank Accounts:", font=("Helvetica", 14), bg="#D1E9FF", padx=10).grid(row=0, column=0)
        tk.Button(bank_account_frame, text="Add Account", command=self.add_bank_account, bg="#3CB371", fg="#FFFFFF").grid(row=0, column=1, padx=10)
        tk.Button(bank_account_frame, text="Add Money", command=self.add_money_to_account, bg="#3CB371", fg="#FFFFFF").grid(row=0, column=2, padx=10)
        tk.Button(bank_account_frame, text="Check Total", command=self.check_total_amount, bg="#3CB371", fg="#FFFFFF").grid(row=0, column=3, padx=10)

    def add_bank_account(self):
        account_dialog = BankAccountDialog(self.root, self.bank_accounts)
        self.root.wait_window(account_dialog.top)
        if account_dialog.result:
            self.bank_accounts.append(account_dialog.result)

    # In the BankAccountManager class
    def add_money_to_account(self):
        account_dialog = AddMoneyDialog(self.root, self.bank_accounts, 0,
                                        "")  # Provide default values for cash_amount and currency
        self.root.wait_window(account_dialog.top)
        if account_dialog.result:
            selected_account_name = account_dialog.result["account_name"]
            amount = account_dialog.result["amount"]

            if not self.bank_accounts or selected_account_name == "Cash":
                # Handle cash transaction
                amount_added = amount
                self.root.cash_amount += amount_added
                messagebox.showinfo("Success",
                                    f"Added ${amount_added} as cash. New cash balance: ${self.root.cash_amount}")
            else:
                # Handle bank account transaction
                for account in self.bank_accounts:
                    if account["account_name"] == selected_account_name:
                        account["balance"] += amount
                        messagebox.showinfo("Success",
                                            f"Added ${amount} to {selected_account_name}. New balance: ${account['balance']}")
                        break

    # def check_total_amount(self):
    #     total_bank_amount = sum(account["balance"] for account in self.bank_accounts)
    #     total_amount = total_bank_amount # self.root.cash_amount
    #     messagebox.showinfo("Total Amount", f"Total amount across all accounts: ${total_amount}")

    def check_total_amount(self):
        total_bank_amount = sum(account["balance"] for account in self.bank_accounts)
        total_amount = total_bank_amount
        messagebox.showinfo("Total Amount", f"Total amount across all accounts: ${total_amount}")

