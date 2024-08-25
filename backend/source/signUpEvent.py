from .signUpEventSchema import SignUpEventSchemaInput, SignUpEventSchemaOutput

from .dbInteraction import createNewSignUpEvent

def signUpEvent(input_value: SignUpEventSchemaInput) -> SignUpEventSchemaOutput:
    output = createNewSignUpEvent(input_value)
    return output