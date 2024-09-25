<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="en">

<head>
	<title>BKMT WATCH | Product</title>
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

	<div class="hero-wrap hero-bread" style="background-image: url('images/bg_1.jpeg');">
		<div class="container">
			<div class="row no-gutters slider-text align-items-center justify-content-center">
				<div class="col-md-9 ftco-animate text-center">
					<p class="breadcrumbs"><span class="mr-2"><a href="index.html">Home</a></span> </p>
					<h1 class="mb-0 bread">Order History</h1>
				</div>
			</div>
		</div>
	</div>
    <section>
        <div class="bodyhis">
            <div class="infohis">
                <img class="imginfohis" src="images/ava_info.jpg"  alt="">
                <div class="headinfohis">
                    <div class="nameinfo">${currentUser.fullname}<br> SĐT: ${currentUser.phone}</div>
                    <div><a class="_78QHr1" href=""><svg width="12" height="12" viewBox="0 0 12 12"
                                xmlns="http://www.w3.org/2000/svg" style="margin-right: 4px;">
                                </svg></a></div>
                </div>
            </div>
            <!-- <div class="headtext">
                Đơn hàng của tôi
            </div>
            <div class="searchhis">
                <div class="ishis"><i class="fa-solid fa-magnifying-glass"></i></div>
                <input type="search" placeholder=" Tìm kiếm theo Tên Sản phẩm, Giá Tiền" class="searchhis-a ">
            </div> -->


            <div class="containerhis">
                <div>
                <c:forEach items="${olist}" var="o">
                	<div class="order-list">  
                    <h2>My Order (Date: ${o.date})</h2>
                    <h2>Status: ${o.status}</h2>                  
                        <div class="orders">
                            <div tag="order-component">
                                <div class="shop shop-cursor">                                
                                    <div class="shop-body">                                    
                                        <c:forEach items="${odlist}" var="od">
                                        	<c:if test="${o.id == od.orderId}">
                                        		<div class="order-item">                                        
                                            <div class="item-pic" data-spm="detail_image"><a href="#"><img
                                                        src="${od.product.image}"></a>
                                            </div>
                                            <div class="item-main item-main-mini">
                                                <div>
                                                    <div class="headtexthis"><span class="spanhis">Product name:</span>
                                                        ${od.product.name}</div>
                                                    <div class="text title item-title"><span class="spanhis">Description: 
                                                            </span>${od.product.desc}</div>
                                                    <div class="numproduct"><span class="spanhis">Quantity: </span>${od.quantity}</div>
                                                    <div class="item-sku"></div>
                                                    <p class="text desc"></p>
                                                    <p class="text desc bold"></p>
                                                </div>
                                            </div>
                                            <div class="item-status">
                                                <div class="item-price text bold">${od.price}$</div>
                                            </div>
                                            <div class="clear"></div>
                                        </div>
                                        	</c:if>
                                        </c:forEach>
                                    </div>
                                </div>
                            </div>
                            <div class="foothis">
                                <div class="tthis">
                                    <div class="totalhis">Total:</div>
                                    <div class="mnhis">${o.total}$</div>
                                </div>
                                <div class="buyhis">
                                    <div class="evaluatehis"><button class="stardust-button--primary btnhis">Rating</button>
                                    </div>
                                    <div class="reorderhis"><button class=" stardust-button--secondary btnhis">Buy more</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </c:forEach>
                </div>
                
            </div>
            
        </div>
    </section>
	
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
		<p>INFERNO Copyright © 2021 Inferno - All rights reserved || Designed By: Mahesh</p>
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


</body>

</html>
