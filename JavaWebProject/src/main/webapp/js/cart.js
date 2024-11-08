function addToCart(id, quantity) {
	console.log("Add to cart")
    $.ajax({
        type: "POST",
        url: "AddToCart",
        data: {
            productId: id,
            quantity: quantity
        },
        success: function (response) {
			alert("Added")
            // Show SweetAlert notification on success
            //Swal.fire({
            //    title: 'Success!',
            //    text: response,  // Use the server response as the message
            //    icon: 'success',
            //    confirmButtonText: 'OK'
            //});
        },
        error: function () {
            Swal.fire({
                title: 'Error!',
                text: 'Failed to add product to cart. Please try again.',
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
			alert("Product removed from cart successfully!");
			location.reload();
		},
		error: function () {
			alert("Failed to remove product from cart. Please try again.");
		}
	});
}

function changeQuantity(id, quantityInput) {
	$.ajax({
    type: "POST",
    url: "ChangeQuantity",
    data: {
      productId : id,
      quantity : quantityInput.value
    },
    success: function (response) {
      console.log("Changed quantity successfully")
    }
  });
  location.reload();
}