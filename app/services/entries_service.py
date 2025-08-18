import uuid
from datetime import date
from decimal import Decimal
from app.services.utilities import (
    _load,
    _save,
    serialize_amount,
    serialize_date,
    match_filters,
    find_index )
from src.core.schemas import Entry, CreateEntry, UpdateEntry

def list_entries(category, from_date, to_date, page, limit):
    data = _load()
    rows = [e for e in data["entries"] if match_filters(e, category, from_date, to_date)]
    rows.sort(key=lambda e: e.get("date",""), reverse=True)
    start = (page-1) * limit
    end = start + limit

    sliced_rows = rows[start:end]

    result = []

    for e in sliced_rows:
        entry = Entry(
            id=e["id"],
            amount=Decimal(e["amount"]),
            date=date.fromisoformat(e["date"]),
            category=e["category"],
            note=e.get("note")
        )
        result.append(entry)
    return result


def create_entry(entry):
    data = _load()

    new_entry = {
        "id": str(uuid.uuid4()),
        "amount": serialize_amount(entry.amount),
        "date": serialize_date(entry.date),
        "category": entry.category,
        "note": entry.note
    }

    data["entries"].append(new_entry)
    _save(data)

    return Entry(
        id=new_entry["id"],
        amount=Decimal(new_entry["amount"]),
        date=date.fromisoformat(new_entry["date"]),
        category=new_entry["category"],
        note=new_entry.get("note")
    )

def update_entry(entry_id, entry):
    data = _load()

    index = find_index(data["entries"], entry_id)
    if index is None:
        return None

    existing_entry = data["entries"][index]

    if entry.amount is not None:
        existing_entry["amount"] = serialize_amount(entry.amount)
    if entry.date is not None:
        existing_entry["date"] = serialize_date(entry.date)
    if entry.category is not None:
        existing_entry["category"] = entry.category
    if entry.note is not None:
        existing_entry["note"] = entry.note

    _save(data)

    return Entry(
        id=existing_entry["id"],
        amount=Decimal(existing_entry["amount"]),
        date=date.fromisoformat(existing_entry["date"]),
        category=existing_entry["category"],
        note=existing_entry.get("note")
    )

def delete_entry(entry_id):
    data = _load()

    index = find_index(data["entries"], entry_id)
    if index is None:
        return False
    data["entries"].pop(index)
    _save(data)
    return True

def get_entry_or_404(entry_id):
    data = _load()

    index = find_index(data["entries"], entry_id)
    if index is None:
        return None

    entry = data["entries"][index]

    return Entry(
        id=entry["id"],
        amount=Decimal(entry["amount"]),
        date=date.fromisoformat(entry["date"]),
        category=entry["category"],
        note=entry.get("note")
    )

