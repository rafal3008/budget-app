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

    def print_summary(self, entry_type, category=None, from_date=None, to_date=None):

        entries = self.get_entries(entry_type, category, from_date, to_date)

        if not entries:
            print(f"No entries found for {entry_type}")
            return

        total = sum(entry['amount'] for entry in entries)
        count = len(entries)

        category_totals = {}
        for entry in entries:
            cat = entry.get('category', 'Uncategorized')
            category_totals[cat] = category_totals.get(cat, 0) + entry['amount']
        print(f"\n===Summary for {entry_type}===")
        print(f"Total entries: {count}")
        print(f"Total amount: {total:.2f}\n")

        print("By category:")
        for cat, amt in category_totals.items():
            print(f"{cat}: {amt:.2f}")
