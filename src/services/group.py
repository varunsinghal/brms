from typing import List

from src.commons.models import TGroupTemplate
from src.services import Service


class GroupService(Service):
    def get_group_templates(self) -> List[TGroupTemplate]:
        return (
            self.session.query(TGroupTemplate)
            .filter(TGroupTemplate.is_active == 1)
            .all()
        )
