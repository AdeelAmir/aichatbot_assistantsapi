from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.airag_chatbot.schemas.user_schema import UserSignUpSchema, UserLoginResponse
from backend.airag_chatbot.services.user_service import user_sign_up_service
from db.session import get_db

router = APIRouter(prefix='/auth', tags=['Auth'])

# Sign up API
@router.post('/signup', response_model=UserLoginResponse, status_code=status.HTTP_201_CREATED)
async def sign_up(data: UserSignUpSchema, db: AsyncSession = Depends(get_db)):
    
    response = user_sign_up_service()
    return {
        "status": True,
        "message": "User created successfully",
        "data": response
    }