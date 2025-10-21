from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent_pipeline.crew import run_crew as run_crew_pipeline
import uvicorn
import asyncio

app = FastAPI(title="TechSage Crew Backend", version="1.0")

class CrewInput(BaseModel):
    topic: str

@app.post("/run-crew")
async def run_crew_endpoint(input_data: CrewInput):
    try:
        result = await asyncio.to_thread(run_crew_pipeline, input_data.topic)
        return {"status": "success", "topic": input_data.topic, "result": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "TechSage Crew API is running 🚀"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
