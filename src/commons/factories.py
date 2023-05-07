import factory
import factory.fuzzy

from src.commons.models import SimpleTextBoxFormElement


def make_simple_textbox_factory() -> factory.Factory:
    class _SimpleTextBoxFactory(factory.Factory):
        class Meta:
            model = SimpleTextBoxFormElement

        id = factory.Sequence(lambda n: n + 1)
        sequence_no = factory.Sequence(lambda n: n + 1)
        label = factory.LazyAttribute(lambda o: f"Label {o.id}")
        tooltip = factory.Faker("text", max_nb_chars=80)
        max_length = factory.fuzzy.FuzzyInteger(low=0, high=80)

    return _SimpleTextBoxFactory
