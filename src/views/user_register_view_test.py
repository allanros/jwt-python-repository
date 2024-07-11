import pytest
from .user_register_view import UserRegisterView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class MockController:
    def registry(self, username: str, password: str) -> str:
        return {'some': 'data'}

def test_handle_user_register():
    body = {
        'username': 'test',
        'password': 'test123'
    }    
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)
    response = user_register_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {'data': {'some': 'data'}}
    assert response.status_code == 201

def test_handle_user_register_invalid_input():
    body = {
        'username': 1231,
        'password': 'test123'
    }    
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)


