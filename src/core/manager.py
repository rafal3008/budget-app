from io_handler import json_handler as handler
from dateutil.parser import parse

class BudgetManager:
    """
    A class to manage budget data, including expenses and income.
    Handles loading, saving, filtering, editing, and summarizing financial entries.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = handler.load_data(self.file_path)

    def add_entry(self, entry, entry_type="expenses"):
        """
        Add a new budget entry to the data.

        Args:
            entry (BudgetEntry): Entry object to be added.
            entry_type (str): Type of entry ('expenses' or 'income').

        Raises:
            ValueError: If entry_type is not recognized.
        """
        if entry_type not in self.data:
            raise ValueError(f"{entry_type} is not a valid entry type")
        self.data[entry_type].append(entry.to_dict())
        handler.save_data(self.file_path, self.data)

    def get_entries(self, entry_type="expenses", category=None, from_date=None, to_date=None):
        """
        Retrieve entries filtered by type, category, and optional date range.

        Args:
            entry_type (str): 'expenses' or 'income'.
            category (str, optional): Filter by category name.
            from_date (datetime, optional): Include entries from this date onward.
            to_date (datetime, optional): Include entries up to this date.

        Returns:
            list[tuple[int, dict]]: List of (index, entry) pairs.
        """
        if entry_type not in self.data:
            raise ValueError(f"{entry_type} is not a valid entry type")

        filtered_entries = []

        for id, entry in enumerate(self.data[entry_type]):
            try:
                entry_date = parse(entry["timestamp"])
            except Exception:
                continue

            if category and entry['category'] != category:
                continue
            if from_date and entry_date < from_date:
                continue
            if to_date and entry_date > to_date:
                continue


            filtered_entries.append((id, entry))



        return filtered_entries

    def get_summary(self, entry_type, category=None, from_date=None, to_date=None):
        """
        Generate a summary report for the selected entries.

        Args:
            entry_type (str): 'expenses' or 'income'.
            category (str, optional): Filter by category.
            from_date (datetime, optional): Filter entries from this date.
            to_date (datetime, optional): Filter entries to this date.

        Returns:
            dict or None: Summary with total amount, entry count, and category breakdown;
                          or None if no entries match.
        """
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
        """
        Print a formatted summary of the entries to the console.

        Args:
            entry_type (str): 'expenses' or 'income'.
            category (str, optional): Filter by category.
            from_date (datetime, optional): Filter from this date.
            to_date (datetime, optional): Filter to this date.
        """
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

    def delete_entry(self, entry_type, index, category=None, from_date=None, to_date=None):
        """
        Delete an entry from the filtered list by its index.

        Args:
            entry_type (str): 'expenses' or 'income'.
            index (int): Index of the entry in the filtered list to delete.
            category (str, optional): Optional filter by category.
            from_date (datetime, optional): Optional filter from date.
            to_date (datetime, optional): Optional filter to date.

        Effects:
            Updates stored data and saves changes to file.
        """
        filtered_entries = self.get_entries(entry_type, category, from_date, to_date)

        if not (0 <= index < len(filtered_entries)):
            print(f"Index {index} is out of range for {entry_type}")
            return

        org_index = filtered_entries[index][0]
        self.data[entry_type].pop(org_index)
        handler.save_data(self.file_path, self.data)
        print(f"Deleted {entry_type} entry {index}.")

    def edit_entry(self, entry_type, index, new_entry, category=None, from_date=None, to_date=None):
        """
        Edit an existing entry selected from filtered results.

        Args:
            entry_type (str): 'expenses' or 'income'.
            index (int): Index in the filtered list of entries.
            new_entry (BudgetEntry): The new entry to replace the old one.
            category (str, optional): Optional filter by category.
            from_date (datetime, optional): Optional filter from date.
            to_date (datetime, optional): Optional filter to date.

        Returns:
            bool: True if the entry was edited successfully, False otherwise.
        """
        filtered_entries = self.get_entries(entry_type, category, from_date, to_date)

        if not (0 <= index < len(filtered_entries)):
            print(f"Index {index} is out of range for filtered results")
            return False

        original_index = filtered_entries[index][0]
        self.data[entry_type][original_index] = new_entry.to_dict()
        handler.save_data(self.file_path, self.data)
        print('Entry edited successfully')
        return True


    def get_balance(self):
        expenses = sum(entry['amount'] for entry in self.data.get('expenses', []))
        income = sum(entry['amount'] for entry in self.data.get('income', []))
        return income - expenses

    def get_filtered_entries(self, entry_type, category=None, from_date=None, to_date=None):
        """
        Retrieve entries with optional filtering by category and date range.

        Args:
            entry_type (str): 'expenses' or 'income'.
            category (str, optional): Filter by category.
            from_date (datetime, optional): Start date for filtering.
            to_date (datetime, optional): End date for filtering.

        Returns:
            list[tuple[int, dict]]: List of (index, entry) pairs.

        Raises:
            ValueError: If entry_type is not recognized.
        """
        if entry_type not in self.data:
            raise ValueError(f"{entry_type} is not a valid entry type")

        filtered_entries = []
        for id, entry in enumerate(self.data[entry_type]):
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

            filtered_entries.append((id, entry))

        return filtered_entries


