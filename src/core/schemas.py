from pydantic import BaseModel, field_validator, ConfigDict
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
    amount: str
    date: str
    category: str


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
    pass

class Entry(EntryBase):
    """
    Full entry
    """
    id: str