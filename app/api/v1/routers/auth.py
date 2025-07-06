from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta

from app.api import deps
from app.core import security
from app.schemas.user import Token, UserCreate

from app.crud import user as crud_user
from app.auth.deps import get_current_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.get("/me")
def read_own_profile(current_user = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "id": current_user.id,
    }

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(deps.get_db)):
    user = crud_user.get_user_by_username(db, form_data.username)
    if not user or not crud_user.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

    access_token = security.create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=60)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(deps.get_db)):
    db_user = crud_user.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    new_user = crud_user.create_user(db=db, user=user)
    
    access_token = security.create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
