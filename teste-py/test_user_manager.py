import pytest
import threading

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, name, email, password):
        if len(password) < 8 or not any(char.isdigit() for char in password):
            raise ValueError("A senha deve ter pelo menos 8 caracteres e incluir um número.")
        if email in self.users:
            raise ValueError("Email já cadastrado.")
        self.users[email] = {'name': name, 'password': password}
    
    def login(self, email, password):
        if email not in self.users:
            raise ValueError("Email não cadastrado.")
        if self.users[email]['password'] != password:
            raise ValueError("Senha incorreta.")
        return True
    
    def delete_user(self, email):
        if email not in self.users:
            raise ValueError("Email não cadastrado.")
        del self.users[email]
    
    def change_password(self, email, new_password):
        if email not in self.users:
            raise ValueError("Email não cadastrado.")
        self.users[email]['password'] = new_password


# Fixtures para o UserManager
@pytest.fixture
def user_manager():
    return UserManager()

# --- Testes Felizes (Happy Path) ---

# Teste de cadastro de usuário válido
def test_register_valid_user(user_manager):
    user_manager.register_user('John Doe', 'john@example.com', 'Password123')
    assert 'john@example.com' in user_manager.users

# Teste de login com credenciais válidas
def test_login_valid_user(user_manager):
    user_manager.register_user('John Doe', 'john@example.com', 'Password123')
    assert user_manager.login('john@example.com', 'Password123')


# --- Testes Tristes (Unhappy Path) ---

# Teste de cadastro com email duplicado
def test_register_duplicate_email(user_manager):
    user_manager.register_user('John Doe', 'john@example.com', 'Password123')
    with pytest.raises(ValueError, match="Email já cadastrado."):
        user_manager.register_user('Jane Doe', 'john@example.com', 'Password456')

# Teste de cadastro com senha curta
def test_register_short_password(user_manager):
    with pytest.raises(ValueError, match="A senha deve ter pelo menos 8 caracteres e incluir um número."):
        user_manager.register_user('John Doe', 'john@example.com', 'short')

# Teste de cadastro com senha sem número
def test_register_password_without_number(user_manager):
    with pytest.raises(ValueError, match="A senha deve ter pelo menos 8 caracteres e incluir um número."):
        user_manager.register_user('John Doe', 'john@example.com', 'Password')

# Teste de login com email não cadastrado
def test_login_invalid_email(user_manager):
    with pytest.raises(ValueError, match="Email não cadastrado."):
        user_manager.login('nonexistent@example.com', 'Password123')

# Teste de login com senha incorreta
def test_login_invalid_password(user_manager):
    user_manager.register_user('John Doe', 'john@example.com', 'Password123')
    with pytest.raises(ValueError, match="Senha incorreta."):
        user_manager.login('john@example.com', 'WrongPassword')


# --- Testes Adicionais ---

# Teste de email com formato inválido
def test_register_invalid_email_format(user_manager):
    with pytest.raises(ValueError, match="Formato de email inválido."):
        user_manager.register_user('John Doe', 'invalid-email', 'Password123')

# Teste de senha com caracteres especiais
def test_register_valid_password_with_special_chars(user_manager):
    user_manager.register_user('John Doe', 'john@example.com', 'Password@123')
    assert 'john@example.com' in user_manager.users

# Teste de limite: email com o tamanho máximo
def test_register_max_email_length(user_manager):
    long_email = 'a' * 245 + '@example.com'  # Tamanho máximo de 254 caracteres
    user_manager.register_user('John Doe', long_email, 'Password123')
    assert long_email in user_manager.users

# Teste de concorrência: cadastro de usuários simultâneos
def test_concurrent_user_registration(user_manager):
    def register_user():
        user_manager.register_user('John Doe', 'john@example.com', 'Password123')
    
    threads = []
    for _ in range(10):  # 10 tentativas simultâneas
        thread = threading.Thread(target=register_user)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    assert 'john@example.com' in user_manager.users
