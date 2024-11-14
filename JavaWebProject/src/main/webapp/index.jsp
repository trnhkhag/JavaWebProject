<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="en">

<head>
	<title>BKMT WATCH | Home</title>
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
</head>

<body class="goto-here">
	<jsp:include page="header.jsp"></jsp:include>
	<!-- END nav -->

	<section id="home-section" class="hero">
		<div class="home-slider owl-carousel">
			<div class="slider-item" style="background-image: url(images/bg_1.jpeg);">
				<div class="overlay"></div>
				<div class="container">
					<div class="row slider-text justify-content-center align-items-center" data-scrollax-parent="true">

						<div class="col-md-12 ftco-animate text-center">
							<h1 class="mb-2">What time is it ?</h1>
							<p><a href="#" class="btn btn-primary">View Details</a></p>
						</div>

					</div>
				</div>
			</div>

			<div class="slider-item" style="background-image: url(images/background_watch.jpeg);">
				<div class="overlay"></div>
				<div class="container">
					<div class="row slider-text justify-content-center align-items-center" data-scrollax-parent="true">

						<div class="col-sm-12 ftco-animate text-center">
							<h1 class="mb-2">Don't waste your time</h1>
							<p><a href="#" class="btn btn-primary">View Details</a></p>
						</div>

					</div>
				</div>
			</div>
		</div>
	</section>

	<section class="ftco-section">
		<div class="container">
			<div class="row no-gutters ftco-services">
				<div id="c2" class="col-md-3 text-center d-flex align-self-stretch ftco-animate">
					<div class="media block-6 services mb-md-0 mb-4">
						<div class="icon bg-color-1 active d-flex justify-content-center align-items-center mb-2">
							<span class="flaticon-shipped"></span>
						</div>
						<div class="media-body">
							<h3 class="heading">Free Shipping</h3>
							<span>On order over $100.000</span>
						</div>
					</div>
				</div>

				<div class="col-md-3 text-center d-flex align-self-stretch ftco-animate">
					<div id="c1" class="media block-6 services mb-md-0 mb-4">
						<div class="icon bg-color-3 d-flex justify-content-center align-items-center mb-2">
							<span class="flaticon-award"></span>
						</div>
						<div class="media-body">
							<h3 class="heading">Superior Quality</h3>
							<span>Quality Products</span>
						</div>
					</div>
				</div>
				<div class="col-md-3 text-center d-flex align-self-stretch ftco-animate">
					<div id="c3" class="media block-6 services mb-md-0 mb-4">
						<div class="icon bg-color-4 d-flex justify-content-center align-items-center mb-2">
							<span class="flaticon-customer-service"></span>
						</div>
						<div class="media-body">
							<h3 class="heading">Support</h3>
							<span>24/7 Support</span>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<section class="ftco-section ftco-category ftco-no-pt">
		<div class="container">
			<div class="row">
				<div class="col-md-8">
					<div class="row">
						<div class="col-md-6 order-md-last align-items-stretch d-flex">
							<div class="category-wrap-2 ftco-animate img align-self-stretch d-flex"
								style="background-image: url(images/category.jpeg);">
								<div class="text text-center" style="margin-top: 200px;">
									<p><a href="Shop?page=1" class="btn btn-primary">Shop now</a></p>
								</div>
							</div>
						</div>
						<div class="col-md-6">
							<div class="category-wrap ftco-animate img mb-4 d-flex align-items-end"
								style="background-image: url(images/bg_watch1.jpg);">
								<div class="text px-3 py-1">
									<h2 class="mb-0"><a href="#">MEN'S WATCHES</a></h2>
								</div>
							</div>
							<div class="category-wrap ftco-animate img d-flex align-items-end"
								style="background-image: url(images/bg_watch2.jpg);">
								<div class="text px-3 py-1">
									<h2 class="mb-0"><a href="#">WOMAN'S WATCHES</a></h2>
								</div>
							</div>
						</div>
					</div>
				</div>

				<div class="col-md-4">
					<div class="category-wrap ftco-animate img mb-4 d-flex align-items-end"
						style="background-image: url(images/bg_watch3.jpg);">
						<div class="text px-3 py-1">
							<h2 class="mb-0"><a href="#">COUPLE'S WATCHES</a></h2>
						</div>
					</div>
					<div class="category-wrap ftco-animate img d-flex align-items-end"
						style="background-image: url(images/bg_watch4.jpg);">
						<div class="text px-3 py-1">
							<h2 class="mb-0"><a href="#">UNISEX'S WATCHES</a></h2>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<section class="ftco-section">
		<div class="container">
			<div class="row justify-content-center mb-3 pb-3">
				<div class="col-md-12 heading-section text-center ftco-animate">
					<span class="subheading">Featured Products</span>
					<h2 class="mb-4">Our New Products</h2>
				</div>
			</div>
		</div>
		<div class="container">
			<div class="row">
			<c:forEach items="${topplist}" var="p">
				<div class="col-md-6 col-lg-3 ftco-animate">
					<div class="product">
						<a href="${pageContext.request.contextPath}/ProductDetail?pid=${p.id}" class="img-prod"><img class="img-fluid" src="${p.image}"
								alt="Colorlib Template">
							<div class="overlay"></div>
						</a>
						<div class="text py-3 pb-4 px-3 text-center">
							<h3><a href="${pageContext.request.contextPath}/ProductDetail?pid=${p.id}">${p.name}</a></h3>
							<div class="d-flex">
								<div class="pricing">
									<p class="price"><span class="price">$${p.price}</span></p>
								</div>
							</div>
							<div class="bottom-area d-flex px-3">
								<div class="m-auto d-flex">
									<a href="${pageContext.request.contextPath}/ProductDetail?pid=${p.id}"
										class="add-to-cart d-flex justify-content-center align-items-center text-center">
										<span><i class="ion-ios-menu"></i></span>
									</a>
									<a href="#" class="buy-now d-flex justify-content-center align-items-center mx-1" onclick="event.preventDefault(); addToCart(${p.id}, 1)">
										<span><i class="ion-ios-cart"></i></span>
									</a>
									<a href="#" class="heart d-flex justify-content-center align-items-center ">
										<span><i class="ion-ios-heart"></i></span>
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</c:forEach>
				
				
				
			</div>
		</div>
	</section>

	<section class="ftco-section img" style="background-image: url(images/bg_watch5.jpg);">
		<div class="container">
			<div class="row justify-content-end">
				<div class="col-md-6 heading-section ftco-animate deal-of-the-day ftco-animate">
					<span class="subheading">Best Price For You</span>
					<h2 class="mb-4" style="color:#fff">Deal of the day</h2>
					<h3><a href="#">Silver Watch</a></h3>
					<span class="price">$100.000 <a href="#">now $95.000 only</a></span>
					<div id="timer" class="d-flex mt-5">
						<div class="time" id="days"></div>
						<div class="time pl-3" id="hours"></div>
						<div class="time pl-3" id="minutes"></div>
						<div class="time pl-3" id="seconds"></div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<section class="ftco-section testimony-section">
		<div class="container">
			<div class="row justify-content-center mb-5 pb-3">
				<div class="col-md-7 heading-section ftco-animate text-center">
					<span class="subheading">Testimony</span>
					<h2 class="mb-4">Our satisfied customer says</h2>
					<p>special day has special watch</p>
				</div>
			</div>
			<div class="row ftco-animate">
				<div class="col-md-12">
					<div class="carousel-testimony owl-carousel">
						<div class="item">
							<div class="testimony-wrap p-4 pb-5">
								<div class="user-img mb-5" style="background-image: url(images/person_1.jpg)">
									<span class="quote d-flex align-items-center justify-content-center">
										<i class="icon-quote-left"></i>
									</span>
								</div>
								<div class="text text-center">
									<p class="mb-5 pl-4 line">best service,the watch so beautiful.</p>
									<p class="name">Garreth Smith</p>
									<span class="position">Marketing Manager</span>
								</div>
							</div>
						</div>
						<div class="item">
							<div class="testimony-wrap p-4 pb-5">
								<div class="user-img mb-5" style="background-image: url(images/person_2.jpg)">
									<span class="quote d-flex align-items-center justify-content-center">
										<i class="icon-quote-left"></i>
									</span>
								</div>
								<div class="text text-center">
									<p class="mb-5 pl-4 line">best service,the watch so beautiful.</p>
									<p class="name">Garreth Smith</p>
									<span class="position">Interface Designer</span>
								</div>
							</div>
						</div>
						<div class="item">
							<div class="testimony-wrap p-4 pb-5">
								<div class="user-img mb-5" style="background-image: url(images/person_3.jpg)">
									<span class="quote d-flex align-items-center justify-content-center">
										<i class="icon-quote-left"></i>
									</span>
								</div>
								<div class="text text-center">
									<p class="mb-5 pl-4 line">best service,the watch so beautiful.</p>
									<p class="name">Garreth Smith</p>
									<span class="position">UI Designer</span>
								</div>
							</div>
						</div>
						<div class="item">
							<div class="testimony-wrap p-4 pb-5">
								<div class="user-img mb-5" style="background-image: url(images/person_1.jpg)">
									<span class="quote d-flex align-items-center justify-content-center">
										<i class="icon-quote-left"></i>
									</span>
								</div>
								<div class="text text-center">
									<p class="mb-5 pl-4 line">best service,the watch so beautiful.</p>
									<p class="name">Garreth Smith</p>
									<span class="position">Web Developer</span>
								</div>
							</div>
						</div>
						<div class="item">
							<div class="testimony-wrap p-4 pb-5">
								<div class="user-img mb-5" style="background-image: url(images/person_1.jpg)">
									<span class="quote d-flex align-items-center justify-content-center">
										<i class="icon-quote-left"></i>
									</span>
								</div>
								<div class="text text-center">
									<p class="mb-5 pl-4 line">best service,the watch so beautiful.</p>
									<p class="name">Garreth Smith</p>
									<span class="position">System Analyst</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<hr>



	<!-- <footer class="ftco-footer" style="background-color: #ffad33;">
		<div class="container" style="height: 180px;">

			<div class="row" style="height: 100%">

				<div class="col-md-4" style="height: 100%;">
					<div class="ftco-footer-widget ml-md-5">
						<h2 class="ftco-heading-2 mt-2">Follow us</h2>
						<ul class="list-unstyled">
							<li><a href="#" class="pb-2 d-block"><span class="facebook"><i
											class="fa-brands fa-facebook"></i></span> facebook</a></li>
							<li><a href="#" class="pb-2 d-block"><span class="ins"><i
											class="fa-brands fa-instagram"></i></span> instagram</a></li>
							<li><a href="#" class="pb-2 d-block"><span class="twitter"><i
											class="fa-brands fa-twitter"></i></span> twitter</a></li>

						</ul>
					</div>
				</div>
				<div class="col-md-4" style="height: 100%;">
					<div class="ftco-footer-widget">
						<h2 class="ftco-heading-2 mt-2">Help</h2>
							<ul class="list-unstyled mr-l-5 pr-l-3 mr-4">
								<li><a href="#" class="pb-2 d-block">Shipping Information</a></li>
								<li><a href="#" class="pb-2 d-block">FAQs</a></li>
								<li><a href="#" class="pb-2 d-block">Terms &amp; Conditions</a></li>
								<li><a href="#" class="pb-2 d-block">Privacy Policy</a></li>
							</ul>
					</div>
				</div>
				<div class="col-md-4" style="height: 100%;">
					<div class="ftco-footer-widget">
						<h2 class="ftco-heading-2 mt-2">Have a Questions?</h2>
						<div class="block-23 mb-3">
							<ul>
								<li class="mb-3 mt-3"><span class="icon icon-map-marker" style="color: #000;"></span><span class="text" style="color: #000;">203 Fake St. Mountain
										View, San Francisco, California, USA</span></li>
								<li><a href="#"><span class="icon icon-phone"></span><span class="text">+84
											0761234567</span></a></li>
								<li><a href="#"><span class="icon icon-envelope"></span><span
											class="text">bkmtwatch@gmail.com</span></a></li>
							</ul>
						</div>
					</div>
				</div>
			</div>
	</footer> -->

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
	<script src="js/sweetalert.all.min.js"></script>
	<script src="js/main.js"></script>
	<script src="js/cart.js"></script>
</body>

</html>
