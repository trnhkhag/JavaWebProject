function addToCart(id, quantity) {
	$.ajax({
    type: "POST",
    url: "AddToCart",
    data: {
      productId : id,
      quantity : quantity
    },
    success: function (response) {
      console.log("Added to cart successfully")
    }
  });
}