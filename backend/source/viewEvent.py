from .viewEventSchema import ViewEventSchemaInput, ViewEventSchemaOutput

def viewEvent(input_value: ViewEventSchemaInput) -> ViewEventSchemaOutput:

    output = ViewEventSchemaOutput(
        Id=1,
        Name="Name",
        Description="Description",
        MaxAttendees=10,
        Date="2021-08-10T00:00:00",
        SineUpDeadline="2021-08-10T00:00:00",
        showNumberOfGuests=True,
        isMailRequired=True,
        isPhoneNumberRequired=True,
        Attendees=[{
            "Name": "Name",
            "Surname": "Surname",
            "Email": "Email",
            "PhoneNumber": "PhoneNumber",
            "NumberOfGuests": 1,
            "SignUpDate": "2021-08-10T00:00:00"
        }],
    )
    return output