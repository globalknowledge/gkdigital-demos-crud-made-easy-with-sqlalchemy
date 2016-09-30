import sqlalchemy
from sqlalchemy import Table, Column, Text, DateTime, Integer

# 1. Create shared engine
conn_str = 'sqlite:///./data/store.bin'
engine = sqlalchemy.create_engine(conn_str)

# 2. Create shared metadata
metadata = sqlalchemy.MetaData()

# 3. Define schema
customers = Table('customers', metadata,
                  Column('id', Integer),
                  Column('name', Text),
                  Column('created', DateTime),
                  Column('email', Text)
                  )

addresses = Table('addresses', metadata,
                  Column('id', Integer),
                  Column('street', Text),
                  Column('city', Text),
                  Column('state', Text),
                  Column('country', Text),
                  Column('postal_code', Text)
                  )

# 4. Create the database
metadata.create_all(engine)


