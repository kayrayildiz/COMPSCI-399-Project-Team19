from flask import Flask, render_template
from pathlib import Path

from src.domain.model import User
import src.adapters.repo as repo
from src.adapters.memory_repo import MemoryRepository
from src.adapters import memory_repo, database_repository, repo_populate
from src.adapters.orm import metadata, map_model_to_tables

# SQLAlchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool

# Import databases or repositories here
from src.quiz import quiz2


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')

    data_path = Path('src') / 'adapters' / 'data'

    # POPULATE MEMORY REPO WITH TEST DATA
    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    if app.config['REPOSITORY'] == 'database': 
        database_uri = app.config['SQLALCHEMY_DATABASE_URI']
        database_echo = app.config['SQLALCHEMY_ECHO']
        database_engine = create_engine(database_uri, connect_args={"check_same_thread": False}, poolclass=NullPool,
                                        echo=database_echo)
        session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)
        repo.repo_instance = database_repository.SqlAlchemyRepository(session_factory)

        if app.config['TESTING'] == 'True' or len(database_engine.table_names()) == 0:
            print("REPOPULATING DATABASE...")

            clear_mappers()
            # create database tables with conditions
            metadata.create_all(database_engine)
            # empty tables
            for table in reversed(metadata.sorted_tables):
                database_engine.execute(table.delete())

            map_model_to_tables()

            # import questions from csv
            database_mode = True
            repo_populate.populate(data_path, repo.repo_instance, database_mode)
            print("REPOPULATING DATABASE... FINISHED")

        else:
            map_model_to_tables()
    
    # POPULATE MEMORY REPO WITH DATA
    elif app.config['REPOSITORY'] == 'memory': # need 'memory' option for testing purposes
        repo.repo_instance = MemoryRepository()
        database_mode = False
        repo_populate.populate(data_path, repo.repo_instance, database_mode)
 
    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .about import about
        app.register_blueprint(about.about_blueprint)

        from .walkthrough import walkthrough
        app.register_blueprint(walkthrough.walkthrough_blueprint)

        from .quiz import quiz, quiz2, modules
            # Quiz 1
        app.register_blueprint(quiz.quiz_blueprint)
        app.register_blueprint(quiz.submit_blueprint)
        #app.register_blueprint(quiz.resolutions_blueprint)
        app.register_blueprint(quiz.leaderboard_blueprint)
            # Quiz 2
        app.register_blueprint(quiz2.quiz_blueprint2)
        app.register_blueprint(quiz2.submit_blueprint2)
        app.register_blueprint(quiz2.solution_blueprint)
            # Modules page
        app.register_blueprint(modules.modules_blueprint)

        from .quiz import quiz2
        app.register_blueprint(quiz2.quiz_blueprint2)
        app.register_blueprint(quiz2.submit_blueprint2)
        app.register_blueprint(quiz2.solution_blueprint)


        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        from .account import account
        app.register_blueprint(account.account_blueprint)

        @app.before_request
        def before_flask_http_request_function():
            if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                repo.repo_instance.reset_session()

        @app.teardown_appcontext
        def shutdown_session(exception=None):
            if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                repo.repo_instance.close_session()
        
    return app