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


@dataclass
class Button:
    text: str
    fn: str = None
    color: ColorEnum = ColorEnum.PRIMARY
    sequence_no: int = 9999


@dataclass
class SubmitButton(Button):
    text: str
    fn: str = "submitForm"
    color: ColorEnum = ColorEnum.SUCCESS


class UpdateButton(Button):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.fn = "updateForm"
        self.color = ColorEnum.PRIMARY


class CancelButton(Button):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.fn = "goBack"
        self.color = ColorEnum.NEUTRAL


class DeleteButton(Button):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.fn = "deleteForm"
        self.color = ColorEnum.DANGER
