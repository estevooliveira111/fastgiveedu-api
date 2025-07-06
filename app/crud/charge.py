from sqlalchemy.orm import Session
from typing import Optional
from app.models.charge import Charge
from app.schemas.charge import ChargeCreate, ChargeUpdate

def get_charge(db: Session, charge_id: int) -> Optional[Charge]:
    return db.query(Charge).filter(Charge.id == charge_id).first()

def get_all_charges(db: Session) -> list[Charge]:
    return db.query(Charge).all()

def create_charge(db: Session, charge_in: ChargeCreate) -> Charge:
    db_charge = Charge(**charge_in.dict())
    db.add(db_charge)
    db.commit()
    db.refresh(db_charge)
    return db_charge

def update_charge(db: Session, charge_id: int, charge_in: ChargeUpdate) -> Optional[Charge]:
    db_charge = get_charge(db, charge_id)
    if not db_charge:
        return None
    update_data = charge_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_charge, key, value)
    db.commit()
    db.refresh(db_charge)
    return db_charge

def delete_charge(db: Session, charge_id: int) -> Optional[Charge]:
    db_charge = get_charge(db, charge_id)
    if not db_charge:
        return None
    db.delete(db_charge)
    db.commit()
    return db_charge
