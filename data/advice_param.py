import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class AdviceParams(SqlAlchemyBase):
    __tablename__ = 'adviceparams'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    param = sqlalchemy.Column(sqlalchemy.String)