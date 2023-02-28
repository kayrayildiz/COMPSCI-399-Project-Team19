import csv
from pathlib import Path

from werkzeug.security import generate_password_hash

from src.adapters.repo import AbstractRepository
from src.domain.model import User, Question 


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        for row in reader:
            row = [item.strip() for item in row]
            yield row


def load_users(data_path: Path, repo: AbstractRepository):
    users_filename = str(Path(data_path) / "users.csv")
    for data_row in read_csv_file(users_filename):
        user = User (
            user_name = data_row[1],
            password = generate_password_hash(data_row[2]) 
        )
        repo.add_user(user)
        
def load_questions(data_path: Path, repo: AbstractRepository):
    question_filename = str(Path(data_path) / "questions.csv")
    for data_row in read_csv_file(question_filename):
        question = Question (
            q_id = data_row[0],
            sender_address = data_row[1], 
            email_subject = data_row[2], 
            email_content = data_row[3], 
            is_legitimate = bool(data_row[4]), 
            reason = data_row[5], 
            tag = data_row[6]
        )
        repo.add_question(question)