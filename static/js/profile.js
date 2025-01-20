const userData = JSON.parse(localStorage.getItem("userData")) || {};

 
document.getElementById("profilePic").src = userData.profileImage || 'photo/profile.jpg';
document.getElementById("userName").textContent = userData.name;
document.getElementById("userEmail").textContent = userData.email;
document.getElementById("userPhone").textContent = userData.phone;
document.getElementById("userAddress").textContent = userData.address;

    


// Add click event listener to the profile picture
const profilePic = document.getElementById("profilePic");
const fileInput = document.getElementById("changeProfilePic");

profilePic.addEventListener("click", () => {
  // Trigger the file input dialog when clicking on the profile picture
  fileInput.click();
});

// Handle profile picture change
fileInput.addEventListener("change", (event) => {
  const newPic = event.target.files[0];

  if (newPic) {
    const picReader = new FileReader();
    picReader.onloadend = function () {
      // Update the profile picture on the page
      profilePic.src = picReader.result;

      // Save the updated profile picture to userData
      userData.profileImage = picReader.result;
      localStorage.setItem("userData", JSON.stringify(userData)); // Save updated data persistently
    };

    picReader.readAsDataURL(newPic); // Convert the selected file to Base64
  }
});