from fastapi import FastAPI

from backend.app.api.v1.kubernetes import kubernetes_router
from backend.app.api.v1.terraform import terraform_router
from backend.app.api.v1.infrastructure import infrastructure_router
from backend.app.api.v1.pdf_report import pdf_report_router
from backend.app.api.v1.report_routes import db_report_router
from backend.app.api.v1.auth import auth_router
from backend.app.api.v1.remediation_routes import (
    router as remediation_router
)
from backend.app.api.v1.export_routes import (
    router as export_router
)
from backend.app.api.v1.chat_routes import (
    router as chat_router
)
from fastapi.middleware.cors import (
    CORSMiddleware
)

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

app.include_router(
    db_report_router,
    prefix="/api/v1"
)

app.include_router(

    remediation_router,

    prefix="/api/v1",

    tags=["Remediation"]

)

app.include_router(

    export_router,

    prefix="/api/v1",

    tags=["Export"]

)

app.include_router(

    chat_router,

    prefix="/api/v1",

    tags=["Chat"]

)

app.include_router(

    auth_router,

    prefix="/api/v1/auth",

    tags=["auth"]
)


app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
