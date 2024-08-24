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
