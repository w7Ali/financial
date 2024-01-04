# main.py
import tkinter as tk
from transaction_manager import TransactionManager
from bank_account_manager import BankAccountManager
from spendings_manager import SpendingsManager

# Create the Tkinter window
root = tk.Tk()

# Create instances of TransactionManager and BankAccountManager
transaction_manager = TransactionManager(root, "expense_manager.db")
bank_account_manager = BankAccountManager(root)
spendings_manager = SpendingsManager(root, bank_account_manager.bank_accounts)  # Pass the bank_accounts to SpendingsManager
# Run the Tkinter event loop
root.mainloop()
