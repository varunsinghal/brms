import logging
from uuid import uuid4

from sqlalchemy.orm import Session


class Service:
    def __init__(self, session: Session) -> None:
        self.log = logging.getLogger(__class__.__name__)
        self.session = session
        self.request_id = uuid4().hex
