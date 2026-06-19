import json
import re

from fastapi import APIRouter, Depends, HTTPException

from backend.services.auth_dependency import get_current_user_id
from backend.services.redesign_service import RedesignService
from backend.services.report_repository import ReportRepository

router = APIRouter()

repository = ReportRepository()

redesign_service = RedesignService()


@router.post("/reports/{report_id}/redesign")
def redesign_architecture(
    report_id: str, current_user_id: str = Depends(get_current_user_id)
):

    report = repository.get_report(report_id, current_user_id)

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    result = redesign_service.redesign(report.report_json)

    try:
        cleaned = result.replace("```json", "").replace("```", "").strip()

        match = re.search(r"\{.*\}", cleaned, re.DOTALL)

        if match:
            cleaned = match.group(0)

        parsed = json.loads(cleaned)

        return parsed

    except Exception as e:
        print("REDESIGN PARSE ERROR")

        print(e)

        print(result)

        return {"error": "Failed to parse redesign"}
