from src.controllers.interface.balance_editor import BalanceEditorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interface.view_interface import ViewInterface

class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        new_balance = request.body.get('new_balance')
        user_id = request.params.get('user_id')

        self.__validate_inputs(user_id=user_id, new_balance=new_balance)

        response = self.__controller.edit(user_id=user_id, new_balance=new_balance)
        return HttpResponse(body={'data': response}, status_code=200)

    def __validate_inputs(self, user_id: any, new_balance: any) -> None:
        if(
            not new_balance
            or not user_id
            or not isinstance(new_balance, float)
        ): raise Exception('Invalid input')