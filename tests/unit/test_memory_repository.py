import pytest
from src.domain.model import Question, User

class TestMemoryRepository:
    def test_user(self, in_memory_repo):
        user = User("test_user_1", "TestPassword1")
        in_memory_repo.add_user(user)
        assert user == in_memory_repo.get_user("test_user_1")

    def test_user_score(self, in_memory_repo):
        user = in_memory_repo.get_user("user_1")
        assert user.score == 0

    def test_add_question(self, in_memory_repo):
        question = Question(100, "email_sender", "email_subject", "email_content", True, "reason", "tag")
        in_memory_repo.add_question(question)
        assert question in in_memory_repo.get_all_questions()    
