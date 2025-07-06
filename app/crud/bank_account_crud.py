from sqlalchemy.orm import Session
from app.models.bank_account_model import BankAccount
from app.schemas.bank_account_schema import BankAccountCreate, BankAccountUpdate

def create_account(db: Session, account: BankAccountCreate):
    db_account = BankAccount(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_all_accounts(db: Session):
    return db.query(BankAccount).all()

def get_account(db: Session, account_id: int):
    return db.query(BankAccount).filter(BankAccount.id == account_id).first()

def update_account(db: Session, account_id: int, data: BankAccountUpdate):
    acc = get_account(db, account_id)
    if not acc:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(acc, key, value)
    db.commit()
    db.refresh(acc)
    return acc

def delete_account(db: Session, account_id: int):
    acc = get_account(db, account_id)
    if not acc:
        return None
    db.delete(acc)
    db.commit()
    return acc
