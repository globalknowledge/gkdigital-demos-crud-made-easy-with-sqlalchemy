import sqlalchemy
import sqlalchemy.ext.declarative
import datetime
import uuid

# setup the engine
conn_string = "sqlite:///./store_db.bin"
engine = sqlalchemy.create_engine(conn_string)

# create base class
SqlAlchemyBase = sqlalchemy.ext.declarative.declarative_base()


# define types that map to tables
class Customer(SqlAlchemyBase):
    __tablename__ = 'Customers'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.Text)
    email = sqlalchemy.Column(sqlalchemy.Text, unique=True, index=True)


class Order(SqlAlchemyBase):
    __tablename__ = 'Orders'
    # id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True,
                           default=lambda: str(uuid.uuid4()).replace('-', ''))
    total_price = sqlalchemy.Column(sqlalchemy.Float)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)


# create tables if missing
SqlAlchemyBase.metadata.create_all(engine)
