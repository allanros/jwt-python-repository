import pytest
from src.models.repositories.user_repository import UserRepository
from unittest.mock import Mock

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_registry_user():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.registry_user('John', '1234')
    
    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES (?, ?, ?)" in cursor.execute.call_args[0][0]
    assert ('John', '1234', 0) == cursor.execute.call_args[0][1]

    mock_connection.commit.assert_called_once()

def test_edit_balance():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.edit_balance(1, 100.0)
    
    cursor = mock_connection.cursor.return_value

    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert (100.0, 1) == cursor.execute.call_args[0][1]

    mock_connection.commit.assert_called_once()

def test_get_user_by_username():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user_by_username('John')
    
    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert ('John',) == cursor.execute.call_args[0][1]

    cursor.fetchone.assert_called_once()

def test_delete_user_by_id():
    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.delete_user_by_id(1)
    
    cursor = mock_connection.cursor.return_value

    assert "DELETE FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert (1,) == cursor.execute.call_args[0][1]

    mock_connection.commit.assert_called_once()
