from fastapi import FastAPI
from pydantic import BaseModel

from utils.preprocessing import full_analysis
from utils.admin_engine import admin_decision_engine

app = FastAPI(title="AI Harassment Detection")

class InputText(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: InputText):
    analysis = full_analysis(input.text)
    decision = admin_decision_engine(analysis)
    return {"analysis": analysis, "decision": decision}
