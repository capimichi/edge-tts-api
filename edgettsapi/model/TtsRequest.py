from pydantic import BaseModel


class TtsRequest(BaseModel):
    text: str
    voice: str

    def get_text(self):
        return self.text

    def set_text(self, text: str):
        self.text = text

    def get_voice(self):
        return self.voice

    def set_voice(self, voice: str):
        self.voice = voice
