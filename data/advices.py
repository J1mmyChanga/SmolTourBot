import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Advices(SqlAlchemyBase):
    __tablename__ = 'advices'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('categories.id'))
    advice = sqlalchemy.Column(sqlalchemy.String)

    categories = orm.relationship('Categories', backref='advices')