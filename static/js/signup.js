document.getElementById("signupForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirmPassword = document.getElementById("confirmPassword").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const address = document.getElementById("address").value.trim();
    const profileImage = document.getElementById("profileImage").files[0];

    if (name === "" || email === "" || password === "" || phone === "" || address === "") {
        alert("Please fill out all fields.");
        return;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
    }

    // Prepare the data object
    const userData = {
        name,
        email,
        phone,
        address,
        password,
        confirmPassword,
        profileImage: null, // Placeholder for the base64 image data
    };

    if (profileImage) {
        const reader = new FileReader();

        reader.onloadend = async function () {
            userData.profileImage = reader.result;

            await sendSignupRequest(userData); // Call the async function to send the request
        };

        reader.readAsDataURL(profileImage);
    } else {
        // If no profile image, proceed directly
        await sendSignupRequest(userData);
    }
});

// Async function to send the sign-up request
async function sendSignupRequest(userData) {
    const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    try {
        const response = await fetch('/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify(userData),
        });

        if (response.ok) {
            const result = await response.json();
            alert('Sign-up successful!');
            window.location.href = '/home/';
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.error || 'Sign-up failed!'}`);
        }
    } catch (error) {
        console.error('Error during sign-up:', error);
        alert('An unexpected error occurred. Please try again later.');
    }
}
