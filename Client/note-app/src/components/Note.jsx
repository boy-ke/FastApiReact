import { useState } from "react";

import NoteViewer from "./NoteViewer";
import NoteEditor from "./NoteEditor";

export default function Note({ note }) {
    const [noteView, setNoteView] = useState("viewing");
    switch (noteView) {
        case "viewing":
            return <NoteViewer note={note} setNoteView={setNoteView} />;
        case "editing":
            return <NoteEditor note={note} setNoteView={setNoteView} />;
        default:
            return <></>;
    }
}