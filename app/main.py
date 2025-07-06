from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from app.db.base import Base
from app.db.session import engine
from app.auth.deps import get_current_user
from app.api.v1.routers import polos_router, students, payments, charges, transfers, auth, bank_accounts_router


from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastGiveEdu API",
    version="1.0.0"
)


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

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    body = exc.body
    if isinstance(body, bytes):
        body = body.decode('utf-8', errors='ignore')
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "type": "validation_error",
                "details": exc.errors(),
                "body": body,
            },
        },
    )


app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", include_in_schema=False)
def root():
    return {"message": "ok"}

app.include_router(auth.router, prefix="/auth", tags=["students"])
app.include_router(students.router, prefix="/students", tags=["students"], dependencies=[Depends(get_current_user)])
app.include_router(payments.router, prefix="/payments", tags=["payments"], dependencies=[Depends(get_current_user)])
app.include_router(charges.router, prefix="/charges", tags=["charges"], dependencies=[Depends(get_current_user)])
app.include_router(transfers.router, prefix="/transfers", tags=["transfers"], dependencies=[Depends(get_current_user)])
app.include_router(polos_router.router, prefix="/polos", tags=["polos"], dependencies=[Depends(get_current_user)])
app.include_router(bank_accounts_router.router, prefix="/financial/bank-accounts", tags=["acounts-bank"], dependencies=[Depends(get_current_user)])
