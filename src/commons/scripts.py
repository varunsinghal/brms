from src.commons.database import get_engine, get_session
from src.commons.factories import (
    make_checkbox_factory,
    make_date_textbox_factory,
    make_form_elements,
    make_form_template_factory,
    make_group_template_factory,
    make_large_textbox_factory,
    make_multi_ordered_select_factory,
    make_multi_select_factory,
    make_numeric_textbox_factory,
    make_radiobutton_factory,
    make_simple_textbox_factory,
    make_single_select_factory,
)
from src.commons.models import Model


def clean_db():
    session = get_session()
    engine = get_engine()
    Model.metadata.drop_all(engine)
    session.commit()


def init_db():
    session = get_session()
    engine = get_engine()
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)
    session.commit()


def load_db():
    session = get_session()
    session.execute()
    session.commit()


def create_factories():
    session = get_session()
    form_template_factory = make_form_template_factory()
    group_template_factory = make_group_template_factory()
    factories = [
        make_simple_textbox_factory(),
        make_numeric_textbox_factory(),
        make_date_textbox_factory(),
        make_large_textbox_factory(),
        make_checkbox_factory(),
        make_radiobutton_factory(),
        make_single_select_factory(),
        make_multi_select_factory(),
        make_multi_ordered_select_factory(),
    ]
    for _ in range(4):
        form_template = form_template_factory.create()
        form_elements = make_form_elements(form_template, factories)
        group_template = group_template_factory.create(
            form_template=form_template
        )
        session.add_all([form_template, group_template] + form_elements)
    session.commit()
