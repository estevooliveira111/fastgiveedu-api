from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.crud import user as crud
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[UserOut])
def list_users(db: Session = Depends(deps.get_db)):
    return crud.get_all_users(db)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(deps.get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(deps.get_db)):
    return crud.create_user(db, user)

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(deps.get_db)):
    return crud.update_user(db, user_id, user)

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, db: Session = Depends(deps.get_db)):
    return crud.delete_user(db, user_id)
