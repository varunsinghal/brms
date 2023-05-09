from unittest import TestCase

from src.commons.database import get_session
from src.commons.factories import (
    make_checkbox_factory,
    make_date_textbox_factory,
    make_form_template_factory,
    make_large_textbox_factory,
    make_numeric_textbox_factory,
    make_radiobutton_factory,
    make_simple_textbox_factory,
)
from src.commons.models import TFormTemplate
from src.commons.serializer import serialize


class TestSerializer(TestCase):
    def setUp(self) -> None:
        self.session = get_session()
        self.form_template = self.create_form_template()

    def create_form_template(self) -> TFormTemplate:
        form_template_factory = make_form_template_factory()
        form_template = form_template_factory.create()
        self.session.add(form_template)
        self.session.commit()
        return form_template

    def tearDown(self) -> None:
        #
        self.session.query(TFormTemplate).delete()
        self.session.commit()

    def test_simple_textbox(self):
        textbox = make_simple_textbox_factory().create(
            form_template=self.form_template,
        )
        print(serialize(textbox))
        self.session.add(textbox)
        self.session.commit()

    def test_numeric_textbox(self):
        textbox = make_numeric_textbox_factory().create(
            form_template=self.form_template,
        )
        print(serialize(textbox))
        self.session.add(textbox)
        self.session.commit()

    def test_date_textbox(self):
        textbox = make_date_textbox_factory().create(
            form_template=self.form_template,
        )
        self.session.add(textbox)
        self.session.commit()
        print(serialize(textbox))

    def test_large_textbox(self):
        textbox = make_large_textbox_factory().create(
            form_template=self.form_template,
        )
        self.session.add(textbox)
        self.session.commit()
        print(serialize(textbox))

    def test_checkbox(self):
        checkbox = make_checkbox_factory().create(
            form_template=self.form_template,
        )
        self.session.add(checkbox)
        self.session.commit()
        print(serialize(checkbox))

    def test_radiobutton(self):
        radio_button = make_radiobutton_factory().create(
            form_template=self.form_template,
        )
        self.session.add(radio_button)
        self.session.commit()
        print(serialize(radio_button))
