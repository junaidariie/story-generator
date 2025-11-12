from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from story_teller import img2text, Generate_story  # ✅ Removed text2speech
from PIL import Image
import io, os

app = FastAPI(title="Story Generater")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

class Out(BaseModel):
    scenario    : str
    story       : str
    audio_url   : str  # ❗ still kept for schema compatibility

@app.get("/")
def Home():
    return {"message" : "The api is live now..."}

@app.post("/upload_image", response_model=Out)
async def upload_image(file : UploadFile = File(...)):
    try:
        img_bytes = await file.read()
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")

        scenario = img2text(img)
        story = Generate_story(scenario)

        # ✅ Removed TTS generation
        audio_url = ""  # return empty since TTS removed

        return Out(
            scenario=scenario,
            story=story,
            audio_url=audio_url
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
