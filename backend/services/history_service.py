import json
from pathlib import Path


class HistoryService:
    FILE_PATH = "backend/data/history/latest_assessment.json"

    def load_latest(self):

        path = Path(self.FILE_PATH)

        if not path.exists():
            return []

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get("findings", [])

    def save(self, findings):

        finding_texts = []

        for finding in findings:
            if hasattr(finding, "message"):
                finding_texts.append(finding.message)

            else:
                finding_texts.append(str(finding))

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump({"findings": finding_texts}, file, indent=4)
