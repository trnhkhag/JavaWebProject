// Function to handle coupon code selection and apply changes to totals
function processCouponCode() {
    // Get the selected coupon code from the dropdown
    var couponCode = document.querySelector('select[name="coupon"]').value;

    // Get the current values from the page (subtotal, shipping, total)
    var subtotal = parseFloat(document.getElementById('subtotal').textContent);
    var shipping = parseFloat(document.getElementById('shipping').textContent);
    var discount = 0.0;
    var total = parseFloat(document.getElementById('total').textContent);

    // Check if a valid coupon code is selected
    if (couponCode === '') {
		location.reload();
        return; // Exit if no coupon is selected
    }

    // Variables to store new total and message
    var message = '';
    var newTotal = total; // Initialize with the current total

    // Process the coupon code
    switch (couponCode) {
        case "FREESHIP":
            message = "Free shipping applied!";
            shipping = 0; // Apply free shipping
            newTotal = subtotal + shipping; // Update total
            break;
        case "DISCOUNT100":
            if (subtotal >= 1000) {
                message = "Discount of $100 applied!";
				shipping = 2.0;
                discount = 100;
                newTotal = subtotal - discount + shipping; // Apply $100 discount
            } else {
                message = "Order must be at least $1000 to apply this coupon.";
            }
            break;
        case "DISCOUNT10P":
            if (subtotal >= 10000) {
				shipping = 2.0;
                discount = subtotal * 0.10;
                message = "10% discount applied! You saved $" + discount.toFixed(1);
                newTotal = subtotal - discount + shipping; // Apply 10% discount
            } else {
                message = "Order must be at least $10000 to apply this coupon.";
            }
            break;
        default:
            message = "Invalid coupon code.";
            break;
    }

    if (message.includes('applied')) {
        // Show success message if "applied" is in the message
        Swal.fire({
            title: 'Success',
            text: message,
            icon: 'success',  // Set the icon to success
            confirmButtonText: 'OK'
        }).then((result) => {
            if (result.isConfirmed) {
                // If message includes 'applied', update the order summary
                updateOrderSummary(subtotal, shipping, discount, newTotal);
            }
        });
    } else {
        // Show error message if "applied" is not in the message
        Swal.fire({
            title: 'Error',
            text: message,
            icon: 'error',  // Set the icon to error
            confirmButtonText: 'OK'
        }).then((result) => {
            if (result.isConfirmed) {
                // Reload the page if message does not include 'applied'
                location.reload();
            }
        });
    }
    

    // Update the message with SweetAlert
    // Swal.fire({
    //     title: 'Information',
    //     text: message,
    //     icon: 'info',
    //     confirmButtonText: 'OK'
    // }).then((result) => {
    //     if (result.isConfirmed) {
    //         if (message.includes('applied')) {
    //             updateOrderSummary(subtotal, shipping, discount, newTotal);
    //         } else {
    //             location.reload();
    //         }
    //     }
    // });
}

// Function to update the order summary on the webpage
function updateOrderSummary(subtotal, shipping, discount, total) {
    // Update the elements with the new values
    document.getElementById('subtotal').textContent = subtotal.toFixed(1) + '$';
    document.getElementById('shipping').textContent = shipping.toFixed(1) + '$';
    document.getElementById('discount').textContent = discount.toFixed(1) + '$';
    document.getElementById('total').textContent = total.toFixed(1) + '$';
}
