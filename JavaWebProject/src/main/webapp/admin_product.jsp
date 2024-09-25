<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BKMT WATCH | Admin - Product</title>
  <link rel="stylesheet" href="fontawesome-free-6.2.0-web/css/all.min.css">
  <link href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' rel='stylesheet'>
  <link rel="stylesheet" href="css/admin_style.css">
</head>

<body>
  <div class="sidebar">
    <div class="logo-details">
      <i class='bx bx-alarm'></i>
      <span class="logo_name">BKMT WATCH</span>
    </div>
    <ul class="nav-links">
      <li>
        <a href="admin_index.html">
          <i class='bx bx-grid-alt'></i>
          <span class="links_name">Dashboard</span>
        </a>
      </li>
      <li>
        <a href="#" class="active">
          <i class='bx bx-box'></i>
          <span class="links_name">Product</span>
        </a>
      </li>
      <li>
        <a href="AdminOrder">
          <i class='bx bx-list-ul'></i>
          <span class="links_name">Order list</span>
        </a>
      </li>
      <li>
        <a href="AdminUser">
          <i class='bx bx-user'></i>
          <span class="links_name">User</span>
        </a>
      </li>
      <li class="log_out">
        <a href="Logout">
          <i class='bx bx-log-out'></i>
          <span class="links_name">Log out</span>
        </a>
      </li>
    </ul>
  </div>
  <section class="home-section">
    <nav>
      <div class="sidebar-button">
        <i class='bx bx-menu sidebarBtn'></i>
        <span class="dashboard">Product</span>
      </div>
      <!-- <div class="search-box">
        <input type="text" placeholder="Search...">
        <i class='bx bx-search'></i>
      </div> -->
      <div class="profile-details">
        <img src="images/profile.jpg" alt="">
        <span class="admin_name">Admin</span>
        <i class='bx bx-chevron-down'></i>
      </div>
    </nav>

    <div class="home-content product">
      <div class="header">
        <div class="nav">
          <div class="search-box">
            <input type="text" placeholder="Search product">
            <i class='bx bx-search'></i>
          </div>
          <div class="action">
            <div class="add-order btn" onclick="addProduct()">
              <i class="bx bx-plus"></i>
            </div>
          </div>
        </div>
      </div>

      <div class="box product-list">
        <table>
          <thead>
            <tr>
              <th class="product-name text-left">Name</th>
              <th>Category</th>
              <th>Stock</th>
              <th>Status</th>
              <th>Price</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
          	<c:forEach items="${plist}" var="p">
          		<tr>
              		<td class="text-left">${p.name}</td>
              		<td>${p.category}</td>
              		<td>${p.stock}</td>
              		<td>
              			<c:choose>
							<c:when test="${p.status == 1}">
							<span class="status-paid">On sale</span>
							</c:when>
							<c:otherwise>
							<span class="status-unpaid">Out of stock</span>
							</c:otherwise>              			
              			</c:choose>
              		</td>
              		<td>${p.price}$</td>
              		<td>
                		<i class='bx bxs-detail' onclick="productDetail(${p.id})">
                  		<span class="tooltip">detail</span>
                		</i>
                		<i class='bx bxs-edit-alt' onclick="productEdit(${p.id})">
                  		<span class="tooltip">edit</span>
                		</i>
                		<i class='bx bxs-trash' onclick="productDelete(${p.id})">
                  		<span class="tooltip">delete</span>
                		</i>
              		</td>
            	</tr>
          	</c:forEach>
          </tbody>
        </table>
      </div>
     <!--  <div class="footer">
        <div class="page">
          <button><i class='bx bx-left-arrow-alt'></i></button>
          <button class="current-page">1</button>
          <button>2</button>
          <button>3</button>
          <button>4</button>
          <button>5</button>
          <button><i class='bx bx-right-arrow-alt'></i></button>
        </div>
      </div> -->
  </section>

  <div class="modal product-form">
    <form action="" class="modal-content animate" method="post" enctype="multipart/form-data" name="manage-product-form" id="product-form">
      <div class="header">
        <h2>Product Information</h2>
      </div>
      <div class="container">
      	<input name="pid" type="hidden" value="">
        <label for="pname">Name</label>
        <input type="text" name="pname">
        <label for="pcategory">Category</label>
        <select name="pcategory" value="">
        	<c:forEach items="${clist}" var="c">
        		<option value="${c.id}">${c.name}</option>
        	</c:forEach>
        </select>
        <label for="pstock">Stock</label>
        <input type="number" name="pstock" value="">
        <label for="pstatus">Status</label>
        <select name="pstatus">
        	<option value="1">On sale</option>
        	<option value="0">Out of stock</option>
        </select>
        <label for="pprice">Price</label>
        <input type="text" name="pprice" value="">
        <label for="pbrand">Brand</label>
        <input type="text" name="pbrand" value="">
        <label for="pdesc">Description</label>
        <textarea name="pdesc" cols="30" rows="3"></textarea>
        <label for="pimage">Image</label>
        <input type="file" name="pimage">
      </div>
      <hr>
      <div class="footer">
        <button type="button" class="cancel">Cancel</button>
        <button type="submit" form="product-form" class="done">Done</button>
      </div>
    </form>
  </div>

  <div class="modal product-detail">
    <div class="container animate">
      <div class="product-img" style="background-image:url(images/product_8.jpg);"></div>
      <h4>Description</h4>
      <p>Far far away, behind the word mountains, far from the countries</p>
      <div class="footer"><button type="button" class="close">Close</button></div>
    </div>
  </div>

  <div class="modal product-delete">
    <div class="container animate">
      <h2>Are you sure you want to<br>
        delete this product?</h2>
      <div class="action">
      <form action="StopSelling" name="delete-confirm-form">
      	<input name="pid" type="hidden" value="">
      	<button type="submit" class="confirm">Confirm</button>
        <button type="button" class="cancel-deletion">Cancel</button>
      </form>
      </div>
    </div>
  </div>

  <script src="js/jquery-3.2.1.min.js"></script>
  <script src="js/admin_product.js"></script>
</body>

</html>