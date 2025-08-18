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
    def from_string(cls, string):
        if not isinstance(string, str):
            raise ValueError(f"Category must be a string")

        raw_str = string.strip().lower()

        alias_map = {
            "food": cls.FOOD,
            "meal": cls.FOOD,
            "bills": cls.BILLS,
            "bill": cls.BILLS,
            "utilities": cls.BILLS,
            "utility": cls.BILLS,
            "clothing": cls.CLOTHING,
            "clothes": cls.CLOTHING,
            "entertainment": cls.ENTERTAINMENT,
            "entertain": cls.ENTERTAINMENT,
            "transport": cls.TRANSPORT,
            "transportation": cls.TRANSPORT,
            "activities": cls.ACTIVITIES,
            "activity": cls.ACTIVITIES,
            "other": cls.OTHER,
            "misc": cls.OTHER,
            "miscellaneous": cls.OTHER,
        }

        if raw_str in alias_map:
            return alias_map[raw_str]

        for member in cls:
            if member.value.lower() == raw_str:
                return member

        raise ValueError(f"Category is invalid: {raw_str}")

    def __str__(self):
        return self.value

