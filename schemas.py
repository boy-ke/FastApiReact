from pydantic import BaseModel


class NoteInput(BaseModel):
    title: str = ""
    description: str = ""