# create tables if missing
from data.base import engine
from data.models import SqlAlchemyBase


def init():
    SqlAlchemyBase.metadata.create_all(engine)

