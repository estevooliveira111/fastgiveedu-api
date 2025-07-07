from fastapi import FastAPI, Depends, Request, status
from fastapi.staticfiles import StaticFiles
from app.db.base import Base
from app.db.session import engine
from app.auth.deps import get_current_user
from app.api.v1.routers import polos_router, students, payments, charges, transfers, auth, bank_accounts_router

from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import json

# Cria as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

# Inicializa o aplicativo FastAPI
app = FastAPI(
    title="FastGiveEdu API",
    version="1.0.0"
)

# Tratamento global para erros HTTP
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "type": "http_error",
                "detail": exc.detail,
                "status_code": exc.status_code,
            },
        },
    )

# Tratamento global para erros de validação
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    body = exc.body

    # Tentativa de converter o corpo em string legível ou dicionário
    if isinstance(body, bytes):
        try:
            body = body.decode('utf-8', errors='ignore')
            body = json.loads(body)
        except json.JSONDecodeError:
            body = str(body)
    elif not isinstance(body, (dict, list, str)):
        body = str(body)

    # Converte qualquer ValueError ou outro objeto em string para serialização segura
    serializable_errors = []
    for error in exc.errors():
        err = error.copy()
        if "ctx" in err and "error" in err["ctx"]:
            err["ctx"]["error"] = str(err["ctx"]["error"])
        serializable_errors.append(err)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": {
                "type": "validation_error",
                "details": serializable_errors,
                "body": body,
            },
        },
    )

# Monta arquivos estáticos (como imagens, CSS, JS etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Rota raiz para checagem rápida
@app.get("/", include_in_schema=False)
def root():
    return {"message": "ok"}

# Rotas protegidas por autenticação
app.include_router(auth.router, prefix="/auth", tags=["students"])
app.include_router(students.router, prefix="/students", tags=["students"], dependencies=[Depends(get_current_user)])
app.include_router(payments.router, prefix="/payments", tags=["payments"], dependencies=[Depends(get_current_user)])
app.include_router(charges.router, prefix="/charges", tags=["charges"], dependencies=[Depends(get_current_user)])
app.include_router(transfers.router, prefix="/transfers", tags=["transfers"], dependencies=[Depends(get_current_user)])
app.include_router(polos_router.router, prefix="/polos", tags=["polos"], dependencies=[Depends(get_current_user)])
app.include_router(bank_accounts_router.router, prefix="/financial/bank-accounts", tags=["accounts-bank"], dependencies=[Depends(get_current_user)])

