from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.bank_account_schema import BankAccountCreate, BankAccountUpdate, BankAccountOut, PaginatedBankAccountOut
from app.crud import bank_account as crud
from app.api import deps

router = APIRouter()

@router.post("/create", response_model=BankAccountOut)
def create(account: BankAccountCreate, db: Session = Depends(deps.get_db)):
    return crud.create_bank_account(db, account)


@router.get("/list", response_model=PaginatedBankAccountOut)
def read_bank_accounts(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(deps.get_db)
):
    skip = (page - 1) * page_size
    total = crud.count_bank_accounts(db)
    bank_accounts = crud.get_bank_accounts_paginated(db, skip=skip, limit=page_size)
    total_pages = (total + page_size - 1)

    return {
        "data": bank_accounts,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "total_items": total
    }

@router.get("/get/{account_id}", response_model=BankAccountOut)
def get(account_id: int, db: Session = Depends(deps.get_db)):
    account = crud.get_bank_account(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account

@router.put("/update/{account_id}", response_model=BankAccountOut)
def update(account_id: int, update_data: BankAccountUpdate, db: Session = Depends(deps.get_db)):
    updated = crud.update_bank_account(db, account_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return updated

@router.delete("/delete/{account_id}", response_model=BankAccountOut)
def delete(account_id: int, db: Session = Depends(deps.get_db)):
    deleted = crud.delete_bank_account(db, account_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return deleted
