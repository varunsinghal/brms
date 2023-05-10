from flask import Blueprint, render_template

from src.commons.database import get_session
from src.services.group import GroupService

group_app = Blueprint("group", __name__)
group_service = GroupService(get_session())


@group_app.route("/")
def group_index():
    context = dict(group_templates=group_service.get_group_templates())
    return render_template("group/index.html", **context)
