from fastapi import FastAPI

from backend.app.api.v1.architecture import router

app = FastAPI(
    title="Architecture Agent"
)

app.include_router(
    router,
    prefix="/api/v1"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
