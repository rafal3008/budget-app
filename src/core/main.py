from core.manager import BudgetManager
from core.budget import BudgetEntry


FILE_PATH = "../data/budget.json"

manager = BudgetManager(FILE_PATH)
new_entry = BudgetEntry(100, "Pranie", "25.06.2025", "Test3")
manager.add_entry(new_entry)

