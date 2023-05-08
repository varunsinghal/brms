import logging

import lxml.etree as ET

from src.commons.models import (
    TFormElement,
    TNumericTextBoxFormElement,
    TSimpleTextBoxFormElement,
)

logger = logging.getLogger(__name__)


class Serializer:
    template_name: str = None

    @classmethod
    def to_html(cls, xml, theme_folder: str):
        xml = xml.encode()
        dom = ET.fromstring(xml)
        xslt = ET.parse(f"xslt/{theme_folder}/{cls.template_name}")
        return ET.tostring(ET.XSLT(xslt)(dom)).decode()

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


MAPPING = {
    TSimpleTextBoxFormElement: SimpleTextBoxSerializer,
    TNumericTextBoxFormElement: NumericTextBoxSerializer,
}


def serialize(instance, theme: str = "default") -> str:
    serializer = MAPPING.get(type(instance))
    if not serializer:
        logger.warning(f"serializer not defined for {type(instance)}")
        return ""
    xml = serializer.to_xml(instance)
    return serializer.to_html(xml, theme)
