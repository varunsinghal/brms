from unittest import TestCase

from src.commons.database import get_session
from src.commons.serializer import FormSubmissionSerializer


class TestFormSubmissionSerializer(TestCase):
    def setUp(self) -> None:
        self.session = get_session()
        self.serializer = FormSubmissionSerializer()

    def test_form_submission(self):
        data = {
            "name": "wd",
            "form_template_id": 1,
            "fe1": "FE-1",
            "fe2": "FE-2",
            "fe3Left": ["FE-3.1"],
            "fe3": ["FE-3.2", "FE-3.3"],
        }
        actual = self.serializer.load(data)
        self.session.add(actual)
        self.session.commit()
