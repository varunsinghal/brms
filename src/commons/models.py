from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.sql import func

Model = declarative_base()


class FormTemplate(Model):
    __tablename__ = "t_form_template"

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    modified_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"<Form-{self.name}>"


class FormElement(Model):
    __tablename__ = "t_form_element"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    sequence_no = Column(Integer, nullable=False)
    label = Column(String(80))
    tooltip = Column(String(256))

    __mapper_args__ = {
        "polymorphic_identity": "form_element",
        "polymorphic_on": "type",
    }

    def __repr__(self):
        return f"<{self.__class__.__name__}-{self.id}>"


class SimpleTextBoxFormElement(FormElement):
    __tablename__ = "t_form_simple_textbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element.id"), primary_key=True
    )
    max_length = Column(Integer)

    __mapper_args__ = {"polymorphic_identity": "simple_textbox"}


class NumericTextBoxFormElement(FormElement):
    __tablename__ = "t_form_numeric_textbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    min_value = Column(Integer)
    max_value = Column(Integer)

    __mapper_args__ = {"polymorphic_identity": "numeric_textbox"}


class DateTextBoxFormElement(FormElement):
    __tablename__ = "t_form_date_textbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    min_date = Column(DateTime)
    max_date = Column(DateTime)

    __mapper_args__ = {"polymorphic_identity": "date_textbox"}


class LargeTextBoxFormElement(FormElement):
    __tablename__ = "t_form_large_textbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )

    __mapper_args__ = {"polymorphic_identity": "large_textbox"}


class CheckBoxFormElement(FormElement):
    __tablename__ = "t_form_checkbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    option = Column(String(256))

    __mapper_args__ = {"polymorphic_identity": "checkbox"}


class RadioButtonFormElement(FormElement):
    __tablename__ = "t_form_radio_button"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    options = Column(String(256))

    __mapper_args__ = {"polymorphic_identity": "radio_button"}


class SingleSelectFormElement(FormElement):
    __tablename__ = "t_form_single_select"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    options = Column(String(256))
    query = Column(Text)

    __mapper_args__ = {"polymorphic_identity": "single_select"}


class MultiSelectFormElement(FormElement):
    __tablename__ = "t_form_multi_select"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    options = Column(String(256))
    query = Column(Text)

    __mapper_args__ = {"polymorphic_identity": "multi_select"}
