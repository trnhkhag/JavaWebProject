<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
		<div class="container">
			<a class="navbar-brand" href="index.html">BKMT WATCH</a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav"
				aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
				<span class="oi oi-menu"></span> Menu
			</button>

			<div class="collapse navbar-collapse" id="ftco-nav">
				<ul class="navbar-nav ml-auto">
					<li class="nav-item active"><a href="Home" class="nav-link">Home</a></li>
					<li class="nav-item dropdown">
						<a class="nav-link dropdown-toggle" href="shop.html" id="dropdown04" data-toggle="dropdown"
							aria-haspopup="true" aria-expanded="false">Category</a>
						<div class="dropdown-menu" aria-labelledby="dropdown04">
							<a class="dropdown-item" href="Shop?cid=1&page=1">Men's Watches</a>
							<a class="dropdown-item" href="Shop?cid=2&page=1">Women's Watches</a>
							<a class="dropdown-item" href="Shop?cid=3&page=1">Couple's Watches</a>
							<a class="dropdown-item" href="Shop?cid=4&page=1">Unisex Watches</a>
						</div>
					</li>
					<li class="nav-item"><a href="about.html" class="nav-link">About</a></li>
					<li class="nav-item"><a href="contact.html" class="nav-link">Contact</a></li>
				</ul>

			</div>

			<div id="right">
				<form class="example" action="Shop" name="search-product" method="get">
					<input type="text" placeholder="Search.." name="search-input">
					<button type="submit" style="background-color: #ffad33;"><i class="fa fa-search"></i></button>
				  </form>
			</div>

			<div class="collapse navbar-collapse ftco-nav-right" id="ftco-nav">
				<ul class="navbar-nav ml-auto">
					<li class="nav-item"><a href="Cart" class="nav-link"><i
								class="fa-solid fa-cart-shopping"></i></a></li>
					<li class="nav-item"><a href="wishlist.html" class="nav-link"><i
								class="fa-solid fa-heart"></i></a></li>
					<c:if test="${sessionScope.user == null}">
						<li class="nav-item"><a href="${pageContext.request.contextPath}/Login" class="nav-link"><i
								class="fa-solid fa-user"></i></a></li>
					</c:if>
					<c:if test="${sessionScope.user != null}">
						<li class="nav-item"><a href="${pageContext.request.contextPath}/Logout" class="nav-link"><i class="fa-solid fa-right-from-bracket"></i></a></li>
					</c:if>
				</ul>
			</div>
		</div>
	</nav>