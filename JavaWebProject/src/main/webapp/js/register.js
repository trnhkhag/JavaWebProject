// registerValidation.js

// Function to validate form fields
function validate() {
    // Get form fields
    const username = document.getElementById("user").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const password = document.getElementById("pass").value;
    const confirmPassword = document.getElementById("confpass").value;

    // Regular expressions for validation
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    const phonePattern = /^[0-9]{10}$/; // Adjust this pattern as needed for different formats

    // Validate username (non-empty)
    if (username === "") {
        Swal.fire({
            title: 'Error!',
            text: 'Username is required.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // Validate email format
    if (!emailPattern.test(email)) {
        Swal.fire({
            title: 'Error!',
            text: 'Please enter a valid email address.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // Validate phone number format
    if (!phonePattern.test(phone)) {
        Swal.fire({
            title: 'Error!',
            text: 'Please enter a valid 10-digit phone number.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // Validate password length
    if (password.length < 6) {
        Swal.fire({
            title: 'Error!',
            text: 'Password must be at least 6 characters long.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // Validate confirm password matches password
    if (password !== confirmPassword) {
        Swal.fire({
            title: 'Error!',
            text: 'Passwords do not match.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // If all validations pass
    return true;
}
