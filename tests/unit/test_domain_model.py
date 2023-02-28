from pathlib import Path
import pytest

from utils import get_project_root
from src.domain.model import User, Question

class TestUser:
    def test_construction(self):
        user1 = User('Shyamli', 'pw12345')
        user2 = User('Martin', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        assert str(user1) == "<User Shyamli>"
        assert str(user2) == "<User Martin>"
        assert str(user3) == "<User Daniel>"

    def test_sort_ordering(self):
        user1 = User("Shyamli", "pw12345")
        user2 = User("Martin", "pw67890")
        user3 = User("Daniel", "pw12345")
        assert user1 > user2
        assert user1 > user3
        assert user2 > user3

    def test_comparison(self):
        user1 = User("Martin", "pw12345")
        user2 = User("Shyamli", "pw67890")
        user3 = User("martin", "pw45673")
        assert user1 != user3
        assert user1 != user2
        assert user3 != user2

    def test_set_operations(self):
        user1 = User('Shyamli', 'pw12345')
        user2 = User('Martin', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        set_of_users = set()
        set_of_users.add(user1)
        set_of_users.add(user2)
        set_of_users.add(user3)
        assert str(sorted(set_of_users)) == "[<User Daniel>, <User Martin>, <User Shyamli>]"

    def test_passwords(self):
        user1 = User('  Shyamli   ', 'pw12345')
        user2 = User('Martin', 'p90')
        assert str(user1) == "<User Shyamli>"
        assert str(user1.password) == "pw12345"
        assert str(user2) == "<User Martin>"
        assert user2.password is None


class TestQuestion:
    def test_construction(self):
        question = Question(100, "email_sender", "email_subject", "email_content", True, "reason", "tag")
        assert str(question) == "<Question id: 100>"

    def test_comparison(self):
        q1 = Question(101, "email_sender", "email_subject", "email_content", True, "reason", "tag")
        q2 = Question(102, "email_sender", "email_subject", "email_content", True, "reason", "tag")
        q3 = Question(103, "email_sender", "email_subject", "email_content", True, "reason", "tag")
        q4 = Question(103, "email_sender", "email_subject", "email_content", True, "reason", "tag")
        assert q1 != q2
        assert q1 != q3
        assert q3 == q4