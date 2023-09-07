import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import ProjectSettings
from routes import api_router

app = FastAPI(
    version="0.1.0",
    openapi_url=f"{ProjectSettings.API_VERSION_PATH}/openapi.json",
    docs_url=f"{ProjectSettings.API_VERSION_PATH}/docs",
    redoc_url=f"{ProjectSettings.API_VERSION_PATH}/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ProjectSettings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=ProjectSettings.API_VERSION_PATH)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081, log_level='debug')
