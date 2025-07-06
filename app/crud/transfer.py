from sqlalchemy.orm import Session
from typing import Optional
from app.models.transfer import Transfer
from app.schemas.transfer import TransferCreate, TransferUpdate

def get_transfer(db: Session, transfer_id: int) -> Optional[Transfer]:
    return db.query(Transfer).filter(Transfer.id == transfer_id).first()

def get_all_transfers(db: Session) -> list[Transfer]:
    return db.query(Transfer).all()

def create_transfer(db: Session, transfer_in: TransferCreate) -> Transfer:
    db_transfer = Transfer(**transfer_in.dict())
    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)
    return db_transfer

def update_transfer(db: Session, transfer_id: int, transfer_in: TransferUpdate) -> Optional[Transfer]:
    db_transfer = get_transfer(db, transfer_id)
    if not db_transfer:
        return None
    update_data = transfer_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_transfer, key, value)
    db.commit()
    db.refresh(db_transfer)
    return db_transfer

def delete_transfer(db: Session, transfer_id: int) -> Optional[Transfer]:
    db_transfer = get_transfer(db, transfer_id)
    if not db_transfer:
        return None
    db.delete(db_transfer)
    db.commit()
    return db_transfer