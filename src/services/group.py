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

    def get_group_template(self, group_template_id: int) -> TGroupTemplate:
        return (
            self.session.query(TGroupTemplate)
            .filter(TGroupTemplate.id == group_template_id)
            .one()
        )
