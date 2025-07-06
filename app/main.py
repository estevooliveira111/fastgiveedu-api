from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.staticfiles import StaticFiles

from app.db.base import Base
from app.db.session import engine

from app.api.v1.routers import students, users, payments, charges, transfers, polos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastGiveEdu API",
    version="1.0.0"
)

oauth2_scheme = HTTPBearer()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", include_in_schema=False)
def root():
    return {"message": "ok"}

app.include_router(polos.router, prefix="/polos", tags=["polos"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(charges.router, prefix="/charges", tags=["charges"])
app.include_router(transfers.router, prefix="/transfers", tags=["transfers"])
