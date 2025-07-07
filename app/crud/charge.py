from sqlalchemy.orm import Session
from typing import Optional
from app.models.charge_model import Charge
from app.models.charge_split_model import ChargeSplit
from app.schemas.charge_schema import ChargeCreate, ChargeUpdate
from app.schemas.charge_split_schema import ChargeSplitCreate

def get_charge(db: Session, charge_id: int) -> Optional[Charge]:
    return db.query(Charge).filter(Charge.id == charge_id).first()

def get_all_charges(db: Session) -> list[Charge]:
    return db.query(Charge).all()

def create_charge(db: Session, charge_in: ChargeCreate) -> Charge:
    new_charge = Charge(
        student_id=charge_in.student_id,
        student_name=charge_in.student_name,
        due_date=charge_in.due_date,
        amount=charge_in.amount,
        status=charge_in.status,
    )
    db.add(new_charge)
    db.commit()
    db.refresh(new_charge)

    if charge_in.splits:
        for split_in in charge_in.splits:
            split = ChargeSplit(
                charge_id=new_charge.id,
                bank_account_id=split_in.bank_account_id,
                polo_id=split_in.polo_id,
                account_name=split_in.account_name,
                amount=split_in.amount,
                amount_type=split_in.amount_type,
            )
            db.add(split)
        db.commit()

    db.refresh(new_charge)
    return new_charge


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
