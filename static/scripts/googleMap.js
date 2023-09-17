// Define pinImage variable
const pinImage = {
url: "https://maps.google.com/mapfiles/ms/icons/red-dot.png", // Default pin color
scaledSize: new google.maps.Size(32, 32),
};

// Function to initialize the map
function initializeMap() {
// Check if Google Maps API is loaded
if (typeof google === "undefined" || typeof google.maps === "undefined") {
    alert("Failed to load Google Maps API. Please try again later.");
    return;
}

const databaseData = [
    {
    lat: 10.862807,
    lng: 32.217636,
    magnitude: 5,
    name: "KSA camp 1",
    state: "Needs attention",
    },
    {
    lat: 12.862807,
    lng: 30.217636,
    magnitude: 5,
    name: "KSA camp 1",
    state: "Needs attention",
    },
    {
    lat: 13.412469,
    lng: 33.212439,
    magnitude: 7,
    name: "KSA camp 2",
    state: "Average",
    },
    {
    lat: 13.960106,
    lng: 32.991455,
    magnitude: 6,
    name: "KSA camp 3",
    state: "Good",
    },
    {
    lat: 12.289109,
    lng: 34.170909,
    magnitude: 4,
    name: "unicef 1",
    state: "Needs attention",
    },
    {
    lat: 14.003746,
    lng: 33.013196,
    magnitude: 8,
    name: "unicef 2",
    state: "Good",
    },
    {
    lat: 13.598206,
    lng: 22.724119,
    magnitude: 5,
    name: "unicef 3",
    state: "Average",
    },
    {
    lat: 12.679302,
    lng: 24.69908,
    magnitude: 6,
    name: "USA alpha 1",
    state: "Average",
    },
    {
    lat: 10.503905,
    lng: 33.312165,
    magnitude: 4,
    name: "USA alpha 2",
    state: "Good",
    },
    {
    lat: 15.601805,
    lng: 32.536853,
    magnitude: 6,
    name: "USA alpha 3",
    state: "Needs attention",
    },
    {
    lat: 12.71543,
    lng: 29.188732,
    magnitude: 7,
    name: "Kujakuja camp 1",
    state: "Needs attention",
    },
    {
    lat: 11.464537,
    lng: 24.442638,
    magnitude: 5,
    name: "Kujakuja camp 2",
    state: "Average",
    },
    {
    lat: 14.240297,
    lng: 32.987977,
    magnitude: 6,
    name: "Kujakuja camp 3",
    state: "Good",
    },
    // Add more data points as needed and try to make it from the database
];

const cardPopup = document.getElementById("cardPopup");
const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 8,
    zoomControl: false,
    mapTypeControl: false,
    streetViewControl: false,
    fullscreenControl: false,
});

// Create a function to handle marker click events
function handleMarkerClick(data) {
    const cardContent = `
    <div class="card">
    <div class="card-title">Name: ${data.name}</div>
    <div class="card-details">
        <p>State: ${data.state}</p>
        <p>Longitude: ${data.lng}</p>
        <p>Magnitude: ${data.magnitude}</p>
        <p>Latitude: ${data.lat}</p>
    </div>
    <div class="card-button">
        <a href="/tips"><button class="action-button">Take action</button></a>
    </div>
    </div>
`;
    cardPopup.innerHTML = cardContent;
    cardPopup.classList.add("active");
}

// Function to close the card
function closeCard() {
    cardPopup.classList.remove("active");
}

// Loop through the data and create markers
databaseData.forEach((data) => {
    let pinColor = "";
    if (data.state === "Needs attention") {
    pinColor = "red";
    } else if (data.state === "Average") {
    pinColor = "orange";
    } else {
    pinColor = "green";
    }

    const marker = new google.maps.Marker({
    position: { lat: data.lat, lng: data.lng },
    map: map,
    title: `Camp name: ${data.name}`,
    icon: {
        url: `https://maps.google.com/mapfiles/ms/icons/${pinColor}-dot.png`,
        scaledSize: new google.maps.Size(32, 32),
    },
    });
    localStorage.setItem("databaseData", JSON.stringify(databaseData));
    marker.addListener("click", () => {
    handleMarkerClick(data);
    });
});

// Fit the map to the markers
const bounds = new google.maps.LatLngBounds();
databaseData.forEach((data) =>
    bounds.extend(new google.maps.LatLng(data.lat, data.lng))
);
map.fitBounds(bounds);

// Close the card when clicking on the map
map.addListener("click", closeCard);
}
function showMapPage() {
window.location.href = "/home.html";
}
function showActionsPage() {
// Replace 'actions-page.html' with the actual URL of the Actions page
window.location.href = "/tips.html";
}
// Call the initializeMap function when the DOM is ready
document.addEventListener("DOMContentLoaded", initializeMap);
