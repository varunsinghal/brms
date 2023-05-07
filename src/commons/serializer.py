import logging

import lxml.etree as ET

from src.commons.models import SimpleTextBoxFormElement

logger = logging.getLogger(__name__)


class Serializer:
    template_name: str = None

    @classmethod
    def to_html(cls, xml, theme_folder: str):
        xml = xml.encode()
        dom = ET.fromstring(xml)
        xslt = ET.parse(f"xslt/{theme_folder}/{cls.template_name}")
        return ET.tostring(ET.XSLT(xslt)(dom)).decode()


class SimpleTextBoxSerializer(Serializer):
    template_name: str = "simple_textbox.xsl"

    @classmethod
    def to_xml(cls, instance: SimpleTextBoxFormElement) -> str:
        xml = "<simple-textbox>"
        xml += f"<id>{instance.id}</id>"
        xml += f"<label>{instance.label}</label>"
        xml += f"<sequence>{instance.sequence_no}</sequence>"
        if instance.tooltip:
            xml += f"<tooltip>{instance.tooltip}</tooltip>"
        if instance.max_length:
            xml += f"<max-length>{instance.max_length}</max-length>"
        xml += "</simple-textbox>"
        return xml


MAPPING = {SimpleTextBoxFormElement: SimpleTextBoxSerializer}


def serialize(instance, theme: str = "default") -> str:
    serializer = MAPPING.get(type(instance))
    if not serializer:
        logger.warning(f"serializer not defined for {type(instance)}")
        return ""
    xml = serializer.to_xml(instance)
    return serializer.to_html(xml, theme)
