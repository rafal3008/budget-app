from pydantic import BaseModel, field_validator, ConfigDict
from typing import Optional
from decimal import Decimal
from datetime import date
from src.core.rules.validators import (
validate_amount,
validate_category,
validate_date,
)

class _CommonModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid" #error when entering a non-existent field
    )

class EntryBase(_CommonModel):
    """
    Common filed for every budget-entry
    """
    amount: Decimal
    date: date
    category: str
    note: Optional[str] = None


    @field_validator("amount", mode="before")
    @classmethod
    def _amount(cls, value):
        return validate_amount(value)

    @field_validator("date", mode="before")
    @classmethod
    def _date(cls, value):
        return validate_date(value)

    @field_validator("category", mode="before")
    @classmethod
    def _category(cls, value):
        return validate_category(value)

class CreateEntry(EntryBase):
    pass

class UpdateEntry(EntryBase):
    amount: Optional[Decimal] = None
    date: Optional[date] = None
    category: Optional[str] = None
    note: Optional[str] = None


    @field_validator("amount", mode="before")
    @classmethod
    def _amount(cls, amt):
        if amt is None:
            return amt
        return validate_amount(amt)

    @field_validator("date", mode="before")
    @classmethod
    def _date(cls, dt):
        if dt is None:
            return dt
        return validate_date(dt)

    @field_validator("category", mode="before")
    @classmethod
    def _category(cls, cat):
        if cat is None:
            return cat
        return validate_category(cat)

class Entry(EntryBase):
    """
    Full entry
    """
    id: str