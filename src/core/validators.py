from datetime import datetime, date
from decimal import Decimal

from src.core.categories import Categories


def validate_amount(amount):
    """
    WHAT IT SHOULD CHECK:
    1. If amount is even a number
    2. If amount not smaller than 0
    """

    try:
        x = Decimal(amount)

    except ValueError:
        raise ValueError(f"{amount} is not a valid amount")

    if x < 0:
        raise ValueError(f"Amount can't be negative")
    else:
        return x

def validate_date(date_str):
    """
    VALIDATES DATE
    It should allow both YYYY-MM-DD and DD-MM-YYYY
    also with "/" "." and just numbers
    """

    if not date_str:
        raise ValueError("Date is required")

    raw_date = str(date_str).strip()
    y = m = d = None

    raw_date = date_str.strip()
    if raw_date.isdigit() and len(raw_date) == 8:
        year_candidate = int(raw_date[:4])
        if 1900 <= year_candidate < 2100:
            # YYYYMMDD format
            year, month, day = year_candidate, int(raw_date[4:6]), int(raw_date[6:8])
        else:
            day, month, year = int(raw_date[:2]), int(raw_date[2:4]), int(raw_date[4:8])


    else:
        #Used separators

        separator = None

        for sep in ("-", ".", "/"):
            if sep in raw_date:
                separator = sep
                break
        if not separator:
            raise ValueError(f"{date_str} is not a valid date format. Try YYYY-MM-DD or DD-MM-YYYY")

        parts = raw_date.split(separator)

        if len(parts) != 3:
            raise ValueError(f"{date_str} is not a valid date format")

        if len(parts[0])==4:
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        elif len(parts[2])==4:
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])

        else:
            raise ValueError(f"{date_str} is not a valid date format. Use YYYY-MM-DD or DD-MM-YYYY")

    try:
        parsed_date = date(year, month, day)
    except ValueError:
        raise ValueError(f"{date_str} is not a valid date")

    if parsed_date > date.today():
        raise ValueError(f"Date can't be in the future")

    return parsed_date



def validate_category(category):
    return Categories.from_string(category)



if __name__ == "__main__":
    try:
        print(validate_amount("123.45"))
        print(validate_amount("-10"))
    except ValueError as e:
        print("Error:", e)

    try:
        print(validate_date("2025-08-17"))  # 2025-08-17
        print(validate_date("17-08-2025"))  # 2025-08-17
        print(validate_date("17/08/2025"))  # 2025-08-17
        print(validate_date("2025/17/08"))  # not a valid date

    except ValueError as e:
        print("Error:", e)
    try:
        print(validate_date("17.08.2025"))  # 2025-08-17
        print(validate_date("20250817"))    # 2025-08-17
        print(validate_date("17082025"))    # 2025-08-17
        print(validate_date("08~17~2025"))  # not a valid date format. Try YYYY-MM-DD or DD-MM-YYYY

    except ValueError as e:
        print("Error:", e)


    try:
        print(validate_category("Food"))
        print(validate_category("food"))
        print(validate_category("car"))
    except ValueError as e:
        print("Error:", e)


