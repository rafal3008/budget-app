from io_handler import json_handler as handler

class BudgetManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = handler.load_data(self.file_path)

    def add_entry(self, entry, entry_type="expenses"):
        if entry_type not in self.data:
            raise ValueError(f"{entry_type} is not a valid entry type")
        self.data[entry_type].append(entry.to_dict())
        handler.save_data(self.file_path, self.data)

    def get_entries(self, entry_type="expenses"):
        if entry_type not in self.data:
            raise ValueError(f"{entry_type} is not a valid entry type")
        return self.data[entry_type]
