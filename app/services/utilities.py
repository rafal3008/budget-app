from datetime import date

from src.io_handler import json_handler
from src.core.constants import DATA_PATH



def check_data_shape(data):
    if not isinstance(data, dict):
        return {"entries": []}
    if "entries" not in data or not isinstance(data.get("entries"), list):
        data["entries"] = []
    return data


def _load():
    try:
        data = json_handler.load_data(DATA_PATH)
    except Exception:
        data = {"entries": []}
    return check_data_shape(data)

def _save(data):
    json_handler.save_data(DATA_PATH, data)


def serialize_amount(amount):
    """
    Keeps the amount in file as string
    """
    return str(amount)

def serialize_date(dt):
    try:
        return dt.isoformat()
    except Exception:
        return str(dt)


def match_filters(entry, category, from_date, to_date):
    """
    Check if the entry matches the given filters.
    """
    if category is not None and entry.get("category") != category:
        return False
    try:
        entry_date = date.fromisoformat(entry.get["date"])
    except Exception:
        return False

    if from_date is not None and entry_date < from_date:
        return False
    if to_date is not None and entry_date > to_date:
        return False
    return True

def find_index(data, entry_id):
    """
    Find the index of an entry by its ID.
    """
    for index, entry in enumerate(data):
        if entry.get("id") == entry_id:
            return index
    return None
