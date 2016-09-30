# define types that map to tables
import uuid
import datetime
import sqlalchemy
import sqlalchemy.ext.declarative

# create base class
SqlAlchemyBase = sqlalchemy.ext.declarative.declarative_base()


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

    def __str__(self):
        return "Order object: id={}, price={}, created={}".format(
            self.id, self.total_price, self.created
        )

    def __repr__(self):
        return "order(id={}, price={})".format(
            self.id, int(self.total_price)
        )
