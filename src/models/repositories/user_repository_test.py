import pytest
from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler

@pytest.mark.skip('integration test')
def test_registry_user():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    repo.registry_user('test_user', 'test_password')

@pytest.mark.skip('integration test')
def test_get_user_by_username():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    response = repo.get_user_by_username('test_user')
    print(type(response))

@pytest.mark.skip('integration test')
def test_delete_user_by_id():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    repo.delete_user_by_id(2)