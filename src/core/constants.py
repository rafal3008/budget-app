"""
ALL CONSTANTS I CAN THINK OF - I SAW IT IN ANOTHER PROJECT, AND SAID - WHY NOT?
"""
from decimal import Decimal

#File paths
DATA_PATH: str = "data/budget.json"

#AMOUNT
MIN_AMOUNT: Decimal =  Decimal("0.01")
MAX_AMOUNT: Decimal = Decimal("1000000")

AMOUNT_DECIMAL_PLACES: int = 2

ERR_AMOUNT_POSITIVE: str = "Amount must be positive"
ERR_AMOUNT_RANGE: str = f"Amount should be between {MIN_AMOUNT} and {MAX_AMOUNT}"

ERR_AMOUNT_DECIMALS = str = "The amount should have a maximum of two decimal places"


#Category
#See categories.py for allowed categories
ERR_CATEGORY_INVALID: str = "Category invalid. Allowed categories: "


#Date
ALLOWED_DATE_INPUT_FORMATS = (
    "%Y-%m-%d",  # 2025-08-18
    "%d.%m.%Y",  # 18.08.2025
    "%d/%m/%Y",  # 18/08/2025
    "%Y/%m/%d",  # 2025/08/18
    "%Y.%m.%d",  # 2025.08.18
)


DATE_FORMAT: str = "YYYY-MM-DD"
ALLOW_FUTURE_DATE: bool = False


ERR_DATE_FORMAT: str = f"Date format must be {DATE_FORMAT}"
ERR_DATE_FUTURE_NOT_ALLOWED: str = "Cannot add future expenses"

#for API pagination
DEFAULT_PAGE = 1
DEFAULT_LIMIT = 50
MAX_LIMIT = 500