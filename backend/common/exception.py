from fastapi import HTTPException
from starlette import status

CredentialException = HTTPException(
	status_code=status.HTTP_401_UNAUTHORIZED,
	detail="Could not validate token",
	headers={"WWW-Authenticate": "Bearer"},
)

UserException = HTTPException(
	status_code=status.HTTP_401_UNAUTHORIZED,
	detail="Could not determen user",
	headers={"WWW-Authenticate": "Bearer"},
)