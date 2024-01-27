import Note from "../../components/AddNote/AddNote.jsx"

export default function NotesList({ notes }) {
    return (
        <div id="notes-list-container">
            <h2 id="notes-list-header">
                Notes List
            </h2>
            <ul id="notes-list">
        {notes.map((note) => (
            <li key={note.id}>
                <Note note={note} />
               
            <h2 className="note-title">{note.title}</h2>
            <p className="note-description">{note.description}</p>
             </li>
        ))}
        </ul>
        </div>
    );
}