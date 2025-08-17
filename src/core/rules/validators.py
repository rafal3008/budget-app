from datetime import datetime, date
from decimal import Decimal, InvalidOperation

from src.core.categories import Categories
from src.core.constants import (
    MIN_AMOUNT,
    MAX_AMOUNT,
    AMOUNT_DECIMAL_PLACES,
    ERR_AMOUNT_RANGE,
    ERR_AMOUNT_POSITIVE,
    ERR_AMOUNT_DECIMALS,
    ERR_CATEGORY_INVALID,
    DATE_FORMAT,
    ERR_DATE_FORMAT,
    ERR_DATE_FUTURE_NOT_ALLOWED,
    ALLOW_FUTURE_DATE,
    ALLOWED_DATE_INPUT_FORMATS

)


def _to_decimal(value):
    if isinstance(value, Decimal):
        return value
    if isinstance(value, int):
        return Decimal(value)
    if isinstance(value, float):
        return Decimal(str(value))
    if isinstance(value, str):
        return Decimal(value.strip().replace(",", "."))
    raise ValueError(ERR_AMOUNT_RANGE)

def _format_amount(value):
    return f"{value:.{AMOUNT_DECIMAL_PLACES}f}"


def validate_amount(amount):
    """
    WHAT IT SHOULD CHECK:
    1. If amount is even a number
    2. If amount not smaller than 0
    """

    try:
        x = _to_decimal(amount)
    except (InvalidOperation, ValueError):
        raise ValueError(ERR_AMOUNT_RANGE)

    if x <= 0:
        raise ValueError(ERR_AMOUNT_POSITIVE)

    tup = x.as_tuple()
    dec_places = max(0, -tup.exponent)
    if dec_places > AMOUNT_DECIMAL_PLACES:
        raise ValueError(ERR_AMOUNT_DECIMALS)

    if x < MIN_AMOUNT or x > MAX_AMOUNT:
        raise ValueError(ERR_AMOUNT_RANGE)

def validate_date(date_str):
    """
    VALIDATES DATE
    It should allow both YYYY-MM-DD and DD-MM-YYYY
    also with "/" "." and just numbers
    """

    if isinstance(date_str, date) and not isinstance(date_str, datetime):
        dt = datetime.combine(date_str, datetime.min.time())
    elif isinstance(date_str, datetime):
        dt = date_str
    elif isinstance(date_str, str):
        raw_date = datetime.stip()
        parsed_date = None
        for fmt in ALLOWED_DATE_INPUT_FORMATS:
            try:
                parsed_date = datetime.strptime(raw_date, fmt)
                break
            except ValueError:
                continue
        if parsed_date is None:
            raise ValueError(ERR_DATE_FORMAT.replace("YYYY-MM-DD", DATE_FORMAT))
        dt = parsed_date

    else:
        raise ValueError(ERR_DATE_FORMAT.replace("YYYY-MM-DD", DATE_FORMAT))

    val_date = dt.date()

    if not ALLOW_FUTURE_DATE and val_date > date.today():
        raise ValueError(ERR_DATE_FUTURE_NOT_ALLOWED)

    return val_date.strftime("%Y-%m-%d")


def validate_category(category):

    if not isinstance(category, str):
        allowed = ", ".join(c.value for c in Categories)
        raise ValueError(f"{ERR_CATEGORY_INVALID}{allowed}")

    try:
        cat = Categories.from_string(category.strip())
    except Exception:
        allowed = ", ".join(c.value for c in Categories)
        raise ValueError(f"{ERR_CATEGORY_INVALID}{allowed}")

    return cat.value



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


