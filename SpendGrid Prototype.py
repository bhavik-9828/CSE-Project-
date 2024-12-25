import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime
from PIL import Image, ImageTk
import random

class SpendGridApp:
    def __init__(self, root):  # Corrected __init__
        self.root = root
        self.root.title("SpendGrid - FinTech App")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.configure("TNotebook.Tab", font=("Arial", 14, "bold"), padding=[10, 5])
        style.configure("TNotebook", tabmargins=[10, 5, 10, 0])

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        self.create_home_tab()
        self.create_expenditure_tab()
        self.create_earnings_tab()
        self.create_savings_tab()

    def create_home_tab(self):
        home_tab = ttk.Frame(self.notebook)
        self.notebook.add(home_tab, text="Home")

        profile_frame = tk.Frame(home_tab, bg="#2E2E2E", pady=20)
        profile_frame.pack(fill="x", padx=20)

    
        img = Image.open("profile_placeholder.jpg")  # Ensure the file exists
        img = img.resize((100, 100))
        self.profile_pic = ImageTk.PhotoImage(img)
        profile_label = tk.Label(profile_frame, image=self.profile_pic, bg="#2E2E2E")
        profile_label.grid(row=0, column=0, rowspan=3, padx=20)
        
        tk.Label(
            profile_frame,
            text="User Name: Arya Pratap",
            font=("Arial", 16),
            bg="#2E2E2E",
            fg="white",
        ).grid(row=0, column=1, sticky="w")
        tk.Label(
            profile_frame,
            text="Account Balance: ₹1,70,000",
            font=("Arial", 16),
            bg="#2E2E2E",
            fg="white",
        ).grid(row=1, column=1, sticky="w")
        tk.Label(
            profile_frame,
            text="Bank: ICICI Bank Ltd.",
            font=("Arial", 16),
            bg="#2E2E2E",
            fg="white",
        ).grid(row=2, column=1, sticky="w")

        logout_button = tk.Button(
            home_tab,
            text="Logout",
            command=self.logout,
            font=("Arial", 14, "bold"),
            bg="#D32F2F",
            fg="white",
            width=20,
            height=2,
            relief="raised",
        )
        logout_button.pack(pady=20, side="bottom")

    def logout(self):
        self.root.quit()

    def create_expenditure_tab(self):
        expenditure_tab = ttk.Frame(self.notebook)
        self.notebook.add(expenditure_tab, text="Expenditure")

        self.month_notebook = ttk.Notebook(expenditure_tab)
        self.month_notebook.pack(fill="both", expand=True)

        for month_index in range(1, 13):
            self.create_month_tab(month_index)

    def create_month_tab(self, month_index):
        month_tab = ttk.Frame(self.month_notebook)
        self.month_notebook.add(month_tab, text=calendar.month_name[month_index][:3])

        expenditure_data = self.get_predefined_expenditure_data(month_index)

        self.create_custom_calendar(month_tab, month_index, expenditure_data)

    def create_earnings_tab(self):
        earnings_tab = ttk.Frame(self.notebook)
        self.notebook.add(earnings_tab, text="Earnings")

        tk.Label(
            earnings_tab, text="Earnings Overview", font=("Arial", 18, "bold")
        ).pack(pady=20)

        earnings_statements = [
            "Salary - ₹80,000",
            "Rent from Tenant - ₹12,000",
            "Return on Stocks - ₹4,000",
            "Side Business - ₹5,000"
        ]

        earnings_frame = tk.Frame(earnings_tab, bg="#2E2E2E", padx=20, pady=10)
        earnings_frame.pack(fill="both", expand=True)

        for statement in earnings_statements:
            label = tk.Label(
                earnings_frame,
                text=f"• {statement}",
                font=("Arial", 12),
                fg="white",
                bg="#2E2E2E",
                wraplength=600,
                justify="left"
            )
            label.pack(pady=5, anchor="w")

    def create_savings_tab(self):
        savings_tab = ttk.Frame(self.notebook)
        self.notebook.add(savings_tab, text="Savings")

        tk.Label(
            savings_tab, text="Savings Overview", font=("Arial", 18, "bold")
        ).pack(pady=20)

        savings_statements = [
            "Saved ₹500 by reducing monthly subscription services.",
            "Cut down on dining out, saving ₹2000 this month.",
            "Reduced electricity bill by ₹1000 with energy-saving appliances.",
            "Refrained from impulse shopping, saving ₹1500.",
            "Saved ₹3000 by switching to a cheaper mobile plan.",
            "Consolidated loans and saved ₹2500 in interest.",
            "Reduced commuting costs by ₹1000 through carpooling.",
            "Optimized groceries, saving ₹800 on monthly spending.",
            "Built an emergency fund of ₹5000 this month.",
            "Achieved a 10% increase in monthly savings by budgeting effectively."
        ]

        random.shuffle(savings_statements)

        savings_frame = tk.Frame(savings_tab, bg="#2E2E2E", padx=20, pady=10)
        savings_frame.pack(fill="both", expand=True)

        for statement in savings_statements:
            label = tk.Label(
                savings_frame,
                text=f"• {statement}",
                font=("Arial", 12),
                fg="white",
                bg="#2E2E2E",
                wraplength=600,
                justify="left"
            )
            label.pack(pady=5, anchor="w")

    def get_predefined_expenditure_data(self, month):
        data = {}
        predefined_dates = {
            1: [5, 12, 18, 22, 25, 28, 30],
            2: [3, 7, 12, 16, 18, 23, 27],
            3: [4, 8, 12, 15, 19, 21, 26],
            4: [2, 6, 10, 14, 18, 21, 24],
            5: [1, 4, 9, 13, 17, 22, 26],
            6: [3, 7, 10, 14, 18, 21, 25],
            7: [2, 6, 9, 13, 16, 20, 23],
            8: [1, 4, 8, 11, 15, 19, 22],
            9: [2, 6, 9, 13, 17, 21, 25],
            10: [3, 7, 11, 14, 18, 21, 28],
            11: [5, 8, 12, 16, 19, 22, 29],
            12: [1, 4, 7, 10, 14, 19, 22],
        }

        expenses = [
            ("Coffee", 100), 
            ("Groceries", 3000), 
            ("EMI", 10000),
            ("Stationery", 300),
            ("Fuel", 3000),
            ("Recharge", 300),
            ("WiFi",500),
        ]
        
        expense_index = 0
        for day in predefined_dates[month]:
            data[day] = f"₹{expenses[expense_index][1]} - {expenses[expense_index][0]}"
            expense_index = (expense_index + 1) % len(expenses)

        return data

    def create_custom_calendar(self, parent, month, expenditure_data):
        now = datetime.now()
        year = now.year

        calendar_frame = tk.Frame(parent, bg="#2E2E2E")
        calendar_frame.pack(expand=True, fill="both")

        canvas = tk.Canvas(calendar_frame, bg="#2E2E2E", highlightthickness=0)
        canvas.pack(expand=True, fill="both")

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days_in_month = calendar.monthrange(year, month)[1]
        first_weekday = calendar.monthrange(year, month)[0]

        canvas_width = 800
        canvas_height = 500
        cell_width = canvas_width // 7
        cell_height = canvas_height // 7

        for col, day in enumerate(days):
            x = col * cell_width
            y = 0
            canvas.create_rectangle(
                x, y, x + cell_width, y + cell_height, fill="#3A3A3A", outline="#555555"
            )
            canvas.create_text(
                x + cell_width // 2,
                y + cell_height // 2,
                text=day,
                fill="#FFFFFF",
                font=("Arial", 12, "bold"),
                width=cell_width,
                anchor="center",
                justify="center"
            )

        row, col = 1, first_weekday
        for day in range(1, days_in_month + 1):
            x = col * cell_width
            y = row * cell_height
            canvas.create_rectangle(
                x, y, x + cell_width, y + cell_height, fill="#3A3A3A", outline="#555555"
            )
            canvas.create_text(
                x + 10,
                y + 10,
                text=str(day),
                fill="#FFFFFF",
                font=("Arial", 10, "bold"),
                anchor="nw",
            )
            if day in expenditure_data:
                canvas.create_text(
                    x + 5,
                    y + 25,
                    text=expenditure_data[day],
                    fill="#FFFFFF",
                    font=("Arial", 10),
                    anchor="nw",
                )

            col += 1
            if col > 6:
                col = 0
                row += 1


def main():
    root = tk.Tk()
    app = SpendGridApp(root)
    root.mainloop()


if __name__ == "__main__":  # Corrected __name__ check
    main()
