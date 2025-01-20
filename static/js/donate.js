document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('.donate-form');
  const foodImageInput = document.getElementById('foodImage');
  const quantityInput = document.getElementById('quantity');
  const expiryDateInput = document.getElementById('expiryDate');
  const today = new Date().toISOString().split('T')[0];

  // Set minimum expiry date to today
  expiryDateInput.setAttribute('min', today);

  // Form submit event
  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Validate file size (max 5MB)
    const file = foodImageInput.files[0];
    if (file && file.size > 5 * 1024 * 1024) {
      alert('Food image size must be less than 5MB');
      return;
    }

    // Ensure all fields are filled
    const inputs = form.querySelectorAll('input, select, textarea');
    for (const input of inputs) {
      if (!input.value) {
        alert(`Please fill out the ${input.previousElementSibling.textContent} field`);
        input.focus();
        return;
      }
    }

    // Successful validation
    alert('Thank you for your donation!');
    form.reset();
    document.getElementById('image-preview').innerHTML = ''; // Clear image preview
  });

  // Preview image after selection
  foodImageInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const previewContainer = document.getElementById('image-preview');
    previewContainer.innerHTML = ''; // Clear previous preview

    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        const img = document.createElement('img');
        img.src = reader.result;
        previewContainer.appendChild(img);
      };
      reader.readAsDataURL(file);
    }
  });
});
