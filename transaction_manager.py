# transaction_manager.py
import tkinter as tk
from tkinter import messagebox
from dateutil.relativedelta import relativedelta
import datetime
from tkcalendar import DateEntry
import sqlite3

class TransactionManager:
    def __init__(self, root, db_name):
        self.root = root
        self.root.title("Expense Manager")
        self.root.geometry("800x500")
        self.root.configure(bg="#E6F7FF")  # Light blue background

        # Create SQLite database and tables
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

        # Shared data
        self.transactions = []

        # Header
        tk.Label(root, text="Expense Manager", font=("Helvetica", 20), bg="#4285F4", fg="#FFFFFF", pady=10).pack(fill="x")

        # Summary Section
        # tk.Label(root, text="Summary:", font=("Helvetica", 16), bg="#4285F4", fg="#FFFFFF", pady=10).pack(fill="x")
        # self.summary_text = tk.Text(root, height=8, width=60, font=("Helvetica", 12), bg="#FFFFFF")
        # self.summary_text.pack()

    def create_tables(self):
        cursor = self.conn.cursor()
        # Create transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                amount REAL,
                person TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def record_transaction(self):
        try:
            amount = float(self.transaction_amount_entry.get())
            person = self.transaction_person_entry.get()
            transaction_type = self.transaction_type_var.get()
            product_name = self.product_name_entry.get()
            product_price = float(self.product_price_entry.get())
            product_description = self.product_description_entry.get()
            payment_method = self.payment_method_var.get()

            self.insert_transaction(transaction_type, amount, person, product_name, product_price, product_description,
                                    payment_method)

            messagebox.showinfo("Success",
                                f"Transaction recorded - Type: {transaction_type}, Amount: ${amount}, Person: {person}")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount or price. Please enter valid numbers.")

    def insert_transaction(self, transaction_type, amount, person, product_name, product_price, product_description,
                           payment_method):
        cursor = self.conn.cursor()
        cursor.execute("""
             INSERT INTO transactions
             (type, amount, person, product_name, product_price, product_description, payment_method)
             VALUES (?, ?, ?, ?, ?, ?, ?)
         """, (transaction_type, amount, person, product_name, product_price, product_description, payment_method))
        self.conn.commit()

    def create_product_entry_widgets(self):
        tk.Label(self.root, text="Product Name:", font=("Helvetica", 12), bg="#4285F4", fg="#FFFFFF").pack(fill="x",
                                                                                                           padx=10,
                                                                                                           pady=5)
        self.product_name_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.product_name_entry.pack(fill="x", padx=10, pady=5)

        tk.Label(self.root, text="Product Price ($):", font=("Helvetica", 12), bg="#4285F4", fg="#FFFFFF").pack(
            fill="x", padx=10, pady=5)
        self.product_price_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.product_price_entry.pack(fill="x", padx=10, pady=5)

        tk.Label(self.root, text="Product Description:", font=("Helvetica", 12), bg="#4285F4", fg="#FFFFFF").pack(
            fill="x", padx=10, pady=5)
        self.product_description_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.product_description_entry.pack(fill="x", padx=10, pady=5)

        tk.Label(self.root, text="Payment Method:", font=("Helvetica", 12), bg="#4285F4", fg="#FFFFFF").pack(fill="x",
                                                                                                             padx=10,
                                                                                                             pady=5)
        self.payment_method_var = tk.StringVar(value="Cash")
        tk.Radiobutton(self.root, text="Cash", variable=self.payment_method_var, value="Cash", font=("Helvetica", 12),
                       bg="#E6F7FF").pack(fill="x", padx=10, pady=5)
        tk.Radiobutton(self.root, text="Bank Account", variable=self.payment_method_var, value="Bank",
                       font=("Helvetica", 12), bg="#E6F7FF").pack(fill="x", padx=10, pady=5)
    def show_summary(self):
        self.summary_text.delete(1.0, tk.END)  # Clear previous text

        # Show Transactions
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()

        if transactions:
            self.summary_text.insert(tk.END, "\nTransactions:\n")
            for transaction in transactions:
                timestamp = datetime.datetime.strptime(transaction[4], '%Y-%m-%d %H:%M:%S')
                formatted_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                result = f"{formatted_date} - Type: {transaction[1]}, Amount: ${transaction[2]}, Person: {transaction[3]}\n"
                self.summary_text.insert(tk.END, result)
