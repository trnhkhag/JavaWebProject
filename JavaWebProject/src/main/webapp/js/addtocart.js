function addToCart(id, quantity) {
	$.ajax({
		type: "POST",
		url: "AddToCart",
		data: {
			productId: id,
			quantity: quantity
		},
		success: function (response) {
			alert("Product added to cart successfully!");
		},
		error: function () {
			alert("Failed to add product to cart. Please try again.");
		}
	});
}
