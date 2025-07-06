from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.transfer import TransferCreate, TransferUpdate, TransferOut
from app.crud import transfer as crud
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[TransferOut])
def list_transfers(db: Session = Depends(deps.get_db)):
    return crud.get_all_transfers(db)

@router.get("/{transfer_id}", response_model=TransferOut)
def get_transfer(transfer_id: int, db: Session = Depends(deps.get_db)):
    transfer = crud.get_transfer_by_id(db, transfer_id)
    if not transfer:
        raise HTTPException(status_code=404, detail="Transfer not found")
    return transfer

@router.post("/", response_model=TransferOut, status_code=status.HTTP_201_CREATED)
def create_transfer(transfer: TransferCreate, db: Session = Depends(deps.get_db)):
    return crud.create_transfer(db, transfer)

@router.put("/{transfer_id}", response_model=TransferOut)
def update_transfer(transfer_id: int, transfer: TransferUpdate, db: Session = Depends(deps.get_db)):
    return crud.update_transfer(db, transfer_id, transfer)

@router.delete("/{transfer_id}", response_model=TransferOut)
def delete_transfer(transfer_id: int, db: Session = Depends(deps.get_db)):
    return crud.delete_transfer(db, transfer_id)
