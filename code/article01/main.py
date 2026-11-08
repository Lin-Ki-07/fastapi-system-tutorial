from fastapi import FastAPI, HTTPException

app = FastAPI()

notes = {
    "basics": {
        "01": {"id": "01", "title": "开始之前"},
    }
}

@app.get("/notes/{category}/{note_id}")
def read_note(category: str, note_id: str):
    note = notes.get(category, {}).get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="笔记不存在")
    return note
