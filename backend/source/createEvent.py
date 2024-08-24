from .createEventSchema import CreateEventSchemaInput, CreateEventSchemaOutput

from .dbInteraction import addEvent

def createEvent(input_value: CreateEventSchemaInput) -> CreateEventSchemaOutput:
    event = addEvent(input_value)


    output = CreateEventSchemaOutput(
        Id=event.id,
        Name=event.name,
        Description=event.description,
        MaxAttendees=event.max_attendees,
        Date=event.date,
        SineUpDeadline=event.sign_up_deadline,
        showNumberOfGuests=event.show_number_of_guests,
        isMailRequired=event.is_mail_required,
        isPhoneNumberRequired=event.is_phone_number_required,
    )
    return output