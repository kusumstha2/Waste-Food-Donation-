document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("editDonationForm");
  const donationsData = JSON.parse(localStorage.getItem("donations")) || [];

  // Get donation index from URL query (e.g., edit-donation.html?index=0)
  const urlParams = new URLSearchParams(window.location.search);
  const donationIndex = urlParams.get("index");

  // Fetch and load the donation data to edit
  if (donationIndex !== null) {
    const donation = donationsData[donationIndex];
    document.getElementById("donorName").value = donation.donorName;
    document.getElementById("donorNumber").value = donation.donorNumber;
    document.getElementById("foodName").value = donation.foodName;
    document.getElementById("foodType").value = donation.foodType;
    document.getElementById("description").value = donation.description;
    document.getElementById("expiryDate").value = donation.expiryDate;
    document.getElementById("location").value = donation.location;

    // Show the current image
    const imagePreview = document.getElementById("image-preview");
    const imgElement = document.createElement("img");
    imgElement.src = donation.foodImage;
    imagePreview.innerHTML = ''; // Clear any existing preview
    imagePreview.appendChild(imgElement);

    // Set up the form to save the edited donation
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      const updatedDonation = {
        donorName: document.getElementById("donorName").value,
        donorNumber: document.getElementById("donorNumber").value,
        foodName: document.getElementById("foodName").value,
        foodType: document.getElementById("foodType").value,
        description: document.getElementById("description").value,
        expiryDate: document.getElementById("expiryDate").value,
        location: document.getElementById("location").value,
        foodImage: donation.foodImage, // Keep the original image if not modified
      };

      // Check if the user selected a new image
      const newFoodImage = document.getElementById("foodImage").files[0];
      if (newFoodImage) {
        const reader = new FileReader();
        reader.onload = function () {
          updatedDonation.foodImage = reader.result;
          donationsData[donationIndex] = updatedDonation;
          localStorage.setItem("donations", JSON.stringify(donationsData));
          window.location.href = "food donation.html"; // Redirect after saving
        };
        reader.readAsDataURL(newFoodImage);
      } else {
        donationsData[donationIndex] = updatedDonation;
        localStorage.setItem("donations", JSON.stringify(donationsData));
        window.location.href = "food donation.html"; // Redirect after saving
      }
    });
  } else {
    alert("No donation found to edit.");
    window.location.href = "food donation.html"; // Redirect if no valid donation index is provided
  }
});
