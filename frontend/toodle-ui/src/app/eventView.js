"use client";

import React, { useState, useEffect } from 'react';

const EventView = () => {
    const [events, setEvents] = useState([]);
    const [expandedEventId, setExpandedEventId] = useState(null);

    

    const fetchEvents = async () => {
        try {
            const response = await fetch('/api/getAllEvents');
            const data = await response.json();
            setEvents(data);
        } catch (error) {
            console.error('Error fetching events:', error);
        }
    };

    const toggleExpand = (eventId) => {
        setExpandedEventId(expandedEventId === eventId ? null : eventId);
    };

    useEffect(() => {
        fetchEvents();
    }
    , []);

    useEffect(() => {
        const fetchEventDetails = async () => {
            try {
                const response = await fetch('/api/viewEvent', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ Id: expandedEventId })
                });
                const data = await response.json();
                console.log(data);
                // Update the event details in the events array
                setEvents(events.map(event => event.Id === expandedEventId ? { ...event, details: data } : event));
                
            } catch (error) {
                console.error('Error fetching event details:', error);
            }
        };

        if (expandedEventId) {
            fetchEventDetails();
        }
    }, [expandedEventId]);


    return (
        <div className='pl-5 pr-10 pb-10 pt-5 rounded-lg bg-gray-950 bg-opacity-5 shadow-slate-300 shadow-md w-96'>
            <h1 className='text-2xl mb-10'>View All Events</h1>
            <div>
            {events.map((event) => (
                <div key={event.Id}>
                     <button
                        onClick={() => toggleExpand(event.Id)}
                        className={`text-left text-lg p-3 m-1 bg-gray-200 text-black rounded-lg shadow-2xl hover:bg-gray-100 ${expandedEventId === event.Id ? 'w-full' : 'w-auto'}`}
                    >
                        {event.Name}
                    </button>
                    {expandedEventId === event.Id && (
                        <div className="ml-10 bg-gray-100 p-2 rounded-lg shadow-md">
                        <div className="p-1">
                            <label className="font-bold">ID:</label>
                            <br></br>
                            <input type="text" className="border rounded p-1" value={events.find(event => event.Id === expandedEventId)?.details?.Id || ''} readOnly/>
                        </div>
                        <div className="p-1"> <label className="font-bold">Max Attendees:</label>
                            <br></br>
                            <input type="text" className="border rounded p-1" value={events.find(event => event.Id === expandedEventId)?.details?.MaxAttendees || ''} readOnly />
                        </div>
                        <div className="p-1"> <label className="font-bold">Signup DeadLine:</label>
                            <br></br>
                            <input type="text" className="border rounded p-1" value={events.find(event => event.Id === expandedEventId)?.details?.SineUpDeadline || ''} readOnly />
                        </div>
                        <div className="p-1"> <label className="font-bold">Description:</label>
                            <br></br>
                            <input type="text" className="border rounded p-1" value={events.find(event => event.Id === expandedEventId)?.details?.Description || ''} readOnly />
                        </div>
                        <div className="p-1"> <label className="font-bold">Event Date:</label>
                            <br></br>
                            <input type="text" className="border rounded p-1" value={events.find(event => event.Id === expandedEventId)?.details?.Date || ''} readOnly />
                        </div>

                        <div className="p-1">
                        <label className="font-bold">Attendees: ({events.find(event => event.Id === expandedEventId)?.details?.Attendees.length || 0})</label>
                            <ul className='pl-5'>
                                {events.find(event => event.Id === expandedEventId)?.details?.Attendees.map(attendee => (
                                    <li key={attendee.Id}>{attendee.Name} {attendee.Surname}</li>
                                ))}
                            </ul>
                            </div>
                    </div>
                    )}
                </div>
            ))}

            </div>
            <button onClick={fetchEvents} className='p-2 m-2 bg-red-600 text-slate-200 rounded-lg shadow-2xl hover:bg-red-500'>Relaod Events</button>
            
        </div>
    );
};

export default EventView;