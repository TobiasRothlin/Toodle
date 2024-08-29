from .viewEventSchema import ViewEventSchemaInput

from .dbInteraction import viewEventById


from fastapi.responses import FileResponse


def getEventAsCSV(input_value: ViewEventSchemaInput) -> str:
    event = viewEventById(input_value.Id)
    # Convert the event to a CSV file
    print(event)
    headers = "Name,Surname,Email,PhoneNumber,NumberOfGuests,SignUpDate\n"
    csv = headers
    for attendee in event["Attendees"]:
        csv += f'{attendee["Name"]},{attendee["Surname"]},{attendee["Email"]},{attendee["PhoneNumber"]},{attendee["NumberOfGuests"]},{attendee["SignUpDate"]}\n'
    
    with open("temp.csv", "w") as f:
        f.write(csv)
    
    return FileResponse("temp.csv", media_type="application/octet-stream", filename=f"{event['Name']}.csv")
