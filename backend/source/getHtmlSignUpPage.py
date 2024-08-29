

def getHtmlSignUpPage(id: int):
    return """
<!DOCTYPE html>
<html>
<head>
    <title id="PageMetaTitle">Sing Up Page</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">

</head>
<body class="bg-gray-100">
    <header class="p-5 text-center">
        <h1 id="Title" class="text-4xl m-3">Title Main</h1>
        <h3 id="SubTitleInfo" class="text-2xl m-2">Subtitle</h3>
        <h3 id="EventDate" class="text-2xl">Date</h3>
    </header>

    <div class="text-center p-10">
        <h2 class="m-2 text-2xl">Attendees</h2>
        <ul id="attendeesList" class="mx-auto w-96">
            <!-- Attendees will be added here -->
        </ul>
    </div>

    <div class="content-center text-center">
        <form id="signupForm" class="grid mx-auto w-96">
            <div class="bg-gray-200 p-10 rounded-lg grid grid-cols-2 gap-4 w-full text-center" >
            <label for="name" class="text-right">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="surname" class="text-right">Surname:</label>
            <input type="text" id="surname" name="surname" required>

            <label for="email" class="text-right">Email:</label>
            <input type="email" id="email" name="email">

            <label for="phoneNumber" class="text-right">Phone Number:</label>
            <input type="text" id="phoneNumber" name="phoneNumber">

            <label for="numberOfGuests" class="text-right">Number of Guests:</label>
            <input type="number" id="numberOfGuests" name="numberOfGuests">
            </div>

            <button type="submit" class="text-white p-2 m-2 bg-red-600 rounded-lg shadow-2xl hover:bg-red-500">Sign Up</button>
        </form>
        </form>
    </div>



    <script>
        // JavaScript code to send a POST request
        const evnetId = %s

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
                li.innerText = attendee.Name + ' ' + attendee.Surname;
                li.classList.add('bg-gray-50', 'm-2', 'p-2', 'rounded-lg');
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

            // Clear the form
            form.reset();
        });



    </script>
</body>
</html>
""" % id

