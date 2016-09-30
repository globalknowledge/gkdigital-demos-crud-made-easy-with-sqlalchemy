# 3. Define schema
from sqlalchemy import Column, Integer, Table, Text, ForeignKey

from data.base import metadata

table = Table('addresses', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('street', Text),
              Column('city', Text),
              Column('state', Text),
              Column('country', Text),
              Column('postal_code', Text),
              Column('user_id', None, ForeignKey('customers.id'))
              )
