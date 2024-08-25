from .viewEventSchema import ViewEventSchemaInput, ViewEventSchemaOutput

from .dbInteraction import viewEventById

def viewEvent(input_value: ViewEventSchemaInput) -> ViewEventSchemaOutput:

    output = viewEventById(input_value.Id)
    
    return output