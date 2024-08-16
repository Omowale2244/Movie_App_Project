from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import HTMLResponse, JSONResponse
from schemas.user import User

user_router = APIRouter()

@user_router.post('/login', tags=['AuthenticationTest'])
def login(user: User):
    if user.email == "myapp@gmail.com" and user.password == "myapp":
        token: str = create_token(user.model_dump())        
        return JSONResponse(status_code=200, content=token)