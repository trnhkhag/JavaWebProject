<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
	<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
		<!DOCTYPE html>
		<html lang="en">

		<head>
			<title>BKMT WATCH | Shop</title>
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
			<script src="js/cart.js"></script>
		</head>

		<body class="goto-here">
			<jsp:include page="header.jsp"></jsp:include>
			<!-- END nav -->

			<div class="hero-wrap hero-bread" style="background-image: url('images/bg_1.jpeg');">
				<div class="container">
					<div class="row no-gutters slider-text align-items-center justify-content-center">
						<div class="col-md-9 ftco-animate text-center">
							<p class="breadcrumbs">
								<span class="mr-2"><a href="Home">Home</a></span> <span>Products</span>
							</p>
							<h1 class="mb-0 bread">Products</h1>
						</div>
					</div>
				</div>
			</div>

			<section class="ftco-section">
				<div class="container">
					<div class="row justify-content-center">
						<div class="col-md-10 mb-2 text-center">
							<ul class="product-category">
								<li><a href="Shop?page=1" class="active">All</a></li>
								<li><a href="Shop?cid=1&page=1" class="active">Men's Watches</a></li>
								<li><a href="Shop?cid=2&page=1" class="active">Women's Watches</a></li>
								<li><a href="Shop?cid=3&page=1" class="active">Couple's Watches</a></li>
								<li><a href="Shop?cid=4" class="active">Unisex Watches</a></li>
							</ul>
						</div>
					</div>
					<div class="filter-container">
						<form action="Shop" name="filter-form" method="get">
							<div style="display: flex; justify-content: center;">
								<div style="margin: 0 30px">
									<h4>Category</h4>
									<c:forEach items="${clist}" var="c">
										<input type="checkbox" id="category${c.id}" name="category${c.id}" value="${c.id}">
										<label for="category${c.id}">${c.name}</label><br>
									</c:forEach>
								</div>
								<div style="margin: 0 30px">
									<h4>Brand</h4>
									<c:forEach items="${blist}" var="b">
										<input type="checkbox" id="${b}" name="${b}" value="${b}">
										<label for="${b}">${b}</label><br>
									</c:forEach>
								</div>
								<div style="margin: 0 30px">
									<h4>Price range</h4>
									<label for="min-price">Min price</label><br>
									<input type="number" name="minPrice" value="0"><br>
									<label for="max-price">Max price</label><br>
									<input type="number" name="maxPrice" value="0"><br>
								</div>
							</div>
							<div style="display: flex; flex-direction: row-reverse; justify-content: center; margin: 20px 0">
								<input type="submit" name="filterSubmit" value="submit">
							</div>
						</form>
					</div>
					<div class="row">
						<c:forEach items="${plist}" var="p">
							<div class="col-md-6 col-lg-3 ftco-animate">
								<div class="product">
									<a href="${pageContext.request.contextPath}/ProductDetail?pid=${p.id}" class="img-prod"><img
											class="img-fluid" src="${p.image}" alt="Colorlib Template">
										<div class="overlay"></div>
									</a>
									<div class="text py-3 pb-4 px-3 text-center">
										<h3>
											<a href="${pageContext.request.contextPath}/ProductDetail?pid=${p.id}">${p.name}</a>
										</h3>
										<div class="d-flex">
											<div class="pricing">
												<p class="price">
													<span class="mr-2 price-dc">$35000.00</span><span class="price-sale">$${p.price}</span>
												</p>
											</div>
										</div>
										<div class="bottom-area d-flex px-3">
											<div class="m-auto d-flex">
												<a href="${pageContext.request.contextPath}/ProductDetail?pid=${p.id}"
													class="add-to-cart d-flex justify-content-center align-items-center text-center">
													<span><i class="ion-ios-menu"></i></span>
												</a> <a href="#" class="buy-now d-flex justify-content-center align-items-center mx-1" onclick="event.preventDefault(); addToCart(${p.id}, ${p.quantity})">
													<span><i class="ion-ios-cart btn-buynow"></i></span>
												</a> <a href="#" class="heart d-flex justify-content-center align-items-center ">
													<span><i class="ion-ios-heart"></i></span>
												</a>
											</div>
										</div>
									</div>
								</div>
							</div>
						</c:forEach>
					</div>
					<div class="row mt-5">
						<div class="col text-center">
							<div class="block-27">
								<ul>
									<c:forEach begin="1" end="${numPage}" var="i">
										<c:choose>
											<c:when test="${curPage eq i}">
												<li class="active"><a href="#">${i}</a></li>
											</c:when>
											<c:otherwise>
												<li><a href="Shop?page=${i}">${i}</a></li>
											</c:otherwise>
										</c:choose>
									</c:forEach>
									<!-- <li><a href="#">&lt;</a></li>
							<li class="active"><span>1</span></li>
							<li><a href="#">2</a></li>
							<li><a href="#">3</a></li>
							<li><a href="#">4</a></li>
							<li><a href="#">5</a></li>
							<li><a href="#">&gt;</a></li> -->
								</ul>
							</div>
						</div>
					</div>
				</div>
			</section>

			<footer>
				<div class="Our_social_media">
					<a href="#"><i class="fa-brands fa-facebook"></i></a> <a href="#"><i class="fa-brands fa-instagram"></i></a>
					<a href="#"><i class="fa-brands fa-twitter"></i></a> <a href="#"><i class="fa-brands fa-youtube"></i></a>
				</div>
				<div class="more_info">
					<a href="#">Contact us</a> <a href="#">Our Services</a> <a href="#">Privacy
						Policy</a> <a href="#">Terms & Conditions</a> <a href="#">Career</a>
				</div>
				<p>INFERNO Copyright Â© 2021 Inferno - All rights reserved ||
					Designed By: Mahesh</p>
			</footer>


			<!-- loader -->
			<div id="ftco-loader" class="show fullscreen">
				<svg class="circular" width="48px" height="48px">
					<circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee" />
					<circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10"
						stroke="#F96D00" />
				</svg>
			</div>
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
		</body>

		</html>