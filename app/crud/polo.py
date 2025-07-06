from sqlalchemy.orm import Session
from app.models.polo import Polo
from app.schemas.polo_schema import PoloCreate, PoloUpdate

def count_polos(db: Session) -> int:
    return db.query(Polo).count()

def get_polos_paginated(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Polo).offset(skip).limit(limit).all()

def get_all_polos(db: Session):
    return db.query(Polo).all()

def get_polo_by_id(db: Session, polo_id: int):
    return db.query(Polo).filter(Polo.id == polo_id).first()

def create_polo(db: Session, polo: PoloCreate):
    db_polo = Polo(**polo.dict())
    db.add(db_polo)
    db.commit()
    db.refresh(db_polo)
    return db_polo

def update_polo(db: Session, polo_id: int, polo_update: PoloUpdate):
    db_polo = get_polo_by_id(db, polo_id)
    if not db_polo:
        return None
    for key, value in polo_update.dict(exclude_unset=True).items():
        setattr(db_polo, key, value)
    db.commit()
    db.refresh(db_polo)
    return db_polo

def delete_polo(db: Session, polo_id: int):
    db_polo = get_polo_by_id(db, polo_id)
    if not db_polo:
        return None
    db.delete(db_polo)
    db.commit()
    return db_polo
