from enum import Enum

class Categories(Enum):
    FOOD = 'Food'
    BILLS = 'Bills'
    CLOTHING = 'Clothing'
    ENTERTAIN = 'Entertainment'
    TRANSPORT = 'Transport'
    ACTIVITIES = 'Activities'
    OTHER = 'Other'

    @classmethod
    def from_string(cls, string):
        if not string:
            raise ValueError(f"Category is empty")

        for member in cls:
            if member.value.lower() == string.strip().lower():
                return member

        allowed = ", ".join(member.value for member in cls)
        raise ValueError(f"{string} is not a valid category\n"
                         f"Allowed categories: {allowed}")

    def __str__(self):
        return self.value

