import mysql.connector
import json
from .Event import Event

def addEventSupport(newEvent) -> Event:
    mydb = mysql.connector.connect(
        host="db",
        user="root",
        password="rootpassword",
        database="ToodleEventData"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO Events (EventName, Description, MaxAttendees, Eventdate, SignUpDeadLine, ShowNumberOfGuests, IsMailRequired, IsPhoneNumberRequired) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (newEvent.Name, 
           newEvent.Description, 
           newEvent.MaxAttendees, 
           newEvent.Date, 
           newEvent.SineUpDeadline, 
           newEvent.showNumberOfGuests, 
           newEvent.isMailRequired, 
           newEvent.isPhoneNumberRequired)
    
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"--AddEventSupport-- {mycursor.rowcount} Events added.")
    mycursor.fetchall()
    mycursor.execute("SELECT * FROM Events WHERE EventName = %s ORDER BY CreatedAt DESC LIMIT 1", (newEvent.Name,))
    res = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return res


def addEvent(event) -> Event:
    res = addEventSupport(event)
    print(f"-AddEvent-- Res:{res}")
    return Event(id=res[0][0], 
                 name=res[0][1], 
                 description=res[0][2], 
                 max_attendees=res[0][3], 
                 date=res[0][4], 
                 sign_up_deadline=res[0][5], 
                 show_number_of_guests=res[0][6], 
                 is_mail_required=res[0][7], 
                 is_phone_number_required=res[0][8])


def getAllEventsSupport():
    mydb = mysql.connector.connect(
        host="db",
        user="root",
        password="rootpassword",
        database="ToodleEventData"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Events ORDER BY CreatedAt ASC")
    res = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return res


def getAllEvents():
    res = getAllEventsSupport()
    print(f"-GetAllEvents-- Res:{res}")
    events = []
    for event in res:
        events.append({
            "Id": event[0],
            "Name": event[1]
        })
    return events


def createNewSignUpEventSupport(newSignUpEvent):
    mydb = mysql.connector.connect(
        host="db",
        user="root",
        password="rootpassword",
        database="ToodleEventData"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO SignUp (Name, SurName, Event_ID, NumberOfGuests, Mail, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (newSignUpEvent.Name, 
           newSignUpEvent.Surname, 
           newSignUpEvent.EventId, 
           newSignUpEvent.NumberOfGuests,
           newSignUpEvent.Email, 
           newSignUpEvent.PhoneNumber, 
           )
    
    mycursor.execute(sql, val)
    mydb.commit()

    mycursor.fetchall()
    mycursor.execute("SELECT * FROM SignUp WHERE Name = %s ORDER BY CreatedAt DESC LIMIT 1", (newSignUpEvent.Name,))
    res = mycursor.fetchall()
    mycursor.close()
    mydb.close()

    return res


def createNewSignUpEvent(signUpEvent):
    res = createNewSignUpEventSupport(signUpEvent)
    print(f"-CreateNewSignUpEvent-- Res:{res}")
    return {
        "Status": "Success",
        "Id": res[0][0],
        "Name": res[0][1],
        "Surname": res[0][2],
        "EventId": res[0][3],
        "NumberOfGuests": res[0][4],
        "Email": res[0][5],
        "PhoneNumber": res[0][6],
        "SignUpDate": res[0][7],
    }


def viewEventSupportById(eventId):
    mydb = mysql.connector.connect(
        host="db",
        user="root",
        password="rootpassword",
        database="ToodleEventData"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM Events WHERE ID = %s", (eventId,))
    res_event = mycursor.fetchall()

    mycursor.execute("SELECT * FROM SignUp WHERE Event_ID = %s", (eventId,))
    res_sign_up = mycursor.fetchall()
    mycursor.close()
    mydb.close()

    return res_event, res_sign_up


def viewEventById(eventId):
    res_event, res_sign_up = viewEventSupportById(eventId)
    print(f"-ViewEventById-- Res:{res_event}")
    event = {
        "Id": res_event[0][0],
        "Name": res_event[0][1],
        "Description": res_event[0][2],
        "MaxAttendees": res_event[0][3],
        "Date": res_event[0][4],
        "SineUpDeadline": res_event[0][5],
        "Attendees": []
    }

    for sign_up in res_sign_up:
        event["Attendees"].append({
            "Id": sign_up[0],
            "Name": sign_up[1],
            "Surname": sign_up[2],
            "NumberOfGuests": sign_up[4],
            "Email": sign_up[5],
            "PhoneNumber": sign_up[6],
            "SignUpDate": sign_up[7]
        })

    return event