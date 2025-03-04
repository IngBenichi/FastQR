from pydantic import BaseModel

class QRRequest(BaseModel):
    text: str
    size: int = 10
