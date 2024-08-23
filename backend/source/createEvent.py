from .createEventSchema import CreateEventSchemaInput, CreateEventSchemaOutput

def createEvent(input_value: CreateEventSchemaInput) -> CreateEventSchemaOutput:
    output = CreateEventSchemaOutput(
        Name=input_value.Name,
        Description=input_value.Description,
        MaxAttendees=input_value.MaxAttendees,
        Date=input_value.Date,
        SineUpDeadline=input_value.SineUpDeadline,
        RequiredInformation=input_value.RequiredInformation,
        OptionalInformation=input_value.OptionalInformation,
        Id="1",
    )

    return output