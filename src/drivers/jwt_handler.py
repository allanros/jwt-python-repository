import jwt
from datetime import datetime, timedelta, timezone

class JWTHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload= {
                'exp': datetime.now(timezone.utc) + timedelta(days=1),
                **body
            },
            key='secret',
            algorithm='HS256'
        )

        return token
    
    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(
            token,
            key='secret',
            algorithms='HS256'
        )

        return token_information
