function validateUserInfo() {
    // Get form fields
    const fullname = document.forms["checkout-form"]["fullname"].value.trim();
    const address = document.forms["checkout-form"]["address"].value.trim();
    const phone = document.forms["checkout-form"]["phone"].value.trim();
    const email = document.forms["checkout-form"]["email"].value.trim();
    
    // Check if required fields are empty
    if (fullname === "") {
        Swal.fire({
            icon: 'warning',
            title: 'Validation Error',
            text: 'Full Name is required.',
            confirmButtonText: 'OK'
        });
        return false;
    }
    
    if (address === "") {
        Swal.fire({
            icon: 'warning',
            title: 'Validation Error',
            text: 'Address is required.',
            confirmButtonText: 'OK'
        });
        return false;
    }
    
    // Phone number validation
    if (phone === "") {
        Swal.fire({
            icon: 'warning',
            title: 'Validation Error',
            text: 'Phone number is required.',
            confirmButtonText: 'OK'
        });
        return false;
    } else if (!/^\d{10}$/.test(phone)) {
        Swal.fire({
            icon: 'warning',
            title: 'Invalid Phone Number',
            text: 'Please enter a valid 10-digit phone number.',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // Optional email validation
    if (email !== "" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        Swal.fire({
            icon: 'warning',
            title: 'Invalid Email',
            text: 'Please enter a valid email address.',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // If all validations pass, show success alert and allow form submission
    Swal.fire({
        icon: 'success',
        title: 'Checkout Successful',
        text: 'Your order has been successfully placed!',
        confirmButtonText: 'OK'
    }).then((result) => {
        if (result.isConfirmed) {
            // After the user confirms the success alert, submit the form
            document.forms["checkout-form"].submit();
        }
    });

    // Prevent form submission until user confirms the success alert
    return false;
}
