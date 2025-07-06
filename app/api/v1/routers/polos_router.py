from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.schemas.polo_schema import PoloCreate, PoloUpdate, PoloOut, PaginatedPoloOut
from app.crud import polo as crud_polo
from app.api import deps

router = APIRouter()

@router.get("/list", response_model=PaginatedPoloOut)
def read_polos(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(deps.get_db)
):
    skip = (page - 1) * page_size
    total = crud_polo.count_polos(db)
    polos = crud_polo.get_polos_paginated(db, skip=skip, limit=page_size)
    return {
        "data": polos,
        "page": page,
        "page_size": page_size,
        "total_pages": (total + page_size - 1),
        "total_items": total
    }

@router.get("/get/{polo_id}", response_model=PoloOut)
def read_polo(polo_id: int, db: Session = Depends(deps.get_db)):
    polo = crud_polo.get_polo_by_id(db, polo_id)
    if not polo:
        raise HTTPException(status_code=404, detail="Polo não encontrado")
    return polo

@router.post("/create", response_model=PoloOut, status_code=status.HTTP_201_CREATED)
def create_polo(polo: PoloCreate, db: Session = Depends(deps.get_db)):
    return crud_polo.create_polo(db, polo)

@router.put("/update/{polo_id}", response_model=PoloOut)
def update_polo(polo_id: int, polo: PoloUpdate, db: Session = Depends(deps.get_db)):
    updated = crud_polo.update_polo(db, polo_id, polo)
    if not updated:
        raise HTTPException(status_code=404, detail="Polo não encontrado")
    return updated

@router.delete("/delete/{polo_id}", response_model=PoloOut)
def delete_polo(polo_id: int, db: Session = Depends(deps.get_db)):
    deleted = crud_polo.delete_polo(db, polo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Polo não encontrado")
    return deleted