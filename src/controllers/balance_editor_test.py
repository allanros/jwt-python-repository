from .balance_editor import BalanceEditor

class MockUserRepository:
    def edit_balance(self, user_id: int, new_balance: float) -> None: pass

def test_edit_balance(): 
    balance_editor = BalanceEditor(MockUserRepository())
    response = balance_editor.edit(32, 105.4)

    assert response['type'] == 'user'
    assert response['count'] == 1
    assert response['new balance'] == 105.4
