from src.controllers.interface.login_creator import LoginCreatorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interface.view_interface import ViewInterface
from src.errors.types.http_bad_request import HttpBadRequestError

class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        username = request.body.get('username')
        password = request.body.get('password')

        self.__validate_inputs(username=username, password=password)

        response = self.__controller.create(username=username, password=password)
        return HttpResponse(body={'data': response}, status_code=200)

    def __validate_inputs(self, username: any, password: any) -> None:
        if(
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ): raise HttpBadRequestError('Invalid input')
