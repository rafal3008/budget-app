from core.manager import BudgetManager
from core.budget import BudgetEntry
from dateutil.parser import parse


FILE_PATH = "../data/budget.json"

manager = BudgetManager(FILE_PATH)

while True:
    print("What would you like to do? 1 - add entry, 2 - show entries, 3 - exit")
    answer = input()
    match answer:
        case "1":
            print("Specify amount: ")
            amount = float(input())
            print("Expense category: ")
            category = input()
            print("Date of expense: ")
            date = parse(input()).strftime("%d.%m.%Y")
            print("Add note to expense: ")
            note = input()
            new_entry = BudgetEntry(amount, category, date, note)
            manager.add_entry(new_entry)
        case "2":
            print("Specify type of entry(income/expenses): ")
            entry_type = input().strip().lower()
            print(f"Current entries: {manager.get_entries()}\n")
            entries = manager.get_entries(entry_type)
            for e in entries:
                print(f"{e['timestamp']} - {e['category']} - {e['amount']} ({e['note']})")

        case "3":
            break


