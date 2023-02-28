from sqlalchemy import (BOOLEAN, Table, MetaData, Column, Integer, String, Boolean)
from sqlalchemy.orm import backref, mapper

from src.domain import model

metadata = MetaData()

# TABLE GENERATION
users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False), 
    Column('score', Integer), 
    Column('frequently_incorrect', String(225)),
)

questions_table = Table(
    'questions', metadata, 
    Column('id', Integer, primary_key=True, autoincrement=True), 
    Column('sender_address', String(255), unique=False, nullable=False), 
    Column('email_subject', String(255), unique=False, nullable=False), 
    Column('email_content', String(255), unique=False, nullable=False), 
    Column('is_legitimate', BOOLEAN), 
    Column('reason', String(255)), 
    Column('tag', String(255)),
)

# MAPPER
def map_model_to_tables():
    mapper(model.User, users_table, properties={
        '_User__user_name': users_table.c.user_name,
        '_User__password': users_table.c.password,
        '_User__score': users_table.c.score,
        '_User__frequently_incorrect': users_table.c.frequently_incorrect,
    })

    mapper(model.Question, questions_table, properties={
        '_Question__q_id': questions_table.c.id, 
        '_Question__sender_address': questions_table.c.sender_address, 
        '_Question__email_subject': questions_table.c.email_subject, 
        '_Question__email_content': questions_table.c.email_content, 
        '_Question__is_legitimate': questions_table.c.is_legitimate, 
        '_Question__reason': questions_table.c.reason,
        '_Question__tag': questions_table.c.tag,
    })