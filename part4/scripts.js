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