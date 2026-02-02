from fastapi import APIRouter
from .models import LoadAORequest
from .service import load_ao_section

router = APIRouter()

@router.post("/ao/load")
def load_ao(request: LoadAORequest):
    return load_ao_section(request.filename)
