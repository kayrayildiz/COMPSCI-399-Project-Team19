import random

from src.adapters.repo import AbstractRepository
from src.domain.model import User, Question


def get_all_questions(repo: AbstractRepository):
    return repo.get_all_questions()


def get_question(repo: AbstractRepository, question_id: int):
    return repo.get_question(question_id)


def get_chunks(repo: AbstractRepository, data_array, per_page: int):
    return list(repo.chunks(data_array, per_page))


def get_user_score(repo: AbstractRepository, user_name):
    return repo.get_score(user_name)


def update_user_score(repo: AbstractRepository, user_name, score: int):
    return repo.add_score(user_name, score)

def get_leaderboard(repo: AbstractRepository):
    users = repo.get_all_users()
    leaderboard = {1: None, 2: None, 3: None, 4: None, 5: None}

    if len(users) >= 1:
        users_and_scores = [(user, user.score) for user in users]
        users_and_scores.sort(key=lambda a: a[1])
        users_and_scores = users_and_scores[::-1]

        for x in range(len(users_and_scores)):
            leaderboard[x + 1] = users_and_scores[x]

    return leaderboard

def get_10_questions(repo: AbstractRepository):
    all_questions = repo.get_all_questions()
    ten_questions = []
    random_sample = random.sample(range(len(all_questions)), 10)
    for number in random_sample:
        ten_questions.append(all_questions[number - 1])
    return ten_questions

def get_user(repo: AbstractRepository, user_name: str):
    return repo.get_user(user_name)

def update_user_tags(repo: AbstractRepository, user_name: str, tag: str):
    repo.add_frequently_incorrect(user_name, tag)

def get_user_tags(repo: AbstractRepository, user_name: str):
    return repo.get_user_tags(user_name)