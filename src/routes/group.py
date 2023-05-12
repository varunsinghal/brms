from flask import Blueprint, render_template, request

from src.commons.database import get_session
from src.services.forms import FormsService
from src.services.group import GroupService

group_app = Blueprint("group_app", __name__)
group_api = Blueprint("group_api", __name__)
group_service = GroupService(get_session())
form_service = FormsService(get_session())


@group_app.route("/")
def template_index():
    context = dict(group_templates=group_service.get_group_templates())
    return render_template("group/index.html", **context)


@group_app.route("/<int:group_template_id>/create", methods=["GET"])
def create_form(group_template_id):
    group_template = group_service.get_group_template(group_template_id)
    form_html = form_service.get_submit_form(
        group_template.form_template_id, submit_text="Create"
    )
    context = dict(form_html=form_html, group_template=group_template)
    return render_template("group/create.html", **context)


@group_api.route("/<int:group_template_id>/create", methods=["POST"])
def create_form_submit(group_template_id: int):
    group_template = group_service.get_group_template(group_template_id)
    return form_service.create_submission(
        group_template.form_template_id, request.get_json()
    )
