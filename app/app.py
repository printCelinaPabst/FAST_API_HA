from fastapi import FastAPI, HTTPException
from functions import lade_mitarbeiter
import json
import uvicorn
import os


app = FastAPI()


@app.get("/mitarbeiterdaten")
def mitarbeiterdaten():
    daten = lade_mitarbeiter()

    if daten is None:
        raise HTTPException(status_code=404, detail="Datei nicht gefunden.")
    return daten    


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)