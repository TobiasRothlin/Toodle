"use client";

import React, { useState, useEffect } from 'react';

const formatDateToISO = (date) => {
    const pad = (num) => String(num).padStart(2, '0');
    const padMilliseconds = (num) => String(num).padStart(3, '0');

    const year = date.getUTCFullYear();
    const month = pad(date.getUTCMonth() + 1); // Months are zero-based
    const day = pad(date.getUTCDate());
    const hours = pad(date.getUTCHours());
    const minutes = pad(date.getUTCMinutes());
    const seconds = pad(date.getUTCSeconds());
    const milliseconds = padMilliseconds(date.getUTCMilliseconds());

    return `${year}-${month}-${day}T${hours}:${minutes}:${seconds}.${milliseconds}Z`;
};

const NewEvent = () => {
    const currentDate = new Date();
    const currentDateStr = formatDateToISO(currentDate);


    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [date, setDate] = useState(currentDateStr);
    const [signUpDeadLine, setSignUpDeadLine] = useState(currentDateStr);
    const [maxParticipants, setMaxParticipants] = useState(1);
    const [showParticipants, setShowParticipants] = useState(true);
    const [isPhoneNumberRequired, setIsPhoneNumberRequired] = useState(true);
    const [isEmailRequired, setIsEmailRequired] = useState(true);

    const handleTitleChange = (e) => {
        setTitle(e.target.value);
    };

    const handleDescriptionChange = (e) => {
        setDescription(e.target.value);
    };

    const handleDateChange = (e) => {
        setDate(e.target.value);
    };

    const handleSignUpDeadLineChange = (e) => {
        setSignUpDeadLine(e.target.value);
    }

    const handleMaxParticipantsChange = (e) => {
        setMaxParticipants(e.target.value);
    }

    const handleShowParticipantsChange = (e) => {
        setShowParticipants(e.target.checked);
    }

    const handleIsPhoneNumberRequiredChange = (e) => {
        setIsPhoneNumberRequired(e.target.checked);
    }

    const handleIsEmailRequiredChange = (e) => {
        setIsEmailRequired(e.target.checked);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        // Add your logic here to handle the submission of the new event
        console.log('New event submitted:', { title, description, date });
        const response = await fetch('http://localhost:8000/api/createEvent', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                Name: title,
                Description: description,
                MaxAttendees: maxParticipants,
                Date: date,
                SineUpDeadline: signUpDeadLine,
                showNumberOfGuests: showParticipants,
                isMailRequired: isPhoneNumberRequired,
                isPhoneNumberRequired: isEmailRequired
            })
        });
        console.log(response);
        if (response.ok) {
            console.log('Event created successfully');

        }


        // Reset the form fields
        setTitle('');
        setDescription('');
        setDate('');
        setSignUpDeadLine('');
        setMaxParticipants(1);
        setShowParticipants(true);
        setIsPhoneNumberRequired(true);
        setIsEmailRequired(true);
    };

    return (
        <div className='pl-5 pr-10 pb-10 pt-5 rounded-lg bg-gray-950 bg-opacity-5 shadow-slate-300 shadow-md w-96'>
            <h1 className='text-2xl mb-10'>Create New Event</h1>
            <form onSubmit={handleSubmit}>
                <div className="p-1">
                    <label className="font-bold">Title:</label>
                    <br />
                    <input type="text" value={title} onChange={handleTitleChange} className='border rounded p-1' />
                </div>
                <div className="p-1">
                    <label className="font-bold">Description:</label>
                    <br />
                    <textarea value={description} onChange={handleDescriptionChange} className='border rounded p-1' />
                </div>
                <div className="p-1">
                    <label className="font-bold">Date:</label>
                    <br />
                    <input type="date" value={date} onChange={handleDateChange} className='border rounded p-1' />
                </div>
                <div className="p-1">
                    <label className="font-bold">Sign Up Deadline:</label>
                    <br />
                    <input type="date" value={signUpDeadLine} onChange={handleSignUpDeadLineChange} className='border rounded p-1' />
                </div>
                <div className="p-1">
                    <label className="font-bold">Max Participants:</label>
                    <br />
                    <input type="number" value={maxParticipants} onChange={handleMaxParticipantsChange} className='border rounded p-1' />
                </div>
                <div className="p-1">
                    <label className="font-bold">Show Participants:</label>
                    <input type="checkbox" checked={showParticipants} onChange={handleShowParticipantsChange} className='border rounded p-1 ml-3' />
                </div>
                <div className="p-1">
                    <label className="font-bold">Require Phone Number:</label>
                    <input type="checkbox" checked={isPhoneNumberRequired} onChange={handleIsPhoneNumberRequiredChange} className='border rounded p-1 ml-3' />
                </div>
                <div className="p-1">
                    <label className="font-bold">Require Email:</label>
                    <input type="checkbox" checked={isEmailRequired} onChange={handleIsEmailRequiredChange} className='border rounded p-1 ml-3' />
                </div>
                <button type="submit" className='p-2 m-2 bg-red-600 text-slate-200 rounded-lg shadow-2xl hover:bg-red-500' >Create Event</button>
            </form>
        </div>
    );
};

export default NewEvent;