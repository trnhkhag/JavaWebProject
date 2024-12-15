<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<html lang="en">

<head>
	<title>BKMT Watch | Sign in</title>

	<!--Custom styles-->
	<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
	<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
	<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<link rel="stylesheet" type="text/css" href="login_register_css/login.css">
	<script src="js/sweetalert.all.min.js"></script>
	<script src="js/login_validation.js"></script>
</head>

<body>
	<div class="container">
		<div class="d-flex justify-content-center h-100">
			<div class="card">
				<div class="card-header">
					<h3>Sign In</h3>
					<div class="d-flex justify-content-end social_icon">
						<span><i class="fab fa-facebook-square"></i></span> <span><i class="fab fa-google-plus-square"></i></span>
						<span><i class="fab fa-twitter-square"></i></span>
					</div>
				</div>
				<div class="card-body">
					<p class="text-danger">${errorString}</p>
					<form method="POST" action="Login" onsubmit="return validate()" name="login">

						<div class="input-group form-group">
							<div class="input-group-prepend">
								<span class="input-group-text"><i class="fas fa-user"></i></span>
							</div>
							<input id="username" type="text" class="form-control" placeholder="Enter Username" name="username">
						</div>

						<div class="input-group form-group">
							<div class="input-group-prepend">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
							<input id="password" type="password" class="form-control" placeholder="Enter Password" name="password">
						</div>

						<div class="row align-items-center remember">
							<input type="checkbox" id="remember"> <label for="remember"> Remember Me</label>
						</div>

						<div class="action">
							<button type="button" value="Cancel" onclick="window.location.assign('Home');"
								class="btn float-right login_btn">Cancel</button>
							<button type="submit" value="Login" class="btn float-right login_btn">Login</button>
						</div>

					</form>
				</div>
				<div class="card-footer">
					<div class="d-flex justify-content-center links">
						Don't have an account?<a href="${pageContext.request.contextPath}/Register">Sign Up</a>
					</div>
					<div class="d-flex justify-content-center">
						<a href="${pageContext.request.contextPath}/Forgotpassword">Forgot your password?</a>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>

</html>