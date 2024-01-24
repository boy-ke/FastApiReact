from fastapi import FastAPI, HTTPException

from model.database import DBSession
from model import models

app = FastAPI()

from schemas import NoteInput
#Health checks
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Adding the API Routes
@app.get("/notes")
def read_notes():
    db = DBSession()
    try:
        notes = db.query(models.Note).all()
    finally:
        db.close()
    return notes

@app.post("/notes")
def add_note(note: NoteInput):
    db = DBSession()
    try:
        if len(note.title) == 0 and len(note.description) == 0:
            raise HTTPException(
                status_code=400, detail={
                    "status": "Error 400 - Bad Request",
                    "message": "Note title and body cannot be empty"
                    })
        new_note = models.Note(
            title=note.title,
            description=note.description
        )
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
    finally:
        db.close()
    return new_note