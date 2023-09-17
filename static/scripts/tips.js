// camp_selector.js
const databaseData = JSON.parse(localStorage.getItem("databaseData"));
// Define an array to store unique camp names
const campNames = [];

// Loop through the dataset from the first page and extract unique camp names
databaseData.forEach((data) => {
  if (!campNames.includes(data.name)) {
    campNames.push(data.name);
  }
});

// Get the dropdown button and menu elements
const campDropdownBtn = document.getElementById("campDropdownBtn");
const campDropdownMenu = document.getElementById("campDropdownMenu");

// Create and append options to the dropdown menu
campNames.forEach((campName) => {
  const option = document.createElement("div");
  option.className = "dropdown-option";
  option.textContent = campName;
  option.addEventListener("click", () => {
    // Call the selectCamp function with the selected camp name
    selectCamp(campName);
  });
  campDropdownMenu.appendChild(option);
});

// Open the dropdown menu when clicking the button
campDropdownBtn.addEventListener("click", () => {
  campDropdownMenu.classList.toggle("show");
});

// Close the dropdown menu when clicking outside of it
window.addEventListener("click", (event) => {
  if (!event.target.matches("#campDropdownBtn")) {
    const dropdowns = document.getElementsByClassName("dropdown-menu");
    for (const dropdown of dropdowns) {
      if (dropdown.classList.contains("show")) {
        dropdown.classList.remove("show");
      }
    }
  }
});

// Add a function to select the camp
function selectCamp(camp) {
  // Call a function to fetch data based on the selected camp
  fetchDataForCamp(camp);
}

// Add a function to fetch and display data for the selected camp
function fetchDataForCamp(camp) {
  // Replace this with your code to fetch data and create cards based on the selected camp
  // Example:
  const cardGrid = document.getElementById("cardGrid");
  cardGrid.innerHTML = ""; // Clear existing cards

  // Dummy data for demonstration (replace with actual data retrieval)
  const dataForCamp = databaseData.filter((data) => data.name === camp);

  // Create a grid for the cards
  const cardGridContainer = document.createElement("div");
  cardGridContainer.className = "card-grid";

  // Create cards for the data
  dataForCamp.forEach((data) => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <div class="card-title">Name: ${data.name}</div>
      <div class="card-details">
        <p>State: ${data.state}</p>
        <p>lat: ${data.lat}</p>
        <p>lng: ${data.lng}</p>
        <p>magnitude: ${data.magnitude}</p>
        <!-- Add other data fields here -->
      </div>
    `;
    cardGridContainer.appendChild(card);
  });

  cardGrid.appendChild(cardGridContainer);
}

// Call fetchDataForCamp with a default camp or implement a default behavior
// fetchDataForCamp('KSA'); // Uncomment this line if you want to load data for 'KSA' camp by default
