from .password_handler import PasswordHandler

def test_encrypt_password():
    password = "123password"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(password)
    assert password_handler.check_password(password, hashed_password) == True
