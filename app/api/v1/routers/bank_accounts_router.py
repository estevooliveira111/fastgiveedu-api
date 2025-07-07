from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.schemas.bank_account_schema import (
    BankAccountCreate,
    BankAccountOut,
    PaginatedBankAccountOut,
    BankAccountUpdate,
)
from app.crud import bank_account as crud
from app.api import deps
from app.models.bank_account_model import BankAccount
from app.models.polo_model import Polo

router = APIRouter()


@router.post("/create", response_model=BankAccountOut)
def create(
    account: BankAccountCreate,
    polo_id: Optional[int] = None,
    db: Session = Depends(deps.get_db),
):
    db_account = crud.create_bank_account(db, account)

    if polo_id is not None:
        polo = crud.get_polo_by_id(db, polo_id)
        if not polo:
            raise HTTPException(status_code=404, detail="Polo não encontrado")
        polo.bank_accounts.append(db_account)
        db.commit()
        db.refresh(db_account)

    return crud.create_bank_account(db, account)


@router.get("/list", response_model=PaginatedBankAccountOut)
def list_bank_accounts(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    polo_id: Optional[int] = Query(None, description="ID do polo para filtrar contas"),
    db: Session = Depends(deps.get_db),
):
    skip = (page - 1) * page_size
    total_query = db.query(BankAccount)
    if polo_id is not None:
        total_query = total_query.join(BankAccount.polos).filter(Polo.id == polo_id)
    total = total_query.count()
    return {
        "data": crud.get_bank_accounts_paginated(
            db, skip=skip, limit=page_size, polo_id=polo_id
        ),
        "page": page,
        "page_size": page_size,
        "total_pages": (total + page_size - 1),
        "total_items": total,
    }


@router.get("/get/{account_id}", response_model=BankAccountOut)
def get(account_id: int, db: Session = Depends(deps.get_db)):
    account = crud.get_bank_account(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account


@router.put("/update/{account_id}", response_model=BankAccountOut)
def update(
    account_id: int, update_data: BankAccountUpdate, db: Session = Depends(deps.get_db)
):
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
