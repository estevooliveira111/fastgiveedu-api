from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.charge import ChargeCreate, ChargeUpdate, ChargeOut
from app.crud import charge as crud
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[ChargeOut])
def list_charges(db: Session = Depends(deps.get_db)):
    return crud.get_all_charges(db)

@router.get("/{charge_id}", response_model=ChargeOut)
def get_charge(charge_id: int, db: Session = Depends(deps.get_db)):
    charge = crud.get_charge_by_id(db, charge_id)
    if not charge:
        raise HTTPException(status_code=404, detail="Charge not found")
    return charge

@router.post("/", response_model=ChargeOut, status_code=status.HTTP_201_CREATED)
def create_charge(charge: ChargeCreate, db: Session = Depends(deps.get_db)):
    return crud.create_charge(db, charge)

@router.put("/{charge_id}", response_model=ChargeOut)
def update_charge(charge_id: int, charge: ChargeUpdate, db: Session = Depends(deps.get_db)):
    return crud.update_charge(db, charge_id, charge)

@router.delete("/{charge_id}", response_model=ChargeOut)
def delete_charge(charge_id: int, db: Session = Depends(deps.get_db)):
    return crud.delete_charge(db, charge_id)
