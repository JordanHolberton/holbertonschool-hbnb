/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    // Example data for places
    const places = [
        { name: 'Place 1', price_per_night: 100 },
        { name: 'Place 2', price_per_night: 150 },
        { name: 'Place 3', price_per_night: 200 }
    ];

    // Function to create place cards
    function createPlaceCard(place) {
        const card = document.createElement('div');
        card.className = 'place-card';

        const name = document.createElement('h3');
        name.textContent = place.name;
        card.appendChild(name);

        const price = document.createElement('p');
        price.textContent = `Price per night: $${place.price_per_night}`;
        card.appendChild(price);

        const button = document.createElement('button');
        button.className = 'details-button';
        button.textContent = 'View Details';
        card.appendChild(button);

        return card;
    }

    // Function to populate places list
    function populatePlacesList() {
        const placesList = document.getElementById('places-list');
        places.forEach(place => {
            const card = createPlaceCard(place);
            placesList.appendChild(card);
        });
    }

    // Populate places list on page load
    populatePlacesList();
});

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
            <div class="place-info">
                <h2>${place.name}</h2>
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
                <p>Rating: ${review.rating}</p>
            `;
            reviewsSection.appendChild(reviewCard);
        });
    }

    function checkUserLoggedIn() {
        // Simulate user login check
        return true; // Change this based on actual login status
    }

    function setupAddReviewSection() {
        const addReviewSection = document.getElementById('add-review');
        if (checkUserLoggedIn()) {
            addReviewSection.innerHTML = `
                <h2>Add a Review</h2>
                <form id="review-form" class="form">
                    <label for="review-text">Review:</label>
                    <textarea id="review-text" name="review-text" required></textarea>
                    <label for="rating">Rating:</label>
                    <select id="rating" name="rating" required>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                    <button type="submit">Submit</button>
                </form>
            `;
        } else {
            addReviewSection.innerHTML = `
                <button onclick="window.location.href='add_review.html'">Add a Review</button>
            `;
        }
    }

    displayPlaceDetails(placeDetails);
    displayReviews(placeDetails.reviews);
    setupAddReviewSection();
});