from fastapi import FastAPI
from backend.ao.routes import router as ao_router

app = FastAPI(
    title="RAG AO ERP",
    description="Backend pour la génération contrôlée de réponses aux appels d'offres ERP",
    version="0.1.0"
)

@app.get("/")
def healthcheck():
    return {
        "status": "ok",
        "message": "RAG AO ERP backend is running"
    }

# On branche ici les routes AO
app.include_router(ao_router)
