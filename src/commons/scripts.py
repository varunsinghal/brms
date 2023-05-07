from .database import get_engine, get_session
from .models import Model


def clean_db():
    pass


def init_db():
    session = get_session()
    engine = get_engine()
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)
    session.commit()


def create_factories():
    # session = get_session()
    pass
