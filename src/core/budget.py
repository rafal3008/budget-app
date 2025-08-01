
class BudgetEntry:
    def __init__(self, amount, category, timestamp, note=""):
        self.amount = amount
        self.category = category
        self.timestamp = timestamp
        self.note = note

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "timestamp": self.timestamp,
            "note": self.note
        }
