function validate() {
    let user = document.forms["login"]["username"].value;
    let pass = document.forms["login"]["password"].value;

    // Check if username is empty
    if (user === "") {
        Swal.fire({
            title: 'Missing Username',
            text: 'Please enter your username.',
            icon: 'warning',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // Check if password is empty
    if (pass === "") {
        Swal.fire({
            title: 'Missing Password',
            text: 'Please enter your password.',
            icon: 'warning',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // Check if password length is less than 6 characters
    if (pass.length < 6) {
        Swal.fire({
            title: 'Password Too Short',
            text: 'Password must be at least 6 characters long.',
            icon: 'warning',
            confirmButtonText: 'OK'
        });
        return false;
    }

    // If all checks pass, allow form submission
    return true;
}