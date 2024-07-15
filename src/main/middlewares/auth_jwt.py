from flask import request
from src.drivers.jwt_handler import JWTHandler
from src.errors.types.http_unauthorized import HttpUnauthorizedError

def auth_jwt_verify():
    jwt_handler = JWTHandler()
    raw_token = request.headers.get('Authorization')
    user_id = request.headers.get('uid')

    if not raw_token or not user_id:
        raise HttpUnauthorizedError('Invalid Auth Informations')
    
    token = raw_token.split(' ')[1]
    token_information = jwt_handler.decode_jwt_token(token)
    token_uid = token_information['user_id']

    if user_id and token_uid and (int(user_id) == int(token_uid)):
        return token_information
    
    raise HttpUnauthorizedError('User unauthorized')
