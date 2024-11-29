document.addEventListener('DOMContentLoaded', () => {
  // Function to create a place card
  function createPlaceCard(place) {
    const placeCard = document.createElement('article');
    placeCard.classList.add('place-card');

    const placeName = document.createElement('h2');
    placeName.classList.add('place-name');
    placeName.textContent = place.title;

    const placePrice = document.createElement('p');
    placePrice.classList.add('place-price');
    placePrice.textContent = `Price per night: $${place.price}`;

    const detailsButton = document.createElement('button');
    detailsButton.classList.add('details-button');
    detailsButton.textContent = 'View Details';
    detailsButton.addEventListener('click', () => {
      window.location.href = `place.html?placeId=${place.id}`;
    });

    placeCard.append(placeName, placePrice, detailsButton);
    return placeCard;
  }

  // Function to display places
  function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return console.error("The element with ID 'places-list' was not found.");
    placesList.innerHTML = '';
    places.forEach(place => placesList.appendChild(createPlaceCard(place)));
  }

  // Function to fetch places from the API
  async function fetchPlaces() {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/v1/places');
      if (!response.ok) throw new Error('Failed to fetch places');
      const places = await response.json();
      displayPlaces(places);
    } catch (error) {
      console.error('Error fetching places:', error);
    }
  }

  fetchPlaces();
});

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  return parts.length === 2 ? parts.pop().split(';').shift() : null;
}

document.addEventListener('DOMContentLoaded', () => {
  // Function to create the review section
  function createReviewSection() {
    const reviewSectionHTML = `
      <section id="add-review" class="add-review">
        <h2>Add a Review</h2>
        <form id="review-form">
          <label for="review-text">Your Review: <br></label>
          <textarea id="review-text" name="review-text" required></textarea><br>
          <label for="review-rate">Your Rating: </label>
          <select id="review-rate" name="review-rate" required>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
          </select><br>
          <button type="submit">Submit Review</button>
        </form>
      </section>
    `;

    const existingSection = document.getElementById('add-review');
    if (existingSection) {
      existingSection.outerHTML = reviewSectionHTML;
    } else {
      document.body.insertAdjacentHTML('beforeend', reviewSectionHTML);
    }
  }

  // Function to check if the page is relevant for displaying the review section
  function isRelevantPage() {
    const page = window.location.pathname.split("/").pop();
    return page === 'place.html' || page === 'add_review.html';
  }

  if (isRelevantPage()) createReviewSection();
});

document.addEventListener('DOMContentLoaded', () => {
  const placeDetails = {
    name: 'Beautiful Place',
    host: 'John Doe',
    price: 150,
    description: 'Great place to stay!',
    amenities: ['WiFi', 'Kitchen', 'Heating'],
    reviews: [
      { user: 'Jane Doe', content: 'Great place to stay!', rating: 5 },
      { user: 'John Smith', content: 'Bullshit', rating: 1 }
    ]
  };

  // Function to display place details
  function displayPlaceDetails(place) {
    const placeDetailsSection = document.getElementById('place-details');
    if (!placeDetailsSection) return console.error("The element with ID 'place-details' was not found.");

    placeDetailsSection.innerHTML = '';
    const placeName = document.createElement('h2');
    placeName.textContent = place.name;

    const placeDescription = document.createElement('p');
    placeDescription.textContent = `Description: ${place.description}`;

    const placePrice = document.createElement('p');
    placePrice.textContent = `Price: $${place.price} per night`;

    const placeAmenities = document.createElement('p');
    placeAmenities.textContent = `Amenities: ${place.amenities.join(', ')}`;

    placeDetailsSection.append(placeName, placeDescription, placePrice, placeAmenities);
  }

  // Function to get place ID from URL
  function getPlaceIdFromURL() {
    return new URLSearchParams(window.location.search).get('placeId');
  }

  // Function to fetch place details
  async function fetchPlaceDetails(token, placeId) {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (!response.ok) throw new Error('Failed to fetch place details');
      const placeDetails = await response.json();
      displayPlaceDetails(placeDetails);
    } catch (error) {
      console.error('Error fetching place details:', error);
    }
  }

  const token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczMjcwNzg0MiwianRpIjoiOWUwODUyMjgtNzQ2ZC00MWI4LTliYjQtNDBjNDRkNDdmYWM3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6IjQ0MjJjY2I3LWExYTctNDQ5Ny05MjBjLTAzOGEwNzgxNzBmZCIsImlzX2FkbWluIjp0cnVlfSwibmJmIjoxNzMyNzA3ODQyLCJjc3JmIjoiZmFmNTYzNzYtOTVjYi00Y2Q4LWI4MzYtODA4YmQ5ODdjNDk5IiwiZXhwIjoxNzMyNzExNDQyfQ.xrz75nrLaE-dKE2W2ApZyClI5_Z6kvuRVsSgBwEJ8J8X8u5K0p8igk-Eg7xTSRHckxt_Nf3DrsK4o87Q1SNs9Q'; // Replace with actual token
  const placeId = '9b8ff017-dc65-4729-a910-08012e513c53'; // Replace with actual place ID
  fetchPlaceDetails(token, placeId);

  // Function to display reviews
  function displayReviews(reviews) {
    const reviewsSection = document.getElementById('reviews');
    reviews.forEach(review => {
      const reviewCard = document.createElement('div');
      reviewCard.className = 'review';
      reviewCard.innerHTML = `
        <p><strong>${review.user}</strong></p>
        <p>${review.content}</p>
        <p>Rating: ${generateStars(review.rating)}</p>
      `;
      reviewsSection.appendChild(reviewCard);
    });
  }

  // Function to generate star ratings
  function generateStars(rating) {
    return Array.from({ length: 5 }, (_, i) => i < rating ? '&#9733;' : '&#9734;').join('');
  }

  displayPlaceDetails(placeDetails);
  displayReviews(placeDetails.reviews);
  fetchPlaceDetails(token, placeId);
  getPlaceIdFromURL();
});

document.addEventListener('DOMContentLoaded', () => {
  const loginButton = document.getElementById('login-link');
  const logoutButton = document.createElement('a');
  logoutButton.id = 'logout-link';
  logoutButton.className = 'login-button';
  logoutButton.textContent = 'Logout';
  logoutButton.style.display = 'none';
  logoutButton.href = '#';
  document.querySelector('nav').appendChild(logoutButton);

  // Function to check if the user is logged in
  function isLoggedIn() {
    return document.cookie.split(';').some(item => item.trim().startsWith('token='));
  }

  if (isLoggedIn()) {
    if (loginButton) loginButton.style.display = 'none';
    logoutButton.style.display = 'block';
  }

  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = loginForm.elements['email'].value;
      const password = loginForm.elements['password'].value;
      await loginUser(email, password);
    });
  }

  // Function to log in the user
  async function loginUser(email, password) {
    const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    if (response.ok) {
      const data = await response.json();
      document.cookie = `token=${data.access_token}; path=/`;
      window.location.href = 'index.html';
    } else {
      alert('Login failed: ' + response.statusText);
    }
  }

  logoutButton.addEventListener('click', () => {
    document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    window.location.href = 'index.html';
  });
});

document.addEventListener('DOMContentLoaded', () => {
  // Function to check authentication
  function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    const logoutLink = document.getElementById('logout-link');
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
      loginLink.style.display = 'block';
      logoutLink.style.display = 'none';
      addReviewSection.style.display = 'none';
      window.location.href = 'index.html';
    } else {
      loginLink.style.display = 'none';
      logoutLink.style.display = 'block';
      addReviewSection.style.display = 'block';
      fetchPlaces(token);
      fetchPlaceDetails(token, getPlaceIdFromURL());
    }

    return token;
  }
  checkAuthentication();
});

// Event listener for price filter change
document.getElementById('price-filter').addEventListener('change', (event) => {
  const selectedPrice = event.target.value;
  const placeCards = document.querySelectorAll('.place-card');

  placeCards.forEach(card => {
    const price = parseFloat(card.querySelector('.place-price').textContent.replace('Price per night: $', ''));
    card.style.display = selectedPrice === 'All' || price <= parseFloat(selectedPrice) ? 'block' : 'none';
  });
});