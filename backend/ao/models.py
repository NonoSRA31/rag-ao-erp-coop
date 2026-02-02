from pydantic import BaseModel

class LoadAORequest(BaseModel):
    filename: str
