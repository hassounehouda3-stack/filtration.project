from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Filtration Calculator")


class FiltrationInput(BaseModel):
    m0: float = Field(gt=0)
    x0: float = Field(ge=0, le=1)


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/calculate")
def calculate(data: FiltrationInput):
    m_residus = data.m0 * data.x0
    m1 = data.m0 - m_residus
    x1 = (data.m0 * data.x0) / m1

    return {
        "m_residus": m_residus,
        "m1": m1,
        "x1": x1
    }