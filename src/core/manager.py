from io_handler import json_handler as handler
from dateutil.parser import parse

class BudgetManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = handler.load_data(self.file_path)

    def add_entry(self, entry, entry_type="expenses"):
        if entry_type not in self.data:
            raise ValueError(f"{entry_type} is not a valid entry type")
        self.data[entry_type].append(entry.to_dict())
        handler.save_data(self.file_path, self.data)

    def get_entries(self, entry_type="expenses", category=None, from_date=None, to_date=None):
        if entry_type not in self.data:
            raise ValueError(f"{entry_type} is not a valid entry type")

        filtered_entries = []

        for entry in self.data[entry_type]:
            try:
                entry_date = parse(entry["timestamp"])
            except Exception:
                continue

            if category is not None and entry['category'] != category:
                continue
            if from_date is not None and entry_date < from_date:
                continue
            if to_date is not None and entry_date > to_date:
                continue

            filtered_entries.append(entry)

        return filtered_entries

    def get_summary(self, entry_type, category=None, from_date=None, to_date=None):
        entries = self.get_entries(entry_type, category, from_date, to_date)
        if not entries:
            return None
        total = sum(entry['amount'] for entry in entries)
        count = len(entries)

        category_totals = {}
        for entry in entries:
            cat = entry.get('category', 'Uncategorized')
            category_totals[cat] = category_totals.get(cat, 0) + entry['amount']

        return {
            "total_amount": total,
            "entries_count": count,
            "by_category": category_totals
        }
    def print_summary(self, entry_type, category=None, from_date=None, to_date=None):
        summary = self.get_summary(entry_type, category, from_date, to_date)

        if not summary:
            print(f"No entries found for {entry_type}")
            return

        print(f"\n===Summary for {entry_type}===")
        print(f"Total entries: {summary['entries_count']}")
        print(f"Total amount: {summary['total_amount']:.2f}\n")

        print("By category:")
        for cat, amt in summary['by_category'].items():
            print(f"{cat}: {amt:.2f}")

    def delete_entry(self, entry_type, index):
            if entry_type not in self.data:
                raise ValueError(f"{entry_type} is not a valid entry type")

            entries = self.data[entry_type]

            if not (0 <= index < len(entries)):
                print(f"Index {index} is out of range for {entry_type}")
                return

            entries.pop(index)
            handler.save_data(self.file_path, self.data)
            print('Entry deleted')

    def edit_entry(self, entry_type, index, new_entry):
        if entry_type not in self.data:
            raise ValueError(f"{entry_type} is not a valid entry type")

        entries = self.data[entry_type]

        if not (0 <= index < len(entries)):
            print(f"Index {index} is out of range for {entry_type}")
            return False

        entries[index] = new_entry.to_dict()
        handler.save_data(self.file_path, self.data)
        print('Entry edited successfully')
        return True

    def get_balance(self):
        expenses = sum(entry['amount'] for entry in self.data.get('expenses', []))
        income = sum(entry['amount'] for entry in self.data.get('income', []))
        return income - expenses




