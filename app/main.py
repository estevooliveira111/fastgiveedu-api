from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Allebank API",
    description="API para autenticação e listagem de transações bancárias da plataforma Allebank.",
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
