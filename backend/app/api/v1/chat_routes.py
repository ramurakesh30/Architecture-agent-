from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from backend.services.auth_dependency import get_current_user_id
from backend.services.chat_service import ChatService
from backend.services.report_repository import ReportRepository

router = APIRouter()

chat_service = ChatService()

repository = ReportRepository()


class ChatRequest(BaseModel):
    question: str


@router.post("/reports/{report_id}/chat")
def chat_with_report(
    report_id: str,
    request: ChatRequest,
    current_user_id: str = Depends(get_current_user_id),
):
    print("CHAT ENDPOINT HIT")

    report = repository.get_report(report_id, current_user_id)

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    return chat_service.answer_question(report.report_json, request.question)
