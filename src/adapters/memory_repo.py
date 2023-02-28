from src.adapters.repo import AbstractRepository
from src.domain.model import User, Question


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__users = list()
        self.__questions = list()

    # User objects
    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name):
        return next((user for user in self.__users if user.user_name == user_name), None)

    def get_score(self, user_name):
        user = self.get_user(user_name)
        return user.score

    def add_score(self, user_name, score: int):
        user = self.get_user(user_name)
        user.add_score(score)

    def get_all_users(self):
        return self.__users

    def get_user_tags(self, user_name: str):
        user = self.get_user(user_name)
        return user.frequently_incorrect
    
    def add_frequently_incorrect(self, user_name: str, tag: str):
        user: User = self.get_user(user_name)
        user.add_frequently_incorrect(self, tag)

    # Question objects
    def add_question(self, question: Question):
        self.__questions.append(question)

    def get_question(self, question_id: int):
        return next((question for question in self.__questions if question.question_id == question_id))

    def get_all_questions(self):
        return self.__questions

    def chunks(self, data_array, per_page: int):
        if len(data_array) > per_page:
            for i in range(0, len(data_array), per_page):
                yield data_array[i: i + per_page]
        else:
            yield data_array

    def get_tag(self, question_id):
        question = self.get_question(question_id)
        return question.tag