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