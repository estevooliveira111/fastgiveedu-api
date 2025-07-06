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

@router.get("/me", summary="Obter perfil do usuário autenticado")
def read_own_profile(current_user = Depends(get_current_user)):
    """
    Retorna o perfil do usuário atualmente autenticado.
    
    Requer um token de acesso válido.
    """
    return {
        "username": current_user.username,
        # "email": current_user.email,
        "id": current_user.id,
    }

@router.post("/login", response_model=Token, summary="Autenticar usuário e gerar token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(deps.get_db)):
    """
    Autentica um usuário com nome de usuário e senha.

    Retorna um token JWT válido por 60 minutos.
    
    **Campos esperados (formulário/x-www-form-urlencoded)**:
    - `username`: Nome de usuário
    - `password`: Senha
    """
    user = crud_user.get_user_by_username(db, form_data.username)
    if not user or not crud_user.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

    access_token = security.create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=60)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=Token, summary="Registrar novo usuário")
def register(user: UserCreate, db: Session = Depends(deps.get_db)):
    """
    Cria um novo usuário e retorna um token JWT de autenticação.

    - `username`: Nome de usuário único
    - `email`: (opcional, se presente no schema)
    - `password`: Senha do usuário

    Se o usuário já existir, retorna erro 400.
    """
    db_user = crud_user.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    new_user = crud_user.create_user(db=db, user=user)
    
    access_token = security.create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}