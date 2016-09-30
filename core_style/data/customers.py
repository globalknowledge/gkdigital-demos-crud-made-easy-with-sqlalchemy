# 3. Define schema
import datetime
from sqlalchemy import Column, DateTime, Integer, Table, Text

from data.base import metadata

table = Table('customers', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('name', Text, nullable=False, unique=True, index=True),
              Column('created', DateTime, default=datetime.datetime.now),
              Column('email', Text, nullable=False, unique=True, index=True)
              )
