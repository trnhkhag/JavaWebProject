function deleteFromCart(id) {
	$.ajax({
    type: "POST",
    url: "DeleteFromCart",
    data: {
      productId : id
    },
    success: function (response) {
      console.log("Deleted from cart successfully")
    }
  });
  location.reload();
}