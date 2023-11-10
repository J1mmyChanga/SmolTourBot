import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Places(SqlAlchemyBase):
    __tablename__ = 'places'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    address = sqlalchemy.Column(sqlalchemy.String)
    location = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('locations.id'))
    #img = sqlalchemy.Column(sqlalchemy.BLOB)