from typing import Optional
from sqlalchemy.orm import Session
from app.models.bank_account_model import BankAccount
from app.models.polo_model import Polo
from app.schemas.bank_account_schema import BankAccountCreate, BankAccountUpdate

def count_bank_accounts(db: Session) -> int:
    return db.query(BankAccount).count()

def get_bank_accounts_paginated(
    db: Session, skip: int = 0, limit: int = 10, polo_id: Optional[int] = None
):
    query = db.query(BankAccount)
    if polo_id is not None:
        query = query.join(BankAccount.polos).filter(Polo.id == polo_id)
    return query.offset(skip).limit(limit).all()

def get_bank_account_by_id(db: Session, account_id: int):
    return db.query(BankAccount).filter(BankAccount.id == account_id).first()



def create_bank_account(db: Session, account_in: BankAccountCreate):
    db_account = BankAccount(**account_in.dict(exclude={"polo_id"}))
    db.add(db_account)
    db.commit()
    db.refresh(db_account)

    if account_in.polo_id:
        polo = db.query(Polo).filter(Polo.id == account_in.polo_id).first()
        if polo:
            polo.bank_accounts.append(db_account)
            db.commit()
            db.refresh(db_account)
    return db_account



def update_bank_account(
    db: Session, account_id: int, account_update: BankAccountUpdate
):
    db_account = get_bank_account_by_id(db, account_id)
    if not db_account:
        return None
    for key, value in account_update.dict(exclude_unset=True).items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return db_account


def delete_bank_account(db: Session, account_id: int):
    db_account = get_bank_account_by_id(db, account_id)
    if not db_account:
        return None
    db.delete(db_account)
    db.commit()
    return db_account
