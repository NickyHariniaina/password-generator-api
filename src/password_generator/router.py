from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from .service import generate_password, check_security
from pydantic import BaseModel

class PasswordModel(BaseModel):
    password: str

router = APIRouter()

@router.get("/generate")
def generate_simple_password(length: int = 8):
    password = generate_password(length)
    return JSONResponse(content={"password": password}, status_code=200)

@router.post("/check_password")
def check_password_strength(request: Request, password: PasswordModel):
    is_strong: bool = check_security(password.password)
    return JSONResponse(content={"is_strong": is_strong}, status_code=201)

