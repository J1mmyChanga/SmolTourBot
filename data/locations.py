import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Locations(SqlAlchemyBase):
    __tablename__ = 'locations'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    location = sqlalchemy.Column(sqlalchemy.String)