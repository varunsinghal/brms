from marshmallow import EXCLUDE, Schema, fields, post_load, pre_load

from src.commons.constants import FIELD_SEPARATOR, FORM_PREFIX
from src.commons.models import TFormElementSubmission, TFormSubmission


class FormElementSubmissionSerializer(Schema):
    id = fields.Int()
    form_submission_id = fields.Int()
    form_element_id = fields.Int()
    value = fields.Str()

    @post_load
    def make_element_submission(self, data, **kwargs):
        return TFormElementSubmission(**data)


class FormSubmissionSerializer(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int()
    name = fields.Str()
    form_template_id = fields.Int()
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    elements = fields.List(fields.Nested(FormElementSubmissionSerializer))

    @pre_load
    def format_submission(self, data, **kwargs):
        output = {}
        elements = []
        output["name"] = data.pop("name")
        output["form_template_id"] = data.pop("form_template_id")
        for key, value in data.items():
            try:
                form_element_id = int(key.strip(FORM_PREFIX))
                if isinstance(value, list):
                    value = FIELD_SEPARATOR.join(value)
                elements.append(
                    {"form_element_id": form_element_id, "value": value}
                )
            except Exception:
                continue
        output["elements"] = elements
        return output

    @post_load
    def make_submission(self, data, **kwargs):
        return TFormSubmission(**data)
