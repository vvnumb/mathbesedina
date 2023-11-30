from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from common.dependencies.token import create_access_token
from common.registry import Registry
from src.api.v1.schemas.dtos.auth import Token
from src.api.v1.use_cases.auth.authenticate_case import AuthenticateCase

router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/token", response_model=Token)
def login_for_access_token(
		form_data: OAuth2PasswordRequestForm = Depends(),
		auth_case: AuthenticateCase = Depends(Registry.authentication_service)
):
	user = auth_case(form_data)
	
	from config import jwt_config
	access_token = create_access_token(
		data={"sub": user.username},
		expires_delta=timedelta(minutes=jwt_config.ACCESS_TOKEN_EXPIRE_MINUTES)
	)
	return {"access_token": access_token, "token_type": jwt_config.TOKEN_TYPE}