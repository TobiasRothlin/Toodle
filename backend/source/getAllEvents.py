from .getAllEventsSchema import GetAllEventsSchemaOutput

from .dbInteraction import getAllEvents as getAllEventsSupport

def getAllEvents():
    return getAllEventsSupport()