from typing import List, Optional

from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.commons.entity import CancelButton, SimpleTextBox, SubmitButton
from src.commons.forms_serializer import serialize
from src.commons.models import TFormSubmission, TFormTemplate
from src.commons.serializer import FormSubmissionSerializer
from src.services import Service


class FormsService(Service):
    def __init__(self, session: Session):
        super().__init__(session)
        self.serializer = FormSubmissionSerializer()

    def get_form_template(self, form_template_id: int) -> TFormTemplate:
        return (
            self.session.query(TFormTemplate)
            .filter(TFormTemplate.id == form_template_id)
            .one()
        )

    def get_submissions(
        self, form_template_id: int, status: Optional[str] = None
    ) -> List[TFormSubmission]:
        criterion = [
            TFormSubmission.status.name == status.upper() if status else 1 == 1
        ]
        return (
            self.session.query(TFormSubmission)
            .filter(
                and_(
                    TFormSubmission.form_template_id == form_template_id,
                    TFormSubmission.is_deleted == 0,
                    *criterion
                )
            )
            .order_by(TFormSubmission.modified_at.desc())
            .all()
        )

    def get_submit_form(
        self,
        form_template_id: int,
        submit_text: str,
        cancel_text: str = "Cancel",
    ) -> str:
        form_template = self.get_form_template(form_template_id)
        mandatory_fields = [
            SimpleTextBox(label="Name", identifier="name", sequence_no=0)
        ]
        buttons = [
            SubmitButton(text=submit_text),
            CancelButton(text=cancel_text),
        ]
        return serialize(
            mandatory_fields + form_template.elements + buttons, many=True
        )

    def create_submission(
        self,
        form_template_id: int,
        data: dict,
    ):
        data.update({"form_template_id": form_template_id})
        submission = self.serializer.load(data)
        self.session.add(submission)
        self.session.commit()
        return self.serializer.dump(submission)

    def update_submission(self, form_submission_id: int):
        pass

    def delete_submission(self, form_submission_id: int):
        # delete from TFormSubmission.
        pass
