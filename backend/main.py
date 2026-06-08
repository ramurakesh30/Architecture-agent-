from fastapi import FastAPI

from backend.app.api.v1.kubernetes import kubernetes_router
from backend.app.api.v1.terraform import terraform_router
from backend.app.api.v1.infrastructure import infrastructure_router
from backend.app.api.v1.pdf_report import pdf_report_router

app = FastAPI(
    title="Kubernetes Analyzer"
)

app.include_router(
    kubernetes_router,
    prefix="/api/v1"
)

app.include_router(
    terraform_router,
    prefix="/api/v1"
)

app.include_router(
    infrastructure_router,
    prefix="/api/v1"
)

app.include_router(
    pdf_report_router,
    prefix="/api/v1"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
