document.addEventListener('DOMContentLoaded', () => {
    const logoutButton = document.querySelector('a[href="#logout"]');
    const logoutModal = document.getElementById('logoutModal');
    const confirmLogoutButton = document.getElementById('confirmLogout');
    const cancelLogoutButton = document.getElementById('cancelLogout');

    // Show logout confirmation modal
    logoutButton.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default link behavior
        logoutModal.style.display = 'flex'; // Show the modal
    });

    // Cancel logout
    cancelLogoutButton.addEventListener('click', () => {
        logoutModal.style.display = 'none'; // Hide the modal
    });

    // Confirm logout
    confirmLogoutButton.addEventListener('click', async () => {
        const token = localStorage.getItem('token'); // Retrieve the token from localStorage

        if (!token) {
            alert('No token found. Please log in first.');
            logoutModal.style.display = 'none'; // Hide the modal
            return;
        }

        console.log(`Token being sent: ${token}`); // Debugging log for token

        try {
            const response = await fetch('/logout/', {
                method: 'POST',
                headers: {
                    'Authorization': `Token ${token}`, // Ensure "Token" prefix
                    'Content-Type': 'application/json', // Content type for JSON
                },
            });

            if (response.ok) {
                const responseData = await response.json();
                alert(responseData.message); // Show success message
                localStorage.removeItem('token'); // Remove token from localStorage
                window.location.href = '/home/'; // Redirect to the home page
            } else {
                const errorData = await response.json();
                alert(`Logout failed: ${errorData.message}`);
            }
        } catch (error) {
            console.error('Error during logout:', error);
            alert('An error occurred. Please try again.');
        }

        logoutModal.style.display = 'none'; // Hide the modal
    });
});
