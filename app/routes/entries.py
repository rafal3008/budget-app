from datetime import date
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query

from src.core.schemas import Entry, CreateEntry, UpdateEntry
from app.services.entries_service import (
    list_entries,
    create_entry,
    update_entry,
    delete_entry,
    get_entry_or_404
)
from src.core.constants import DEFAULT_PAGE, DEFAULT_LIMIT, MAX_LIMIT

router = APIRouter()

@router.get("", response_model=List[Entry])
def get_entries(
    category: Optional[str] = Query(None, description="Filter by category"),
    from_date: Optional[date] = Query(None, description="Filter entries from this date"),
    to_date: Optional[date] = Query(None, description="Filter entries to this date"),
    page: int = Query(DEFAULT_PAGE, ge=1, description="Page number for pagination"),
    limit: int = Query(DEFAULT_LIMIT, ge=1, le=MAX_LIMIT, description="Number of entries per page")
):

    return list_entries(category, from_date, to_date, page, limit)

@router.post("", response_model=Entry, status_code=201)
def post_entry(entry: CreateEntry):
    return create_entry(entry)

@router.get("/{entry_id}", response_model=Entry)
def get_entry(entry_id: str):
    entry = get_entry_or_404(entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

@router.put("/{entry_id}", response_model=Entry)
def put_entry(entry_id: str, entry: UpdateEntry):
    updated_entry = update_entry(entry_id, entry)
    if not updated_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return updated_entry

@router.delete("/{entry_id}", status_code=204)
def delete_entry_by_id(entry_id: str):
    if not delete_entry(entry_id):
        raise HTTPException(status_code=404, detail="Entry not found")
    return None