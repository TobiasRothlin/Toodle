from .signUpEventSchema import SignUpEventSchemaInput, SignUpEventSchemaOutput


def signUpEvent(input_value: SignUpEventSchemaInput) -> SignUpEventSchemaOutput:
    output = SignUpEventSchemaOutput(
        Status="Success",
        Name=input_value.Name,
        Id=input_value.Id,
    )
    return output