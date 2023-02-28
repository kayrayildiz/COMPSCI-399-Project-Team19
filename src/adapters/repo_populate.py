from pathlib import Path

from src.adapters.repo import AbstractRepository
from src.adapters.data_importer import load_users, load_questions


def populate(data_path: Path, repo: AbstractRepository, database_mode: bool):
    # if database_mode = "database": only load questions, no fake users should be loaded from an external file
    if database_mode == True:
        load_questions(data_path, repo)

    # if database_mode = "memory": load fake, or admin, users from csv file for testing purposes
    else:
        load_users(data_path, repo)
        load_questions(data_path, repo)
    