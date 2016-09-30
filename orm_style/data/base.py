# noinspection PyUnresolvedReferences
import sqlalchemy

# setup the engine
conn_string = "sqlite:///./store_db.bin"
engine = sqlalchemy.create_engine(conn_string)


