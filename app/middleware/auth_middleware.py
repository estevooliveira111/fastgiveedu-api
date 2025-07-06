from fastapi import Request
from fastapi.responses import JSONResponse
from jose import JWTError, jwt
from app.core.config import settings
from app.core.security import ALGORITHM

EXCLUDED_PATHS = ["/", "/auth/login", "/docs", "/openapi.json", "/static"]

async def auth_middleware(request: Request, call_next):
    if any(request.url.path.startswith(p) for p in EXCLUDED_PATHS):
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(status_code=401, content={"detail": "Não autorizado"})

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        request.state.user = payload.get("sub")
    except JWTError:
        return JSONResponse(status_code=401, content={"detail": "Token inválido"})

    return await call_next(request)
