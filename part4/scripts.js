/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/



//function to create a place and review card
document.addEventListener('DOMContentLoaded', () => {
    const placeDetails = {
        name: 'Beautiful Place',
        host: 'John Doe',
        price: 150,
        description: 'A lovely place to stay.',
        amenities: ['WiFi', 'Pool', 'Parking'],
        reviews: [
            { comment: 'Great place!', user: 'Alice', rating: 5 },
            { comment: 'Very comfortable.', user: 'Bob', rating: 4 }
        ]
    };

    function displayPlaceDetails(place) {
        const placeDetailsSection = document.getElementById('place-details');
        placeDetailsSection.innerHTML = `
            <h2>${place.name}</h2>
            <div class="place-info">
                <p><strong>Host:</strong> ${place.host}</p>
                <p><strong>Price:</strong> $${place.price} per night</p>
                <p><strong>Description:</strong> ${place.description}</p>
                <p><strong>Amenities:</strong> ${place.amenities.join(', ')}</p>
            </div>
        `;
    }

    function displayReviews(reviews) {
        const reviewsSection = document.getElementById('reviews');
        reviews.forEach(review => {
            const reviewCard = document.createElement('div');
            reviewCard.className = 'review-card';
            reviewCard.innerHTML = `
                <p><strong>${review.user}</strong></p>
                <p>${review.comment}</p>
                <p>Rating: ${generateStars(review.rating)}</p>
            `;
            reviewsSection.appendChild(reviewCard);
        });
    }

    function generateStars(rating) {
        let stars = '';
        for (let i = 0; i < 5; i++) {
            stars += i < rating ? '&#9733;' : '&#9734;';
        }
        return stars;
    }
    displayPlaceDetails(placeDetails);
    displayReviews(placeDetails.reviews);
});


document.addEventListener('DOMContentLoaded', () => {
    function checkUserLoggedIn() {
        // Simulate user login check
        return true; // Change this based on actual login status
    }
    function setupAddReviewSection() {
        const addReviewSection = document.getElementById('add-review');
        if (addReviewSection) {
            if (checkUserLoggedIn()) {
                addReviewSection.innerHTML = `
                    <h2>Add a Review</h2>
                    <form id="review-form" class="form">
                        <label for="review-text">Your Review:</label>
                        <textarea id="review-text" name="review-text" required></textarea><br>
                        <label for="rating">Rating:</label>
                        <select id="rating" name="rating" required>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select><br>
                        <button type="submit" class="generic-button">Submit Review</button>
                    </form>
                `;
            } else {
                addReviewSection.innerHTML = `
                    <button onclick="window.location.href='login.html'">Login to Add a Review</button>
                `;
            }
        }
    }


    setupAddReviewSection();
});

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            await loginUser(email, password);
        });
    }
});

async function loginUser(email, password) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        console.log('Response status:', response.status); // Log the response status

        if (response.ok) {
            const data = await response.json();
            console.log('Response data:', data); // Log the response data
            document.cookie = `token=${data.access_token}; path=/`;
            window.location.href = 'index.html';
        } else {
            const errorText = await response.text();
            console.log('Error text:', errorText); // Log the error text
            let errorData;
            try {
                errorData = JSON.parse(errorText);
            } catch (e) {
                errorData = { error: errorText };
            }
            alert('Échec de la connexion : ' + errorData.error);
        }
    } catch (error) {
        console.error('Erreur:', error);
        alert('Échec de la connexion : ' + error.message);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();
});

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        console.log('No token found, showing login link');
        loginLink.style.display = 'block';
    } else {
        console.log('Token found, hiding login link and fetching places');
        loginLink.style.display = 'none';
        fetchPlaces(token);
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

async function fetchPlaces(token) {
    try {
        console.log('Fetching places with token:', token);
        const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        console.log('Response status:', response.status); // Log the response status

        if (response.ok) {
            const places = await response.json();
            console.log('Places data:', places); // Log the places data
            displayPlaces(places);
        } else {
            console.error('Failed to fetch places:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = ''; // Clear the current content

    places.forEach(place => {
        console.log('Creating card for place:', place); // Log each place
        const card = createPlaceCard(place);
        placesList.appendChild(card);
    });
}

function createPlaceCard(place) {
    const card = document.createElement('div');
    card.className = 'place-card';

    const name = document.createElement('h3');
    name.textContent = place.title; // Utilisez place.title au lieu de place.name
    card.appendChild(name);

    const price = document.createElement('p');
    price.textContent = `Price per night: $${place.price}`; // Utilisez place.price au lieu de place.price_per_night
    card.appendChild(price);

    const button = document.createElement('button');
    button.className = 'generic-button';
    button.textContent = 'View Details';
    card.appendChild(button);

    return card;
}

document.getElementById('price-filter').addEventListener('change', (event) => {
    const selectedPrice = event.target.value;
    filterPlacesByPrice(selectedPrice);
});

function filterPlacesByPrice(maxPrice) {
    const placesList = document.getElementById('places-list');
    const placeCards = placesList.getElementsByClassName('place-card');

    for (let card of placeCards) {
        const price = parseFloat(card.querySelector('p').textContent.replace('Price per night: $', ''));
        if (maxPrice === 'all' || price <= parseFloat(maxPrice)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    }
}