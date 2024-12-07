<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="en">

<head>
	<title>BKTM WATCH | Checkout</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	<link href="https://fonts.googleapis.com/css?family=Poppins:200,300,400,500,600,700,800&display=swap"
		rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Lora:400,400i,700,700i&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Amatic+SC:400,700&display=swap" rel="stylesheet">

	<link rel="stylesheet" href="css/open-iconic-bootstrap.min.css">
	<link rel="stylesheet" href="css/animate.css">

	<link rel="stylesheet" href="css/owl.carousel.min.css">
	<link rel="stylesheet" href="css/owl.theme.default.min.css">
	<link rel="stylesheet" href="css/magnific-popup.css">

	<link rel="stylesheet" href="css/aos.css">

	<link rel="stylesheet" href="css/ionicons.min.css">

	<link rel="stylesheet" href="css/bootstrap-datepicker.css">
	<link rel="stylesheet" href="css/jquery.timepicker.css">

	<link rel="stylesheet" href="fontawesome-free-6.2.0-web/css/all.css">

	<link rel="stylesheet" href="css/flaticon.css">
	<link rel="stylesheet" href="css/icomoon.css">
	<link rel="stylesheet" href="css/style.css">
	<link rel="stylesheet" href="css/mystyle.css">
	<script src="js/sweetalert.all.min.js"></script>
	<script src="js/coupon.js"></script>
	<script src="js/checkout.js"></script>
</head>

<body class="goto-here">
	<jsp:include page="header.jsp"></jsp:include>
	<!-- END nav -->

	<div class="hero-wrap hero-bread" style="background-image: url('images/bg_1.jpeg');">
		<div class="container">
			<div class="row no-gutters slider-text align-items-center justify-content-center">
				<div class="col-md-9 ftco-animate text-center">
					<p class="breadcrumbs"><span class="mr-2"><a href="index.html">Home</a></span> <span>Checkout</span>
					</p>
					<h1 class="mb-0 bread">Checkout</h1>
				</div>
			</div>
		</div>
	</div>

	<section class="ftco-section">
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-xl-7 ftco-animate">
					<form method="post" action="CreateOrder" class="billing-form" id="checkout-form" onsubmit="return validateUserInfo()">
						<h3 class="mb-4 billing-heading">Billing Address</h3>
						<div class="row align-items-end">
							<div class="col-md-12">
								<div class="form-group">
									<label for="fullname">Full Name<span class="important"> *</span></label>
									<input name="fullname" type="text" class="form-control" placeholder="John M. Doe" value="${currentUser.fullname}">
								</div>
							</div>
							<div class="col-md-12">
								<div class="form-group">
									<label for="address">Address<span class="important"> *</span></label>
									<input name="address" type="text" class="form-control" placeholder="542 W, 15th Street" value="${currentUser.address}">
								</div>
							</div>
							<div class="col-md-12">
								<div class="form-group">
									<label for="phone">Phone<span class="important"> *</span></label>
									<input name="phone" type="text" class="form-control" placeholder="0123456789" value="${currentUser.phone}">
								</div>
							</div>
							<div class="col-md-12">
								<div class="form-group">
									<label for="email">Email</label>
									<input name="email" type="text" class="form-control" placeholder="john@example.com" value="${currentUser.email}">
								</div>
							</div>
							<!-- <div class="col-md-12">
								<div class="form-group">
									<label for="note">Note</label>
									<textarea name="note" class="form-control note" placeholder=""></textarea>
								</div>
							</div> -->
							<div class="col-md-12">
    							<div class="form-group">
        							<label for="coupon">Coupon Code</label>
        							<select name="coupon" class="form-control" onchange="processCouponCode(this.value)">
            							<option value="">No Coupon</option>
            							<option value="FREESHIP">Free ship coupon</option>
            							<option value="DISCOUNT100">Discount $100 (For orders from $1000)</option>
            							<option value="DISCOUNT10P">Discount 10% (For orders from $10000)</option>
        							</select>
    							</div>
							</div>
						</div>
					</form><!-- END -->
				</div>
				<div class="col-xl-5">
					<div class="row mt-5 pt-3">
						<div class="col-md-12 d-flex mb-5">
							<div class="cart-detail cart-total p-3 p-md-4">
								<h3 class="billing-heading mb-4">Your Order</h3>
								<p class="d-flex">
									<span>Subtotal</span>
									<span id="subtotal">${sessionScope.subtotal}$</span>
								</p>
								<p class="d-flex">
									<span>Shipping</span>
									<span id="shipping">${sessionScope.shipping}$</span>
								</p>
								<p class="d-flex">
									<span>Discount</span>
									<span id="discount">0$</span>
								</p>
								<hr>
								<p class="d-flex total-price">
									<span>Total</span>
									<span id="total">${sessionScope.total}$</span>
								</p>
							</div>
						</div>
						<div class="col-md-12">
							<div class="cart-detail p-3 p-md-4">
								<h3 class="billing-heading mb-3">Payment Options</h3>
								<div class="form-group">
									<div class="col-md-12">
										<div class="radio">
											<label><input type="radio" name="optradio" class="mr-2" checked> Cash</label>
										</div>
									</div>
								</div>
								<div class="form-group">
									<div class="col-md-12">
										<div class="radio">
											<label><input type="radio" name="optradio" class="mr-2"> Credit cards</label>
										</div>
									</div>
								</div>
								<div class="form-group">
									<div class="col-md-12">
										<div class="radio">
											<label><input type="radio" name="optradio" class="mr-2"> Mobile payments</label>
										</div>
									</div>
								</div>
								<p><button type="submit" form="checkout-form" class="btn btn-primary py-3 px-4">Continue Checkout</button></p>
							</div>
						</div>
					</div>
				</div> <!-- .col-md-8 -->
			</div>
		</div>
	</section> <!-- .section -->

	<footer>
		<div class="Our_social_media">
			<a href="#"><i class="fa-brands fa-facebook"></i></a>
			<a href="#"><i class="fa-brands fa-instagram"></i></a>
			<a href="#"><i class="fa-brands fa-twitter"></i></a>
			<a href="#"><i class="fa-brands fa-youtube"></i></a>
		</div>
		<div class="more_info">
			<a href="#">Contact us</a>
			<a href="#">Our Services</a>
			<a href="#">Privacy Policy</a>
			<a href="#">Terms & Conditions</a>
			<a href="#">Career</a>
		</div>
		<p>INFERNO Copyright Â© 2021 Inferno - All rights reserved || Designed By: Mahesh</p>
	</footer>



	<!-- loader -->
	<div id="ftco-loader" class="show fullscreen"><svg class="circular" width="48px" height="48px">
			<circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee" />
			<circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10"
				stroke="#F96D00" />
		</svg></div>


	<script src="js/jquery.min.js"></script>
	<script src="js/jquery-migrate-3.0.1.min.js"></script>
	<script src="js/popper.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/jquery.easing.1.3.js"></script>
	<script src="js/jquery.waypoints.min.js"></script>
	<script src="js/jquery.stellar.min.js"></script>
	<script src="js/owl.carousel.min.js"></script>
	<script src="js/jquery.magnific-popup.min.js"></script>
	<script src="js/aos.js"></script>
	<script src="js/jquery.animateNumber.min.js"></script>
	<script src="js/bootstrap-datepicker.js"></script>
	<script src="js/scrollax.min.js"></script>
	<script
		src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVWaKrjvy3MaE7SQ74_uJiULgl1JY0H2s&sensor=false"></script>
	<script src="js/google-map.js"></script>
	<script src="js/main.js"></script>

	<script>
		$(document).ready(function () {

			var quantitiy = 0;
			$('.quantity-right-plus').click(function (e) {

				// Stop acting like a button
				e.preventDefault();
				// Get the field name
				var quantity = parseInt($('#quantity').val());

				// If is not undefined

				$('#quantity').val(quantity + 1);


				// Increment

			});

			$('.quantity-left-minus').click(function (e) {
				// Stop acting like a button
				e.preventDefault();
				// Get the field name
				var quantity = parseInt($('#quantity').val());

				// If is not undefined

				// Increment
				if (quantity > 0) {
					$('#quantity').val(quantity - 1);
				}
			});

		});
	</script>

</body>

</html>