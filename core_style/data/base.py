import sqlalchemy

# 1. Create shared engine
conn_str = 'sqlite:///./data/store.bin'
engine = sqlalchemy.create_engine(conn_str, echo=False)

# 2. Create shared metadata
metadata = sqlalchemy.MetaData()


def create_db():
    # 4. Create the database
    metadata.create_all(engine)


def created_conn():
    return engine.connect()
