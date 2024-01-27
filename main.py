from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm.exc import UnmappedInstanceError
from typing import Annotated
from model.database import DBSession
from model import models
from schemas import BaseModel



app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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


@app.get("/notes/{node_id}")
def read_notes_by_id(note_id: int):
    db = DBSession()
    try:
        note = db.query(models.Note).filter(models.Note.id == note_id).first()
        if note is None:
            raise HTTPException(
                status_code=404, detail={
                    "status": "Error 404 - Not Found",
                    "message": f"Note with id {note_id} not found"
                    })
    finally:
        db.close()
    return note


@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: NoteInput):
    if len(updated_note.title) == 0 and len(updated_note.description) == 0:
        raise HTTPException(status_code=400, detail={
            "status": "Error 400 - Bad Request",
            "message": "Note title and description cannot be empty"
        })
    db = DBSession()
    try:
        #note_to_update = db.query(models.Note).filter(models.Note.id == note_id).first()
        note = db.query(models.Note).filter(models.Note.id == note_id).first()
        note.title = updated_note.title
        note.description = updated_note.description
        db.commit()
        db.refresh(note)
    finally:
        db.close()
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    db = DBSession()
    try:
        note = db.query(models.Note).filter(models.Note.id == note_id).first()
        db.delete(note)
        db.commit()
    except UnmappedInstanceError:
        raise HTTPException(status_code=400, detail={
            "status": "Error 400 - Bad Request",
            "message": f"Note with `id` `{note_id}` doesn't exist."
        })
    finally:
        db.close()
    return {
        "status": "200 - Success",
        "message": "Note deleted successfully."
        }