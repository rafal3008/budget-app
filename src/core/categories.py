from enum import Enum

class Categories(Enum):
    FOOD = 'Food'
    BILLS = 'Bills'
    CLOTHING = 'Clothing'
    ENTERTAINMENT = 'Entertainment'
    TRANSPORT = 'Transport'
    ACTIVITIES = 'Activities'
    OTHER = 'Other'

    @classmethod
    def from_string(cls, str):
        if not str:
            raise ValueError(f"Category is empty")

        for member in cls:
            if member.value.lower() == str.strip().lower():
                return member

        raise ValueError(f"Category is invalid: {str}")

    def __str__(self):
        return self.value

