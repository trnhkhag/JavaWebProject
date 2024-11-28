function addToCart(id, quantity) {
    $.ajax({
        type: "POST",
        url: "AddToCart",
        data: {
            productId: id,
            quantity: quantity
        },
        success: function (response) {
            // Show SweetAlert notification on success
            Swal.fire({
                title: 'Success!',
                text: response,  // Use the server response as the message
                icon: 'success',
                confirmButtonText: 'OK'
            });
        },
        error: function (xhr) {
            Swal.fire({
                title: 'Error!',
                text: xhr.responseText,  // Display server-provided error message
                icon: 'error',
                confirmButtonText: 'OK'
            });
        }
    });
}

function deleteFromCart(id) {
    $.ajax({
        type: "POST",
        url: "DeleteFromCart",
        data: {
            productId: id
        },
        success: function (response) {
            Swal.fire({
                title: 'Success!',
                text: response,  // Use the server response as the message if provided
                icon: 'success',
                confirmButtonText: 'OK'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Reload the page or update the cart UI after confirming
                    location.reload();
                }
            });
        },
        error: function () {
            Swal.fire({
                title: 'Error!',
                text: 'Failed to remove product from cart. Please try again.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        }
    });
}

function changeQuantity(id, quantityInput) {
    $.ajax({
        type: "POST",
        url: "ChangeQuantity",
        data: {
            productId: id,
            quantity: quantityInput.value
        },
        success: function (response) {
            Swal.fire({
                title: 'Success!',
                text: 'Quantity updated successfully.',
                icon: 'success',
                confirmButtonText: 'OK'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Reload the page or update the cart UI after confirming
                    location.reload();
                }
            });
        },
        error: function (xhr) {
            Swal.fire({
                title: 'Error!',
                text: xhr.responseText || 'Failed to change quantity. Please try again.',
                icon: 'error',
                confirmButtonText: 'OK'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Reload the page after error confirmation
                    location.reload();
                }
            });
        }
    });
}
