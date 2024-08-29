"use client";

import React, { useState, useEffect } from 'react';
import Image from "next/image";

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

    const downloadEvent = async (eventId,eventName) => {
        console.log('Downloading event:', eventId);
        try {
            const response = await fetch('/api/getEventAsCSV', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ Id : eventId})
            });
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = `${eventName}.csv`;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    }

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


    const [copied, setCopied] = useState(false);

    const copyLinkToClipboard = (eventId) => {
        let mainURL = window.location.origin;
        let link = mainURL + `/api/getSignUpPage/${eventId}`;
        navigator.clipboard.writeText(link)
            .then(() => {
                console.log('Link copied to clipboard');
                setCopied(true); // Set copied to true when link is successfully copied
                setTimeout(() => {
                    setCopied(false); // Reset copied to false after 2 seconds
                }, 2000);
            })
            .catch((error) => {
                console.error('Error copying link to clipboard:', error);
            });
    };

    return (
        <div className='pl-5 pr-10 pb-10 pt-5 rounded-lg bg-gray-950 bg-opacity-5 shadow-slate-300 shadow-md w-96'>
            <h1 className='text-2xl mb-10'>View All Events</h1>
            <div>
                {events.map((event) => (
                    <div key={event.Id}>
                        <div className='w-full bg-gray-100 m-2 rounded-lg'>
                            <button
                                onClick={() => toggleExpand(event.Id)}
                                className="h-10 w-48 m-2 text-left text-xl " // Increase the width to 64
                            >
                                {event.Name}
                            </button>
                            <button
                                className='h-10 w-10 m-2'
                                title='Download CSV File'
                                onClick={() => downloadEvent(event.Id,event.Name)} // Call the downloadEvent function with the event Id
                            >
                                <Image
                                    src="/Download.svg"
                                    alt="Download"
                                    width={24}
                                    height={24}
                                    className='h-10 w-10 display: inline-block vertical-align: middle'
                                />
                            </button>
                            <button className='h-10 w-10 m-2'
                                title='Copy the Sign Up Page Link'
                                onClick={() => copyLinkToClipboard(event.Id)}>
                                <Image
                                    src="/Copy.svg"
                                    alt="Copy"
                                    width={24}
                                    height={24}
                                    className='h-10 w-10 display: inline-block vertical-align: middle'
                                />
                                {copied && (<div className='w-2 h-2 bg-green-300 rounded-lg '></div>)}
                            </button>
                        </div>

                        {expandedEventId === event.Id && (

                            <div className="ml-10 bg-gray-100 p-2 rounded-lg shadow-md ">

                                <div className="p-1">
                                    <label className="font-bold">ID:</label>
                                    <br></br>
                                    <input type="text" className="border rounded p-1" value={events.find(event => event.Id === expandedEventId)?.details?.Id || ''} readOnly />
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