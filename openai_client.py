import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

def build_user_prompt(gender: str, age: str, signs: str, description: str) -> str:
    base_prompt = (
        "Analyze the following patient's data and provide a list of the top 5 possible diagnoses "
        "with the percentage likelihood of each diagnosis. Additionally, include the next recommended steps, "
        "such as lab work, imaging, and treatment protocols:\n\n"
        f"•⁠  Gender: {gender}\n"
        f"•⁠  Age: {age}\n"
        f"•⁠  Signs and Symptoms: {signs}\n"
        f"•⁠  Description: {description}\n"
        "•⁠  Lab Work or Imaging Results: none\n\n"
        "Based on this information, generate:\n"
        "1. Top 5 Diagnoses ranked by percentage probability.\n"
        "2. Next Steps including recommended further lab work, imaging, and treatment protocols for each diagnosis.\n"
        "3. Return the response in JSON format."
    )
    return base_prompt

def get_diagnosis_from_openai(gender: str, age: str, signs: str, description: str):
    try:
        user_prompt = build_user_prompt(gender, age, signs, description)
        thread = openai.beta.threads.create()
        openai.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_prompt
        )

        run = openai.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=ASSISTANT_ID
        )

        if run.status == "completed":
            messages = openai.beta.threads.messages.list(thread_id=thread.id)
            for msg in messages.data:
                if msg.role == "assistant" and msg.content[0].type == "text":
                    return msg.content[0].text.value

        return {
            "error": f"Incomplete run: {run.status}",
            "last_error": getattr(run, "last_error", None)
        }

    except Exception as e:
        print(f"[OpenAI Error] {e}")
        return {"error": "OpenAI call failed"}
