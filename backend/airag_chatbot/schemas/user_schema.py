from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# ======= Input Schema =======

class UserSignUpSchema(BaseModel):
    first_name: str = Field(..., description="First Name")
    last_name: str = Field(..., description="Last Name")
    email: EmailStr = Field(..., description="Email address")
    password: str = Field(..., description="Password", min_length=8)
    confirm_password: str = Field(..., description="Confirm password", min_length=8)

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(..., description="Email address")
    password: str = Field(..., description="Password", min_length=8)


# ======= Response Schema =======

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        orm_status: True


class UserTokenResponse(UserResponse):
    access_token: Optional[str] = None
    token_type: Optional[str] = "bearer"


class UserLoginResponse(BaseModel):
    status: bool
    message: str
    data: UserTokenResponse