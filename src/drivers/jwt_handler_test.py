from .jwt_handler import JWTHandler

def test_jwt_handler():
    jwt_handler = JWTHandler()

    body = {
        'username': 'test',
        'password': 'test',
        'role': 'admin',
        'status': 'active'
    }

    token = jwt_handler.create_jwt_token(body)
    token_information = jwt_handler.decode_jwt_token(token)
    
    assert token is not None
    assert isinstance(token, str)
    assert token_information['username'] == body['username']
    assert token_information['password'] == body['password']
    assert token_information['role'] == body['role']
    assert token_information['status'] == body['status']