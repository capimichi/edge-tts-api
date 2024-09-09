from pydantic import BaseModel
from typing import List, Optional


class VoiceTag(BaseModel):
    ContentCategories: Optional[List[str]] = None
    VoicePersonalities: Optional[List[str]] = None


class Voice(BaseModel):
    Name: Optional[str] = None
    ShortName: Optional[str] = None
    Gender: Optional[str] = None
    Locale: Optional[str] = None
    SuggestedCodec: Optional[str] = None
    FriendlyName: Optional[str] = None
    Status: Optional[str] = None
    VoiceTag: Optional[VoiceTag]
