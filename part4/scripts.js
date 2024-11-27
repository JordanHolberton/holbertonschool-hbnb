
document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
          event.preventDefault();
          const email = document.getElementById('email').value;
          const password = document.getElementById('password').value;
          try {
              await loginUser(email, password);
          } catch (error) {
              document.getElementById('error-message').textContent = 'Login failed: ' + error.message;
          }
      });
  }

  const placeDetails = document.getElementById('place-details');
  const reviewsSection = document.getElementById('reviews');
  const addReviewSection = document.getElementById('add-review');

  // Example data, replace with actual data from your API
  const place = {
      name: 'Place Name',
      host: 'Host Name',
      price: 100,
      description: 'A beautiful place to stay.',
      amenities: ['WiFi', 'Air Conditioning', 'Pool']
  };

  const reviews = [
      { comment: 'Great place!', user: 'User1', rating: 5 },
      { comment: 'Very comfortable.', user: 'User2', rating: 4 }
  ];

  // Populate place details
  const placeInfo = `
      <h2>${place.name}</h2>
      <p><strong>Host:</strong> ${place.host}</p>
      <p><strong>Price per night:</strong> $${place.price}</p>
      <p><strong>Description:</strong> ${place.description}</p>
      <p><strong>Amenities:</strong> ${place.amenities.join(', ')}</p>
  `;
  placeDetails.innerHTML = placeInfo;

  // Populate reviews
  if (reviews.length > 0) {
      reviews.forEach(review => {
          const reviewCard = document.createElement('div');
          reviewCard.className = 'review-card';

          const reviewContent = `
              <p><strong>Comment:</strong> ${review.comment}</p>
              <p><strong>User:</strong> ${review.user}</p>
              <p><strong>Rating:</strong> ${review.rating}</p>
          `;
          reviewCard.innerHTML = reviewContent;
          reviewsSection.appendChild(reviewCard);
      });
  } else {
      reviewsSection.innerHTML = '<p>No reviews yet.</p>';
  }

  // Check if user is logged in
  const userLoggedIn = true; // Replace with actual login check

  if (!userLoggedIn) {
      addReviewSection.innerHTML = '<button onclick="location.href=\'add_review.html\'">Add a Review</button>';
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

      if (response.ok) {
          const data = await response.json();
          document.cookie = `token=${data.access_token}; path=/`;
          window.location.href = 'index.html';
      } else {
          throw new Error(response.statusText);
      }
  } catch (error) {
      throw new Error('Network error: ' + error.message);
  }
}