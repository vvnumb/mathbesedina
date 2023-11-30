from datetime import datetime, timedelta

from jose import jwt

from config import jwt_config


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
	to_encode = data.copy()
	expire = datetime.utcnow() + expires_delta
	
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, jwt_config.SECRET_KEY, algorithm=jwt_config.ALGORITHM)
	return encoded_jwt
