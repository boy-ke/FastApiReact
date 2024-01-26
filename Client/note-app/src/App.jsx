import { useState, useEffect, createContext } from 'react';
import axios from 'axios';
import AddNote from "./components/AddNote";
import NotesList from "./components/NotesList";

export const NotesListUpdateFunctionContext = createContext(null);


export default function App() {
  const [notes, setNotes] = useState([]);
  useEffect(() => {
    const getNotes = async () => {
      const API_URL = "http://localhost:8000/notes";
      const { data } = await axios.get(`${API_URL}/notes`);
      setNotes(data);
    }
    getNotes();
  }, []);


  return (
    <NotesListUpdateFunctionContext.Provider value={setNotes}>
      <div>
        <h1 id="app-title">Notes App</h1>
        <AddNote />
        <NotesList notes={notes} />
      </div>
    </NotesListUpdateFunctionContext.Provider>
  );
}