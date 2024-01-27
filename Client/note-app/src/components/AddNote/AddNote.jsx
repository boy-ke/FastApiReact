import React, { useState, useContext } from "react";
import axios from "axios";

import { NotesListUpdateFunctionContext } from "../../App";

export default function AddNote() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [isFormSubmitting, setIsFormSubmitting] = useState(false);
  const [hasInputError, setHasInputError] = useState(false);

  const setNotes = useContext(NotesListUpdateFunctionContext);

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (title.length > 0 || description.length > 0) {
      setIsFormSubmitting(true);
      const API_URL = "http://localhost:8000";
      const { data } = await axios.post(`${API_URL}/notes`, {
        title,
        description: description.length > 0 ? description : "No description",
      });
      setNotes((prev) => [...prev, data]);      
    } else {
      setHasInputError(true);
    }
    setTitle("");
    setDescription("");
    setIsFormSubmitting(false);
  };


  return (
    <form onSubmit={(event) => handleSubmit(event)} id="add-note-form">
      <input type="text" placeholder="Enter Note Title" id="title-input" className={hasInputError ? "input-error" : ""}
        value={title} onChange={(event) => {
          setHasInputError(false);
          setTitle(event.target.value);
        }}
      />

      <textarea placeholder="Enter Note Description" id="note-body-textarea" className={hasInputError ? "input-error" : ""}
      cols={30} rows={10} value={description} onChange={(event) => {
        setHasInputError(false);
        setDescription(event.target.value);
      }}
      />
      <button id="add-note-btn" type="submit" disabled={isFormSubmitting}>
        {isFormSubmitting ? "..." : "Add Note"}
      </button>
      </form>
  );
}