<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<html>

<head>
    <title>BKMT Watch | Sign Up</title>
    <!--Made with love by Mutiullah Samim -->
    <!--Reference source at https://bootsnipp.com/snippets/vl4R7-->
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">

    <!--Bootsrap 4 CDN-->
    <!-- <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
        integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"> -->

    <!--Fontawesome CDN-->
    <!-- <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css"
        integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous"> -->

    <!--Custom styles-->
    <link rel="stylesheet" type="text/css" href="login_register_css/register.css">
    <style>
    	.card {
    		margin-top: auto;
    		margin-bottom: auto;
    		width: auto;
    		background-color: rgba(0,0,0,0.5) !important;
    	}
    </style>
</head>

<body>
    <div class="container">
        <div class="d-flex justify-content-center h-100">
            <div class="card">
                <div class="card-header">
                    <h3>Please Enter Your Email</h3>
                </div>
                <div class="card-body">
                    <p class="text-danger">${errorString}</p>
                    <form action="Forgotpassword" method="post" name="email_form" onsubmit="return validateEmail()" >
                        <div class="input-group form-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"><i class="fas fa-phone"></i></span>
                            </div>
                            <input type="text" class="form-control" placeholder="example@email.com" id="email" name="email">
                        </div>
                        <div class="form-group action">
                            <input type="reset" value="Reset" class="btn login_btn">
                            <input type="submit" value="Register" class="btn float-right register_btn" id="submit">
                        </div>
                    </form>
                </div>
                <div class="card-footer">
                    <div class="d-flex justify-content-center links">
                        Already have an account?<a href="${pageContext.request.contextPath}/Login">Sign In</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
	<script src="js/sweetalert.all.min.js"></script>
    <script src="js/forgotpassword.js"></script>

</body>

</html>