# noinspection PyUnresolvedReferences
import sqlalchemy
import sqlalchemy.orm

# setup the engine
conn_string = "sqlite:///./store_db.bin"
engine = sqlalchemy.create_engine(conn_string, echo=True)
session_factory = sqlalchemy.orm.sessionmaker(engine)

