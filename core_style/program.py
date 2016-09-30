import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Text, DateTime, Integer
import datetime

# 1. Create shared engine
conn_str = 'sqlite:///./data/store.bin'
engine = sqlalchemy.create_engine(conn_str)

# 2. Create shared metadata
metadata = sqlalchemy.MetaData()

# 3. Define schema
customers = Table('customers', metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('name', Text, nullable=False, unique=True, index=True),
                  Column('created', DateTime, default=datetime.datetime.now),
                  Column('email', Text, nullable=False, unique=True, index=True)
                  )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('street', Text),
                  Column('city', Text),
                  Column('state', Text),
                  Column('country', Text),
                  Column('postal_code', Text),
                  Column('user_id', None, ForeignKey('customers.id'))
                  )

# 4. Create the database
metadata.create_all(engine)


