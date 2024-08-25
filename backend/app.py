from typing import Union
from fastapi.responses import HTMLResponse

from fastapi import FastAPI
from pydantic import BaseModel

from source.createEventSchema import CreateEventSchemaInput
from source.signUpEventSchema import SignUpEventSchemaInput
from source.viewEventSchema import ViewEventSchemaInput

from source.createEvent import createEvent
from source.signUpEvent import signUpEvent
from source.viewEvent import viewEvent
from source.getAllEvents import getAllEvents
from source.getHtmlSignUpPage import getHtmlSignUpPage

app = FastAPI()


@app.post("/createEvent")
def create_event(input_value: CreateEventSchemaInput):
    return createEvent(input_value)


@app.post("/signUpEvent")
def sign_up_event(input_value: SignUpEventSchemaInput):
    return signUpEvent(input_value)


@app.post("/viewEvent")
def view_event(input_value: ViewEventSchemaInput):
    return viewEvent(input_value)


@app.get("/getAllEvents")
def get_all_events():
    return getAllEvents()


@app.get("/getSignUpPage/{id}")
def get_html_page(id: int):
    html_content = getHtmlSignUpPage(id)
    return HTMLResponse(content=html_content, status_code=200)

# Ensure the OpenAPI documentation is available
@app.get("/openapi.json")
async def get_openapi():
    print(app.openapi())
    return app.openapi()

@app.get("/docs")
async def get_docs():
    print(app.docs_url)
    return app.docs_url

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)