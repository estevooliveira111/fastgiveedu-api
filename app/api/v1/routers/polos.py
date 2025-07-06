from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.polo import PoloCreate, PoloUpdate, PoloOut
from app.crud import polo as crud_polo
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[PoloOut])
def read_polos(db: Session = Depends(deps.get_db)):
    return crud_polo.get_all_polos(db)

@router.get("/{polo_id}", response_model=PoloOut)
def read_polo(polo_id: int, db: Session = Depends(deps.get_db)):
    polo = crud_polo.get_polo_by_id(db, polo_id)
    if not polo:
        raise HTTPException(status_code=404, detail="Polo não encontrado")
    return polo

@router.post("/", response_model=PoloOut, status_code=status.HTTP_201_CREATED)
def create_polo(polo: PoloCreate, db: Session = Depends(deps.get_db)):
    return crud_polo.create_polo(db, polo)

@router.put("/{polo_id}", response_model=PoloOut)
def update_polo(polo_id: int, polo: PoloUpdate, db: Session = Depends(deps.get_db)):
    updated = crud_polo.update_polo(db, polo_id, polo)
    if not updated:
        raise HTTPException(status_code=404, detail="Polo não encontrado")
    return updated

@router.delete("/{polo_id}", response_model=PoloOut)
def delete_polo(polo_id: int, db: Session = Depends(deps.get_db)):
    deleted = crud_polo.delete_polo(db, polo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Polo não encontrado")
    return deleted
