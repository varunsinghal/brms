from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

DATABASE_URI = (
    "mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}"
)


class _Database:
    engine: Engine = None
    session: Session = None


def get_engine() -> Engine:
    return _Database.engine


def get_session() -> Session:
    return _Database.session


def get_connection_uri(**db_credentials):
    return DATABASE_URI.format(**db_credentials)


def initialize_session(connection_uri: str, echo: bool = True):
    _Database.engine = create_engine(connection_uri, echo=echo)
    _Database.session = scoped_session(sessionmaker(bind=_Database.engine))


def destroy_session():
    _Database.session = None
    _Database.engine = None


def rollback_session():
    if _Database.session:
        _Database.session.rollback()


def close_session():
    if _Database.session:
        _Database.session.remove()
