from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from source.createEventSchema import CreateEventSchemaInput
from source.signUpEventSchema import SignUpEventSchemaInput
from source.viewEventSchema import ViewEventSchemaInput

from source.createEvent import createEvent
from source.signUpEvent import signUpEvent
from source.viewEvent import viewEvent

app = FastAPI()


@app.post("/api/createEvent")
def create_event(input_value: CreateEventSchemaInput):
    return createEvent(input_value)


@app.post("/api/signUpEvent")
def sign_up_event(input_value: SignUpEventSchemaInput):
    return signUpEvent(input_value)


@app.post("/api/viewEvent")
def view_event(input_value: ViewEventSchemaInput):
    return viewEvent(input_value)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)