// Get the donation list container
const donationList = document.getElementById('donation-list');

// Fetch donations from localStorage
let donations = JSON.parse(localStorage.getItem('donations')) || [];

// Function to render donation cards
function renderDonations() {
  donationList.innerHTML = ''; // Clear the list

  if (donations.length === 0) {
    donationList.innerHTML = '<p>No donations available yet.</p>';
  } else {
    donations.forEach((donation, index) => {
      const card = document.createElement('div');
      card.className = 'card';

      const img = document.createElement('img');
      img.src = donation.foodImage;
      img.alt = donation.foodName;
      card.appendChild(img);

      const details = `
        <h3>${donation.foodName}</h3>
        <p><strong>Donor:</strong> ${donation.donorName}</p>
        <p><strong>Type:</strong> ${donation.foodType}</p>
        <button class="view-details-btn" onclick="viewDetails(${index})">View Details</button>
        <button class="edit-btn" onclick="editDonation(${index})">Edit</button>
        <button class="delete-btn" onclick="deleteDonation(${index})">Delete</button>
      `;
      card.innerHTML += details;

      donationList.appendChild(card);
    });
  }
}

// Function to show details in the same card
function viewDetails(index) {
  const donation = donations[index];
  const detailsDiv = document.createElement('div');
  
  // Add the back button
  detailsDiv.innerHTML = `
    <button class="back-btn" onclick="goBack(${index})">← Back</button>
    <p><strong>Donor:</strong> ${donation.donorName}</p>
    <p><strong>Food Name:</strong> ${donation.foodName}</p>
    <p><strong>Food Type:</strong> ${donation.foodType}</p>
    <p><strong>Description:</strong> ${donation.description}</p>
    <p><strong>Location:</strong> ${donation.location}</p>
    <p><strong>Expiry Date:</strong> ${donation.expiryDate}</p>
    <img src="${donation.foodImage}" alt="${donation.foodName}" style="width: 100%; max-width: 300px;">
  `;
  
  const card = donationList.children[index];
  card.innerHTML = ''; // Clear the card
  card.appendChild(detailsDiv);
}

// Function to go back to the donation card view
function goBack(index) {
  renderDonations(); // Re-render the donation list (restores the original view)
  // Optionally, you can also scroll to the top of the donation list:
  donationList.scrollIntoView({ behavior: 'smooth' });
}

// Function to delete a donation with confirmation
function deleteDonation(index) {
  const confirmDelete = confirm('Are you sure you want to delete this donation?');
  if (confirmDelete) {
    donations.splice(index, 1); // Remove the donation from the array
    localStorage.setItem('donations', JSON.stringify(donations)); // Save updated donations
    renderDonations(); // Re-render the donation list
  }
}

// Function to edit a donation
function editDonation(index) {
  window.location.href = `/editdonation/?index=${index}`;
}

// Add functionality to the close button
document.getElementById("closeButton").addEventListener("click", function () {
  window.location.href = "{% url 'foodapp:dashboard' %}"; // Redirect to index.html
});

// Initial render
renderDonations();
