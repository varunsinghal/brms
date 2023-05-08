from unittest import TestCase

from src.commons.database import get_session
from src.commons.factories import (
    make_form_template_factory,
    make_numeric_textbox_factory,
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
