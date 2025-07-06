from sqlalchemy.orm import Session
from typing import Optional
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentUpdate

def get_payment(db: Session, payment_id: int) -> Optional[Payment]:
    return db.query(Payment).filter(Payment.id == payment_id).first()

def get_all_payments(db: Session) -> list[Payment]:
    return db.query(Payment).all()

def create_payment(db: Session, payment_in: PaymentCreate) -> Payment:
    db_payment = Payment(**payment_in.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def update_payment(db: Session, payment_id: int, payment_in: PaymentUpdate) -> Optional[Payment]:
    db_payment = get_payment(db, payment_id)
    if not db_payment:
        return None
    update_data = payment_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_payment, key, value)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete_payment(db: Session, payment_id: int) -> Optional[Payment]:
    db_payment = get_payment(db, payment_id)
    if not db_payment:
        return None
    db.delete(db_payment)
    db.commit()
    return db_payment
