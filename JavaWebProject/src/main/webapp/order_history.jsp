<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BKMT WATCH | Admin - Order_detail</title>
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
        <a href="admin_product.html">
          <i class='bx bx-box'></i>
          <span class="links_name">Product</span>
        </a>
      </li>
      <li>
        <a href="#" class="active">
          <i class='bx bx-list-ul'></i>
          <span class="links_name">Order list</span>
        </a>
      </li>
      <li>
        <a href="#">
          <i class='bx bx-pie-chart-alt-2'></i>
          <span class="links_name">Analytics</span>
        </a>
      </li>
      <li>
        <a href="admin_user.html">
          <i class='bx bx-user'></i>
          <span class="links_name">User</span>
        </a>
      </li>
      <li class="log_out">
        <a href="#">
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
        <span class="dashboard">Order detail</span>
      </div>
      <div class="profile-details">
        <img src="images/profile.jpg" alt="">
        <span class="admin_name">Admin</span>
        <i class='bx bx-chevron-down'></i>
      </div>
    </nav>

    <div class="home-content order-detail">
      <div class="header">
        <div class="nav">
          <div class="search-box">
            <input type="text" placeholder="Search ...">
            <i class='bx bx-search'></i>
          </div>
          <div class="action">
            <div class="btn">
              <i class="bx bx-edit"></i>
            </div>
            <div class="btn">
              <i class="bx bx-exit"></i>
            </div>
          </div>
        </div>
      </div>

      <div class="info" item="${in4}" var="o" >
        <div class="box order-info">
          <table>
            <caption>Order Infomation</caption>
            <tbody>
              <tr>
                <th>Order's ID</th>
                <td>${o.madh }</td>
              </tr>
              <tr>
                <th>Date</th>
                <td>${o.date }</td>
              </tr>
              <tr>
                <th>Total</th>
                <td>${o.total }</td>
              </tr>
              <tr>
                <th>Status</th>
                <td><span class="status-paid">${o.status}</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="box customer-info">
          <table>
            <caption>Customer Infomation</caption>
            <tbody>
              <tr>
                <th>Name</th>
                <td>Pham Hoang Bach</td>
              </tr>
              <tr>
                <th>Phone Number</th>
                <td>0123456789</td>
              </tr>
              <tr>
                <th>Address</th>
                <td>123 An Duong Vuong, P.5, Q.5, TPHCM</td>
              </tr>
              <tr>
                <th>Email</th>
                <td><a href="#">bach@gmail.com</a></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="box product-list">
        <table>
          <caption>Product List</caption>
          <thead>
            <tr>
              <th></th>
              <th>Description</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
          <c:for>
            <tr>
              <td>
                <div class="product-img" style="background-image:url(images/product_8.jpg);"></div>
              </td>
              <td>
                <h4>Submariner</h4>
                <p>Far far away, behind the word mountains, far from the countries</p>
              </td>
              <td>50$</td>
              <td>1</td>
              <td>50$</td>
            </tr>
    	</c:for>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</body>

</html>