from .viewEventSchema import ViewEventSchemaInput, ViewEventSchemaOutput


def viewEvent(input_value: ViewEventSchemaInput) -> ViewEventSchemaOutput:

    output = ViewEventSchemaOutput(
        Id="1",
        Name="Name",
        Description="Description",
        MaxAttendees=1,
        Date="2021-08-10T00:00:00",
        SineUpDeadline="2021-08-10T00:00:00",
        RequiredInformation=["RequiredInformation"],
        OptionalInformation=["OptionalInformation"],
        Attendees=["Attendees"],
    )
    return output