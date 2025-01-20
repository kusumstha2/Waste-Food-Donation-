// Get elements
const logoutLink = document.querySelector('a[href="#logout"]');
const logoutModal = document.getElementById('logoutModal');
const confirmLogout = document.getElementById('confirmLogout');
const cancelLogout = document.getElementById('cancelLogout');

const donateButton = document.querySelector('.donate-btn');  // Get donate button
const donateModal = document.getElementById('donateModal');

const profileLink = document.querySelector('a[href="#profile"]');
const profileModal = document.getElementById('profileModal');
const profileModalBody = document.getElementById('profileModalBody');

const modalBody = document.getElementById('modalBody');

// Show the modal when the logout link is clicked
logoutLink.addEventListener('click', (event) => {
  event.preventDefault();
  logoutModal.style.display = 'flex';
});

// Hide the modal when "Cancel" is clicked
cancelLogout.addEventListener('click', () => {
  logoutModal.style.display = 'none';
});

// Handle logout confirmation
confirmLogout.addEventListener('click', () => {
  logoutModal.style.display = 'none';
  // Redirect to the login page (replace with your login page URL)
  window.location.href = 'login.html';
});

// Add and remove class to disable body scroll
const disableBodyScroll = () => {
  document.body.style.overflow = 'hidden'; // Prevent scroll
};

const enableBodyScroll = () => {
  document.body.style.overflow = ''; // Restore scroll
};

// Add event listener to Donate Now button
donateButton.addEventListener('click', () => {
  // Fetch content from donate.html and insert it into the modal
  fetch('donate.html')
  .then(response => response.text())
  .then(html => {
      modalBody.innerHTML = html; // Insert HTML content
      donateModal.style.display = 'flex'; // Show the modal
      disableBodyScroll(); // Disable scrolling
  })
  .catch(error => {
      console.error('Error loading donate.html:', error);
  });
});

  // Close the modal when clicking outside the modal content
  window.addEventListener('click', (event) => {
    if (event.target === donateModal) {
        donateModal.style.display = 'none';
        modalBody.innerHTML = ''; // Clear the modal content
        enableBodyScroll(); // Eable scrolling
    }
});

// Fetch Profile Content
profileLink.addEventListener('click', (event) => {
  event.preventDefault();
  fetch('profile.html')
    .then(response => response.text())
    .then(html => {
      profileModalBody.innerHTML = html;

      const userData = JSON.parse(localStorage.getItem("userData")) || {};
      const profilePic = document.getElementById("profilePic");

      // Populate user data
      profilePic.src = userData.profileImage || '../photo/profile.jpg';
      document.getElementById("userName").textContent = userData.name || 'Guest';
      document.getElementById("userEmail").textContent = userData.email || '';
      document.getElementById("userPhone").textContent = userData.phone || '';
      document.getElementById("userAddress").textContent = userData.address || '';

      // Handle profile picture update
      const fileInput = document.getElementById("changeProfilePic");
      profilePic.addEventListener("click", () => fileInput.click());
      fileInput.addEventListener("change", (event) => {
        const newPic = event.target.files[0];
        if (newPic) {
          const reader = new FileReader();
          reader.onloadend = () => {
            profilePic.src = reader.result;
            userData.profileImage = reader.result;
            localStorage.setItem("userData", JSON.stringify(userData));
          };
          reader.readAsDataURL(newPic);
        }
      });

      profileModal.style.display = 'flex';
    })
    .catch(error => console.error('Error loading profile.html:', error));
});

  // Close the modal when clicking outside the modal content
  window.addEventListener('click', (event) => {
    if (event.target === profileModal) {
        profileModal.style.display = 'none';
        modalBody.innerHTML = ''; // Clear the modal content
        enableBodyScroll(); // Eable scrolling
    }
});
