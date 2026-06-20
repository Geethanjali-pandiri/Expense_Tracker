import json
import os

FILE = "data.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {"income": 0, "expenses": [], "balance": 0}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

def add_income():
    amt = float(input("Enter income: "))
    data["income"] += amt
    data["balance"] += amt
    save_data(data)
    print("Income added!")

def add_expense():
    name = input("Expense name: ")
    amt = float(input("Amount: "))
    data["expenses"].append({"name": name, "amount": amt})
    data["balance"] -= amt
    save_data(data)
    print("Expense added!")

def show_balance():
    print("\n--- BALANCE ---")
    print("Income:", data["income"])
    print("Balance:", data["balance"])

def show_history():
    print("\n--- EXPENSE HISTORY ---")
    for e in data["expenses"]:
        print(f"{e['name']} - {e['amount']}")

while True:
    print("\n==== EXPENSE TRACKER ====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        show_history()
    elif choice == "5":
        break
    else:
        print("Invalid choice")