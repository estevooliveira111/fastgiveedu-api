from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

from fastapi.security import HTTPBearer
from fastapi.staticfiles import StaticFiles
from app.api.v1.routers import students

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="FastGiveEdu API",
    version="1.0.0"
)

oauth2_scheme = HTTPBearer()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", include_in_schema=False)
def root():
    """
    Endpoint simples para testar se a API está online.
    Retorna mensagem de OK.
    """
    return {"message": "ok"}

app.include_router(students.router, prefix="/students", tags=["students"])
