from unittest import TestCase

from src.commons.factories import make_simple_textbox_factory
from src.commons.serializer import serialize


class TestSerializer(TestCase):
    def setUp(self) -> None:
        self.simple_textbox_factory = make_simple_textbox_factory()

    def test_simple_textbox(self):
        textbox = self.simple_textbox_factory.create()
        serialize(textbox)
