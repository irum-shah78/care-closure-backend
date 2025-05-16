# def build_prompt(gender: str, age: str, signs: str, description: str) -> str:
#     return f"""
#     Analyze the following patient's data and provide a list of the top 5 possible diagnoses with the percentage likelihood of each diagnosis.
#     Additionally, include the next recommended steps such as lab work, imaging, and treatment protocols:

#     •⁠  Gender: {gender}
#     •⁠  Age: {age}
#     •⁠  Signs and Symptoms: {signs}
#     •⁠  Description: {description}
#     •⁠  Lab Work or Imaging Results: none

#     Return the response in JSON format.
#     """


def build_user_prompt(gender: str, age: str, signs: str, description: str) -> str:
    return f"""
Gender: {gender}
Age: {age}
Signs and Symptoms: {signs}
Description: {description}
Lab Work or Imaging: none
"""

def get_system_prompt() -> str:
    return """
You are Clinician's Companion, a diagnostic assistant designed to help healthcare professionals by analyzing patient symptoms and returning structured diagnoses.

Your task is to:
1. Identify the top 5 most likely diagnoses.
2. Assign a percentage likelihood to each.
3. Recommend next steps including lab work, imaging, and treatment.
4. Format the output in JSON like this:
{
  "diagnoses": [
    {
      "name": "Diagnosis Name",
      "percentageLikelihood": "80%",
      "reasoning": "Why this diagnosis is likely",
      "nextSteps": {
        "labWork": "...",
        "imaging": "...",
        "treatmentProtocol": "..."
      }
    }
  ],
  "disclaimer": "Clinician's Companion is a decision support tool; always confirm with medical judgment."
}
"""
