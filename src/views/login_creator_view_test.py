import pytest
from .login_creator_view import LoginCreatorView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class MockController:
    def create(self, username: str, password: str) -> dict:
        return {'some': 'data'}

def test_handle_login_creator():
    body = {
        'username': 'test',
        'password': 'test123'
    }    
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)
    response = login_creator_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {'data': {'some': 'data'}}
    assert response.status_code == 200

@pytest.mark.skip(reason='Not implemented yet')
def test_handle_user_register_invalid_input():
    body = {
        'username': 1231,
        'password': 'test123'
    }    
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)


