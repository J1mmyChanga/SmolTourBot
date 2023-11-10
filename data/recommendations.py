import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Recommendations(SqlAlchemyBase):
    __tablename__ = 'recommendations'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('categories.id'))
    recommendation = sqlalchemy.Column(sqlalchemy.String)

    categories = orm.relationship('Categories', backref='recommendations')