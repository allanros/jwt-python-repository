from .user_register import UserRegister
from src.models.interface.user_repository import UserRepositoryInterface

class MockUserRepository(UserRepositoryInterface):
    def __init__(self) -> None:
        self.registry_user_att = {}

    def registry_user(self, username: str, password: str) -> None: 
        self.registry_user_att["username"] = username
        self.registry_user_att["password"] = password

    def edit_balance(self, user_id: int, new_balance: float) -> None: pass

    def get_user_by_username(self, username: str) -> tuple[int, str, str]: pass

def test_registry():
    repo = MockUserRepository()
    controller = UserRegister(repo)

    username = "test"
    password = "test123"

    response = controller.registry(username, password)

    assert response["username"] == username
    assert response["type"] == "user"
    assert response["count"] == 1

    assert repo.registry_user_att["username"] == username
    assert repo.registry_user_att["password"] is not None
    assert repo.registry_user_att["password"] != password

