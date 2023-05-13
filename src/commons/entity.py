import enum
from dataclasses import dataclass


@dataclass
class SimpleTextBox:
    identifier: str
    label: str
    sequence_no: int
    tooltip: str = ""
    max_length: int = 80


class ColorEnum(enum.Enum):
    PRIMARY = "primary"
    DANGER = "danger"
    SUCCESS = "success"
    NEUTRAL = "secondary"
    WARNING = "warning"


class FormStatus(enum.Enum):
    DRAFT = {"css": ColorEnum.PRIMARY.value}
    PENDING = {"css": ColorEnum.WARNING.value}
    APPROVED = {"css": ColorEnum.SUCCESS.value}
    REJECTED = {"css": ColorEnum.DANGER.value}
    CLOSED = {"css": ColorEnum.NEUTRAL.value}


@dataclass
class Button:
    text: str
    fn: str = None
    color: ColorEnum = ColorEnum.PRIMARY
    sequence_no: int = 9999


@dataclass
class SubmitButton(Button):
    fn: str = "submitForm"
    color: ColorEnum = ColorEnum.SUCCESS


@dataclass
class UpdateButton(Button):
    fn: str = "updateForm"
    color: ColorEnum = ColorEnum.PRIMARY


@dataclass
class CancelButton(Button):
    fn: str = "goBack"
    color: ColorEnum = ColorEnum.NEUTRAL


@dataclass
class DeleteButton(Button):
    fn: str = "deleteForm"
    color: ColorEnum = ColorEnum.DANGER
