from core.manager import BudgetManager
from core.budget import BudgetEntry
from dateutil.parser import parse
from datetime import datetime


FILE_PATH = "../data/budget.json"

manager = BudgetManager(FILE_PATH)

def entry_prompt():
    print("\n===Adding new entry===")
    amount = float(input("Amount: ")) or 0
    category = input("Category: ") or "N/A"
    date_str = input("Date: ") or str(datetime.now())
    date = parse(date_str).strftime("%d.%m.%Y")
    note = input("Note [optional]: ")
    return BudgetEntry(amount, category, date, note)

def filter_prompt():
    print("\n===Filtering entries=== ")
    entry_type = input("Type of entry(expenses/income): ").strip().lower() or "expenses"
    category = input("Category [optional]: ").strip() or None

    from_date_str = input("From (dd.mm.yyyy)[optional]: ").strip()
    from_date = parse(from_date_str) if from_date_str else None

    to_date_str = input("To (dd.mm.yyyy)[optional]: ").strip()
    to_date = parse(to_date_str) if to_date_str else None

    return entry_type, category, from_date, to_date

def display_entries(entries):
    print("\n===Found entries===")
    if not entries:
        print("No entries found.")
    for entry in entries:
        print(f"{entry['timestamp']} | {entry['category']} | {entry['amount']} | {entry['note']} ")

def summary_prompt():
    while True:
        entry_type = input("Type of entry(expenses/income): ").strip().lower()
        if entry_type in ("expenses", "income"):
            break
        print("Invalid type. Try 'expenses' or 'income'.")

    category = input("Category [optional]: ").strip() or None

    from_date_str = input("From (dd.mm.yyyy)[optional]: ").strip()
    from_date = parse(from_date_str) if from_date_str else None

    to_date_str = input("To (dd.mm.yyyy)[optional]: ").strip()
    to_date = parse(to_date_str) if to_date_str else None

    return entry_type, category, from_date, to_date


def main_menu():

    while True:
        print("\n====Budget-app text client - MAIN MENU====")
        print("1. Add new entry")
        print("2. Show entries(filtered)")
        print("3. Show summary report")
        print("4. Exit")

        answer = input("What would you like to do?: ").strip()

        match answer:
            case "1":
                entry = entry_prompt()
                entry_type = input("Type of entry(expenses/income): ").strip().lower() or "expenses"
                manager.add_entry(entry, entry_type)
                print("Added new entry")
            case "2":
                entry_type, category, from_date, to_date = filter_prompt()
                entries = manager.get_entries(entry_type, category, from_date, to_date)
                display_entries(entries)
            case "3":
                entry_type, category, from_date, to_date = summary_prompt()
                manager.print_summary(entry_type, category, from_date, to_date)



            case "4":
                print("Exiting")
                break
            case _:
                print("Invalid input. Try again")

if __name__ == "__main__":
    main_menu()


