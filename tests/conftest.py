import pytest

from src import create_app
from src.adapters import memory_repo, repo_populate

from utils import get_project_root

TEST_DATA_PATH = get_project_root() / "tests" / "data"

@pytest.fixture
def in_memory_repo():
    repo = memory_repo.MemoryRepository()
    repo_populate.populate(TEST_DATA_PATH, repo, database_mode=False)
    return repo

@pytest.fixture
def client():
    test_app = create_app({
        'TESTING': True,                 # Overrides config.py, sets testing to True
        'REPOSITORY': 'memory',          # Memory needs to be implemented so we can test with persistent (and fake) data
        'TEST_DATA_PATH': TEST_DATA_PATH, 
        'WTF_CSRF_ENABLED': False
    })
    return test_app.test_client()

class AuthenticationManager:
    def __init__(self, client):
        self.__client = client

    # Example user: 1,user_1,User1password
    def login(self, user_name="user_1", password="User1password"):
        return self.__client.post(
            'authentication/login',
            data={'user_name': user_name, 'password': password}
        )
    
    def logout(self):
        return self.__client.get('/auth/logout')

@pytest.fixture
def auth(client):
    return AuthenticationManager(client)