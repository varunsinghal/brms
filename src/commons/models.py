from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.sql import func

Model = declarative_base()


class TFormTemplate(Model):
    __tablename__ = "t_form_template"

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    modified_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    elements = relationship("TFormElement", backref="form_template")

    def __repr__(self):
        return f"<Form-{self.name}>"


class TFormElement(Model):
    __tablename__ = "t_form_element"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    template_id = Column(Integer, ForeignKey("t_form_template.id"))
    sequence_no = Column(Integer, nullable=False)
    label = Column(String(80))
    tooltip = Column(String(256))

    @hybrid_property
    def identifier(self):
        return f"{self.__class__.__name__}-{self.id}"

    __mapper_args__ = {
        "polymorphic_identity": "form_element",
        "polymorphic_on": "type",
    }

    def __repr__(self):
        return f"<{self.__class__.__name__}-{self.id}>"


class TSimpleTextBoxFormElement(TFormElement):
    __tablename__ = "t_form_simple_textbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element.id"), primary_key=True
    )
    max_length = Column(Integer, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "simple_textbox"}


class TNumericTextBoxFormElement(TFormElement):
    __tablename__ = "t_form_numeric_textbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    min_value = Column(Integer)
    max_value = Column(Integer)

    __mapper_args__ = {"polymorphic_identity": "numeric_textbox"}


class TDateTextBoxFormElement(TFormElement):
    __tablename__ = "t_form_date_textbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    min_date = Column(String(80))
    max_date = Column(String(80))

    __mapper_args__ = {"polymorphic_identity": "date_textbox"}


class TLargeTextBoxFormElement(TFormElement):
    __tablename__ = "t_form_large_textbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )

    __mapper_args__ = {"polymorphic_identity": "large_textbox"}


class TCheckBoxFormElement(TFormElement):
    __tablename__ = "t_form_checkbox"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    option = Column(String(256))

    __mapper_args__ = {"polymorphic_identity": "checkbox"}


class TRadioButtonFormElement(TFormElement):
    __tablename__ = "t_form_radio_button"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    options = Column(String(256))

    __mapper_args__ = {"polymorphic_identity": "radio_button"}


class TSingleSelectFormElement(TFormElement):
    __tablename__ = "t_form_single_select"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    options = Column(String(256))
    query = Column(Text)

    __mapper_args__ = {"polymorphic_identity": "single_select"}


class TMultiSelectFormElement(TFormElement):
    __tablename__ = "t_form_multi_select"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    options = Column(String(256))
    query = Column(Text)

    __mapper_args__ = {"polymorphic_identity": "multi_select"}


class TMultiSelectOrderedFormElement(TFormElement):
    __tablename__ = "t_form_multi_select_ordered"

    id: Mapped[int] = mapped_column(
        ForeignKey("t_form_element"), primary_key=True
    )
    options = Column(String(256))
    query = Column(Text)

    __mapper_args__ = {"polymorphic_identity": "multi_select_ordered"}
