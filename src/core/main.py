from .budget import *
from io_handler.json_handler import load_data, save_data


FILE_PATH = "../data/budget.json"

data = load_data(FILE_PATH)

new_entry = BudgetEntry(100, "Pranie", "25.06.2025", "Teścik")

print(data)

data['expenses'].append(new_entry.to_dict())

print(data)
