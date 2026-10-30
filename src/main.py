from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI()


class Extraction(BaseModel):
    kind: Literal["ci_failure","incident","terraform_plan"]
    severity: Literal["low","medium","high"]
    summary: str
    action_items: list[str]= Field(min_length=1)
    affected_services: list[str] = Field(min_length=1)


@app.post("/extract")
def extract(req: Extraction):
    return req