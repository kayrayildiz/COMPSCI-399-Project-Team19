import abc
from src.domain.model import User, Question

repo_instance = None
class RepositoryException(Exception):
    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):
    # User objects
    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_score(self, user_name):
        raise NotImplementedError

    @abc.abstractmethod
    def add_score(self, user_name, score: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_users(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_tags(self, user_name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def add_frequently_incorrect(self, user_name: str, tag: str):
        raise NotImplementedError
        

    # Question objects
    @abc.abstractmethod
    def add_question(self, question: Question):
        raise NotImplementedError

    @abc.abstractmethod
    def get_question(self, question_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_questions(self):
        raise NotImplementedError

    @abc.abstractmethod
    def chunks(self, data_array, per_page: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tag(self, question_id):
        raise NotImplementedError