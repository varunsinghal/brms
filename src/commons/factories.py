from datetime import datetime, timedelta, timezone

import factory
import factory.fuzzy
from faker import Faker

from src.commons.constants import FIELD_SEPARATOR
from src.commons.models import (
    TCheckBoxFormElement,
    TDateTextBoxFormElement,
    TFormElement,
    TFormTemplate,
    TLargeTextBoxFormElement,
    TNumericTextBoxFormElement,
    TRadioButtonFormElement,
    TSimpleTextBoxFormElement,
)


def make_form_template_factory() -> factory.Factory:
    class _FormTemplateFactory(factory.Factory):
        class Meta:
            model = TFormTemplate

        class Params:
            duration = factory.fuzzy.FuzzyInteger(low=1, high=100)

        id = factory.Sequence(lambda n: n + 1)
        name = factory.LazyAttribute(lambda o: f"Form template {o.id}")
        created_at = factory.fuzzy.FuzzyDateTime(
            datetime(2008, 1, 1, tzinfo=timezone.utc)
        )
        modified_at = factory.LazyAttribute(
            lambda o: o.created_at + timedelta(o.duration)
        )

    return _FormTemplateFactory


class FormElementFactory(factory.Factory):
    class Meta:
        model = TFormElement

    class Params:
        form_template = make_form_template_factory().create()

    id = factory.Sequence(lambda n: n + 1)
    template_id = factory.LazyAttribute(lambda o: o.form_template.id)
    sequence_no = factory.Sequence(lambda n: n + 1)
    label = factory.LazyAttribute(lambda o: f"Label {o.id}")
    tooltip = factory.Faker("text", max_nb_chars=80)


def make_simple_textbox_factory() -> factory.Factory:
    class _SimpleTextBoxFactory(FormElementFactory):
        class Meta:
            model = TSimpleTextBoxFormElement

        max_length = factory.fuzzy.FuzzyInteger(low=0, high=80)

    return _SimpleTextBoxFactory


def make_numeric_textbox_factory() -> factory.Factory:
    class _NumericTextBoxFactory(FormElementFactory):
        class Meta:
            model = TNumericTextBoxFormElement

        min_value = factory.fuzzy.FuzzyInteger(low=0, high=10)
        max_value = factory.fuzzy.FuzzyInteger(low=20, high=30)

    return _NumericTextBoxFactory


def make_date_textbox_factory() -> factory.Factory:
    class _DateTextBoxFactory(FormElementFactory):
        class Meta:
            model = TDateTextBoxFormElement

        min_date = factory.Faker("date")
        max_date = factory.Faker("date")

    return _DateTextBoxFactory


def make_large_textbox_factory() -> factory.Factory:
    class _LargeTextBoxFactory(FormElementFactory):
        class Meta:
            model = TLargeTextBoxFormElement

    return _LargeTextBoxFactory


def make_checkbox_factory() -> factory.Factory:
    class _CheckBoxFactory(FormElementFactory):
        class Meta:
            model = TCheckBoxFormElement

        checked_value = factory.Faker("word")

    return _CheckBoxFactory


def make_radiobutton_factory() -> factory.Factory:
    class _RadioButtonFactory(FormElementFactory):
        class Meta:
            model = TRadioButtonFormElement

        @factory.lazy_attribute
        def options(self):
            return FIELD_SEPARATOR.join(Faker().words())

    return _RadioButtonFactory
