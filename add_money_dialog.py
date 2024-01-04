# add_money_dialog.py
from tkinter import Toplevel, StringVar, OptionMenu, Label, Entry, Button, messagebox, Menu, simpledialog

class AddMoneyDialog:
    def __init__(self, parent, bank_accounts, cash_amount, currency):
        self.top = Toplevel(parent)
        self.top.title("Add Money to Account")
        self.top.geometry("700x450")

        self.selected_account_var = StringVar(value="Cash")
        self.amount_var = StringVar()
        self.description_var = StringVar()
        self.date_var = StringVar(value="Just Now")
        self.time_var = StringVar(value="")

        Label(self.top, text="Select Account or Cash:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10)

        if bank_accounts:
            # Only create OptionMenu if bank_accounts is not empty
            OptionMenu(self.top, self.selected_account_var, *["Cash"] + [account["account_name"] for account in bank_accounts]).grid(row=0, column=1, padx=10, pady=10)

        Label(self.top, text="Amount: $", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10)
        Entry(self.top, textvariable=self.amount_var, font=("Helvetica", 12)).grid(row=1, column=1, padx=10, pady=10)

        Label(self.top, text="Description:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10)
        Entry(self.top, textvariable=self.description_var, font=("Helvetica", 12)).grid(row=2, column=1, padx=10, pady=10)

        Label(self.top, text="Date:", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=10)
        Entry(self.top, textvariable=self.date_var, font=("Helvetica", 12)).grid(row=3, column=1, padx=10, pady=10)

        Label(self.top, text="Time:", font=("Helvetica", 12)).grid(row=4, column=0, padx=10, pady=10)
        Entry(self.top, textvariable=self.time_var, font=("Helvetica", 12)).grid(row=4, column=1, padx=10, pady=10)

        Button(self.top, text="Add Money", command=self.add_money, font=("Helvetica", 12), bg="#3CB371", fg="#FFFFFF").grid(row=5, column=0, columnspan=2, pady=10)

        # Add Setting Menu
        setting_menu = Menu(self.top)
        self.top.config(menu=setting_menu)
        currency_menu = Menu(setting_menu, tearoff=0)
        setting_menu.add_cascade(label="Settings", menu=currency_menu)
        currency_menu.add_command(label="Select Currency", command=self.select_currency)

        self.result = None
        self.bank_accounts = bank_accounts
        self.cash_amount = cash_amount
        self.currency = currency

    def add_money(self):
        selected_account_name = self.selected_account_var.get()
        amount = float(self.amount_var.get())
        description = self.description_var.get()
        date_str = self.date_var.get()
        time_str = self.time_var.get()

        if not self.bank_accounts or selected_account_name == "Cash":
            # Handle cash transaction
            self.cash_amount += amount
            total_amount = self.cash_amount
            messagebox.showinfo("Cash Transaction", f"Added ${amount} as cash. Total Amount: ${total_amount}")
        else:
            # Handle bank account transaction
            for account in self.bank_accounts:
                if account["account_name"] == selected_account_name:
                    account["balance"] += amount
                    total_amount = sum(account["balance"] for account in self.bank_accounts) + self.cash_amount
                    messagebox.showinfo("Bank Transaction", f"Added ${amount} to {selected_account_name}. Total Amount: ${total_amount}")
                    break

        # Update the transaction history and show the analysis report
        # ... (code to update transaction history and show analysis report)

        self.top.destroy()

    def select_currency(self):
        # Let's use simpledialog for simplicity. You can enhance this with more sophisticated logic.
        result = simpledialog.askstring("Select Currency", "Enter Currency Code (e.g., USD, EUR):")
        if result:
            self.currency = result

