function validateEmail() {
	// Get the email
	const email = document.getElementById("email").value.trim();
	
	// Regular expressions for validation
	const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
	
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
	
	return true;
}

function validateCode() {
	// Get the code
	const code = document.getElementById("code").value.trim();
		
	// Define the regex pattern for a 6-digit code
	const sixDigitPattern = /^\d{6}$/;
	
	// Validate email format
	if (!sixDigitPattern.test(code)) {
		Swal.fire({
		    title: 'Error!',
		    text: 'Please enter a valid code.',
		    icon: 'error',
		    confirmButtonText: 'OK'
		});
		return false;
	}
		
	return true;
}

function validatePassword() {
	const password = document.getElementById("pass").value;
	const confirmPassword = document.getElementById("cpass").value;
	
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