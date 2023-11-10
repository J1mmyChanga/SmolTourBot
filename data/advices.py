import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Advices(SqlAlchemyBase):
    __tablename__ = 'advices'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    advice = sqlalchemy.Column(sqlalchemy.String)
    param = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('adviceparams.id'))

    categories = orm.relationship('AdviceParams', backref='advices')