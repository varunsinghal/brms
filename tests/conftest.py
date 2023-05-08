from src.commons.database import (
    close_session,
    destroy_session,
    get_engine,
    get_session,
    initialize_session,
)
from src.commons.models import *


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    initialize_session("sqlite:///:memory:", echo=False)
    session = get_session()
    engine = get_engine()
    Model.metadata.create_all(engine)
    session.commit()


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    close_session()
    destroy_session()


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """
