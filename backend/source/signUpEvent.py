from .signUpEventSchema import SignUpEventSchemaInput, SignUpEventSchemaOutput


def signUpEvent(input_value: SignUpEventSchemaInput) -> SignUpEventSchemaOutput:
    output = SignUpEventSchemaOutput(
        Status="Status",
        Id=1,
        Name="Name",
        Surname="Surname",
        SignUpDate="2021-08-10T00:00:00",
        EventId="EventId",
        Email="Email",
        PhoneNumber="PhoneNumber",
        NumberOfGuests=1,
    )
    return output