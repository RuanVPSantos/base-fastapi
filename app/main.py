from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.init_db import init_db
from app.modules.module1.router import router as module1_router
from app.modules.module2.router import router as module2_router

app = FastAPI(title="My FastAPI App", version=settings.API_VERSION)

init_db()

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],  # Substitua por métodos específicos, como ["GET", "POST"]
    allow_headers=["*"],  # Substitua por cabeçalhos específicos, como ["Authorization", "Content-Type"]
)

# Incluindo os módulos
app.include_router(module1_router, prefix="/module1", tags=["Module 1"])
app.include_router(module2_router, prefix="/module2", tags=["Module 2"])

@app.get("/")
async def root():
    return {"message": "Welcome to My FastAPI App"}
