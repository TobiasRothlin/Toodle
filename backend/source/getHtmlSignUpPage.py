

def getHtmlSignUpPage(id: int):
    return """
<!DOCTYPE html>
<html>
<head>
    <title id="PageMetaTitle"></title>
    <style>
        /* CSS styles for the header */
        header {
            background-color: #f2f2f2;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <h1 id="Title"></h1>
        <h3 id="SubTitleInfo"></h3>
        <h3 id="EventDate"></h3>
    </header>

    <div>
        <h2>Attendees</h2>
        <ul id="attendeesList">
            <!-- Attendees will be added here -->
        </ul>
    </div>

    <form id="signupForm">
        <label for="username">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="surname">Surname:</label>
        <input type="text" id="surname" name="surname" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>

        <label for="phoneNumber">Phone Number:</label>
        <input type="text" id="phoneNumber" name="phoneNumber"><br><br>

        <label for="numberOfGuests">Number of Guests:</label>
        <input type="number" id="numberOfGuests" name="numberOfGuests"><br><br>

        <button type="submit">Sign Up</button>
    </form>

    <script>
        // JavaScript code to send a POST request
        const evnetId = %s;

        function loadEventInfo() {
                    //Load the Event Data via Post request
        fetch('/api/viewEvent', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({Id: evnetId})
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);

            // Set the title of the page
            document.getElementById('PageMetaTitle').innerText = result.Name;
            document.getElementById('Title').innerText = result.Name;
            document.getElementById('SubTitleInfo').innerText = result.Description;
            document.getElementById('EventDate').innerText = result.Date;


            // Add the attendees to the list
            const attendeesList = document.getElementById('attendeesList');
            attendeesList.innerHTML = '';
            result.Attendees.forEach(attendee => {
                const li = document.createElement('li');
                li.innerText = attendee.Name;
                attendeesList.appendChild(li);
            });
            // Handle the response here
        })
        }

        loadEventInfo()


        const form = document.getElementById('signupForm');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const name = document.getElementById('name').value;
            const surname = document.getElementById('surname').value;
            const email = document.getElementById('email').value;
            const phoneNumber = document.getElementById('phoneNumber').value;
            const numberOfGuests = document.getElementById('numberOfGuests').value;

            
            const data = {
                Name: name,
                Surname: surname,
                EventId: evnetId,
                Email: email,
                PhoneNumber: phoneNumber,
                NumberOfGuests: numberOfGuests
            };
            
            fetch('/api/signUpEvent', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                console.log(result);
                // Handle the response here
            })
            .then(() => {
                loadEventInfo()
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle errors here
            });
        });



    </script>
</body>
</html>
""" % id

