document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const storedData = JSON.parse(localStorage.getItem("userData"));

    if (storedData && storedData.email === email && storedData.password === password) {
        // alert("Login successful!");
        window.location.href = "index.html";
    } else {
        alert("Invalid email or password.");
    }
});