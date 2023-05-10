import logging

import lxml.etree as ET

from src.commons.constants import FIELD_SEPARATOR
from src.commons.models import (
    TCheckBoxFormElement,
    TDateTextBoxFormElement,
    TFormElement,
    TLargeTextBoxFormElement,
    TMultiOrderedSelectFormElement,
    TMultiSelectFormElement,
    TNumericTextBoxFormElement,
    TRadioButtonFormElement,
    TSimpleTextBoxFormElement,
    TSingleSelectFormElement,
)

logger = logging.getLogger(__name__)


class Serializer:
    template_name: str = ""

    @classmethod
    def to_html(cls, xml: str, theme_folder: str):
        xml_bytes = xml.encode()
        dom = ET.fromstring(xml_bytes)
        xslt = ET.parse(f"templates/forms/{theme_folder}/{cls.template_name}")
        return ET.tostring(ET.XSLT(xslt)(dom), method="html").decode()

    @classmethod
    def base_attributes(cls, instance: TFormElement):
        return (
            f"<id>{instance.id}</id>"
            f"<identifier>{instance.identifier}</identifier>"
            f"<label>{instance.label}</label>"
            f"<sequence>{instance.sequence_no}</sequence>"
            f"<tooltip>{instance.tooltip}</tooltip>"
        )


class SimpleTextBoxSerializer(Serializer):
    template_name: str = "simple_textbox.xsl"

    @classmethod
    def to_xml(cls, instance: TSimpleTextBoxFormElement) -> str:
        xml = "<simple-textbox>"
        xml += cls.base_attributes(instance)
        xml += f"<max-length>{instance.max_length}</max-length>"
        xml += "</simple-textbox>"
        return xml


class NumericTextBoxSerializer(Serializer):
    template_name: str = "numeric_textbox.xsl"

    @classmethod
    def to_xml(cls, instance: TNumericTextBoxFormElement) -> str:
        xml = "<numeric-textbox>"
        xml += cls.base_attributes(instance)
        xml += f"<min-value>{instance.min_value}</min-value>"
        xml += f"<max-value>{instance.max_value}</max-value>"
        xml += "</numeric-textbox>"
        return xml


class DateTextBoxSerializer(Serializer):
    template_name: str = "date_textbox.xsl"

    @classmethod
    def to_xml(cls, instance: TDateTextBoxFormElement) -> str:
        xml = "<date-textbox>"
        xml += cls.base_attributes(instance)
        xml += f"<min-date>{instance.min_date}</min-date>"
        xml += f"<max-date>{instance.max_date}</max-date>"
        xml += "</date-textbox>"
        return xml


class LargeTextBoxSerializer(Serializer):
    template_name: str = "large_textbox.xsl"

    @classmethod
    def to_xml(cls, instance: TLargeTextBoxFormElement) -> str:
        xml = "<large-textbox>"
        xml += cls.base_attributes(instance)
        xml += "</large-textbox>"
        return xml


class CheckBoxSerializer(Serializer):
    template_name: str = "checkbox.xsl"

    @classmethod
    def to_xml(cls, instance: TCheckBoxFormElement) -> str:
        xml = "<checkbox>"
        xml += cls.base_attributes(instance)
        xml += f"<checked-value>{instance.checked_value}</checked-value>"
        xml += "</checkbox>"
        return xml


class RadioButtonSerializer(Serializer):
    template_name: str = "radio_button.xsl"

    @classmethod
    def to_xml(cls, instance: TRadioButtonFormElement) -> str:
        xml = "<radio-button>"
        xml += cls.base_attributes(instance)
        xml += "<options>"
        for option in instance.options.split(FIELD_SEPARATOR):
            xml += f"<option><value>{option}</value></option>"
        xml += "</options>"
        xml += "</radio-button>"
        return xml


def get_option_or_query_xml(options: str, query: str):
    if options:
        xml = "<options>"
        xml += "".join(
            [
                "<option><value>" + option + "</value></option>"
                for option in options.split(FIELD_SEPARATOR)
            ]
        )
        xml += "</options>"
    else:
        xml = f"<query>{query}</query>"
    return xml


class SingleSelectSerializer(Serializer):
    template_name: str = "single_select.xsl"

    @classmethod
    def to_xml(cls, instance: TSingleSelectFormElement) -> str:
        xml = "<single-select>"
        xml += cls.base_attributes(instance)
        xml += get_option_or_query_xml(instance.options, instance.query)
        xml += "</single-select>"
        return xml


class MultiSelectSerializer(Serializer):
    template_name: str = "multi_select.xsl"

    @classmethod
    def to_xml(cls, instance: TMultiSelectFormElement) -> str:
        xml = "<multi-select>"
        xml += cls.base_attributes(instance)
        xml += get_option_or_query_xml(instance.options, instance.query)
        xml += "</multi-select>"
        return xml


class MultiOrderedSelectSerializer(Serializer):
    template_name: str = "multi_ordered_select.xsl"

    @classmethod
    def to_xml(cls, instance: TMultiOrderedSelectFormElement) -> str:
        xml = "<multi-ordered-select>"
        xml += cls.base_attributes(instance)
        xml += get_option_or_query_xml(instance.options, instance.query)
        xml += "</multi-ordered-select>"
        return xml


MAPPING = {
    TSimpleTextBoxFormElement: SimpleTextBoxSerializer,
    TNumericTextBoxFormElement: NumericTextBoxSerializer,
    TDateTextBoxFormElement: DateTextBoxSerializer,
    TLargeTextBoxFormElement: LargeTextBoxSerializer,
    TCheckBoxFormElement: CheckBoxSerializer,
    TRadioButtonFormElement: RadioButtonSerializer,
    TSingleSelectFormElement: SingleSelectSerializer,
    TMultiSelectFormElement: MultiSelectSerializer,
    TMultiOrderedSelectFormElement: MultiOrderedSelectSerializer,
}


def serialize(instance, theme: str = "default") -> str:
    serializer = MAPPING.get(type(instance))
    if not serializer:
        logger.warning(f"serializer not defined for {type(instance)}")
        return ""
    xml = serializer.to_xml(instance)
    return serializer.to_html(xml, theme)
