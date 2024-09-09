import os
import tempfile
from typing import List

from fastapi import FastAPI
from fastapi.responses import FileResponse
import edge_tts
import uvicorn

from edgettsapi.model.TtsRequest import TtsRequest
from edgettsapi.model.Voice import Voice

from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("EDGE_TTS_BASE_URL", "http://localhost:8000")

app = FastAPI(title="Edge TTS API", version="0.1.0", root_path=base_url)

@app.post("/tts")
async def text_to_speech(tts_request: TtsRequest) -> FileResponse:
    text = tts_request.get_text()
    voice_name = tts_request.get_voice()
    communicate = edge_tts.Communicate(text, voice_name)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file_path = temp_file.name
    await communicate.save(temp_file_path)

    return FileResponse(temp_file_path, media_type="audio/mpeg")

@app.get("/voices")
async def get_voices() -> List[Voice]:
    voices_items = await edge_tts.list_voices()
    voices = []
    for voice in voices_items:
        if voice:
            voices.append(Voice.model_validate(voice))

    return voices


if(__name__ == "__main__"):
    uvicorn.run(app, host="0.0.0.0", port=8000)