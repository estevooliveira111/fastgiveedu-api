from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.payment import PaymentCreate, PaymentUpdate, PaymentOut
from app.crud import payment as crud
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[PaymentOut])
def list_payments(db: Session = Depends(deps.get_db)):
    return crud.get_all_payments(db)

@router.get("/{payment_id}", response_model=PaymentOut)
def get_payment(payment_id: int, db: Session = Depends(deps.get_db)):
    payment = crud.get_payment_by_id(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.post("/create", response_model=PaymentOut, status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentCreate, db: Session = Depends(deps.get_db)):
    return crud.create_payment(db, payment)

@router.put("/{payment_id}", response_model=PaymentOut)
def update_payment(payment_id: int, payment: PaymentUpdate, db: Session = Depends(deps.get_db)):
    return crud.update_payment(db, payment_id, payment)

@router.delete("/{payment_id}", response_model=PaymentOut)
def delete_payment(payment_id: int, db: Session = Depends(deps.get_db)):
    return crud.delete_payment(db, payment_id)