from fastapi import FastAPI
from models.models import ChatRequest, FeedbackRequest
from openai_client import get_diagnosis_from_openai
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat/diagnose")
async def diagnose(req: ChatRequest):
    result = get_diagnosis_from_openai(
        gender=req.gender,
        age=req.age,
        signs=req.signs_symptoms,
        description=req.description
    )

    try:
        return {"result": eval(result) if isinstance(result, str) else result}
    except Exception as e:
        print(f"[Parsing Error] {e}")
        return {"error": "Failed to parse AI response"}


@app.post("/chat/feedback")
async def submit_feedback(req: FeedbackRequest):
    print(f"Feedback received: {req.dict()}")
    # TODO: Save to database or file (e.g., MongoDB, SQLite)
    return {"result": "Feedback submitted successfully"}

