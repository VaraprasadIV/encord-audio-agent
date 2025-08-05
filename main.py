
from fastapi import FastAPI, UploadFile, File
from agent import AudioTranslateAgent
import shutil
import os
import uuid

app = FastAPI()
agent = AudioTranslateAgent()

@app.post("/edit")
async def edit(file: UploadFile = File(...)):
    temp_path = f"/tmp/{uuid.uuid4()}_{file.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        result = agent.transcribe_and_translate(temp_path)
        return {"segments": result}
    finally:
        os.remove(temp_path)
