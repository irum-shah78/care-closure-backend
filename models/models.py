from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    gender: str
    age: str
    signs_symptoms: str
    description: str

class ChatResponse(BaseModel):
    diagnoses: list
    disclaimer: Optional[str] = "This is not a medical diagnosis. Always consult a physician."


class FeedbackRequest(BaseModel):
    diagnosis: str
    feedback: str  # "positive" or "negative"
    patientId: str | None = None
    encounterId: str | None = None