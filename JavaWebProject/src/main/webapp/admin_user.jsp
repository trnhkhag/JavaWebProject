<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BKMT WATCH | Admin - User</title>
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
        <a href="AdminProduct">
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
        <a href="#" class="active">
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
        <span class="dashboard">User</span>
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

    <div class="home-content user">
      <div class="header">
        <div class="nav">
          <div class="search-box">
            <input type="text" placeholder="Search user">
            <i class='bx bx-search'></i>
          </div>
          <div class="action">
            <div class="add-user btn" onclick="addUser()">
              <i class="bx bx-plus"></i>
            </div>
            <div class="filter-list btn">
              <i class="bx bx-filter"></i>
            </div>
          </div>
        </div>

        <div class="filter">
          <div class="option">
            <p class="title">Role</p>
            <div class="option-list user-manage">
              <form action="" class="crole">
                <select name="role">
                  <option value="all">All</option>
                  <option value="customer">Customer</option>
                  <option value="loyalcustomer">Loyal customer</option>
                </select>
              </form>
            </div>
          </div>
          <div class="option">
            <p class="title">Registration Date</p>
            <div class="option-list">
              <form action="">
                <input type="date" name="regisdate">
              </form>
            </div>
          </div>
          <div class="option">
            <p class="title">Status</p>
            <div class="option-list">
              <form action="">
                <select name="status">
                  <option value="all">All</option>
                  <option value="online">Online</option>
                  <option value="offline">Offline</option>
                </select>
              </form>
            </div>
          </div>
          <div class="option">
            <p class="title">Sort</p>
            <div class="option-list">
              <div class="sort">
                <button id="byname"><i class="fa-solid fa-arrow-up"></i> By name</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="box user-list">
        <table>
          <thead>
            <tr>
              <th class="text-left">User</th>
              <th class="text-left">Fullname</th>
              <th class="text-left">Phone Number</th>
              <th>Address</th>
              <th>Role</th>
            </tr>
          </thead>
          <tbody>
          	<c:forEach items="${ulist}" var="u">
          		<tr>
              <td class="text-left">
                <p>${u.username}</p>
                <p class="email">${u.email}</p>
              </td>
              <td class="text-left">${u.fullname}</td>
              <td class="text-left">${u.phone}</td>
              <td>${u.address}</td>
              <td>${u.role}</td>
              <td>
                <i class='bx bxs-edit-alt' onclick="editUser(${u.id})">
                  <span class="tooltip">Edit</span>
                </i>
                <i class="bx bxs-user-x" onclick="banUser(${u.id})">
                  <span class="tooltip">Ban</span>
                </i>
              </td>
            </tr>
          	</c:forEach>
          </tbody>
        </table>
      </div>
    </div>
    <!-- <div class="footer">
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

  <div class="modal user-form">
    <form action="" class="modal-content animate" name="manage-user-form" method="post">
      <div class="header">
        <h2>Customer Information</h2>
      </div>
      <div class="container">
      	<input type="hidden" name="uid" value="">
        <label for="uname">Name</label>
        <input type="text" name="uname" value="">
        <label for="upass">Password</label>
        <input type="password" name="upass" value="">
        <label for="uemail">Email</label>
        <input type="text" name="uemail" value="">
        <label for="uphone">Phone number</label>
        <input type="text" name="uphone" value="">
        <label for="urole">Role</label>
        <select name="urole">
          <option value="Customer">Customer</option>
          <option value="Admin">Admin</option>
        </select>
      </div>
      <hr>
      <div class="footer">
        <button type="button" class="cancel">Cancel</button>
        <button type="submit" class="done">Done</button>
      </div>
    </form>
  </div>
  <script src="js/jquery-3.2.1.min.js"></script>
  <script src="js/admin_user.js"></script>
  <script>
    // expand and shrink sidebar
    let sidebar = document.querySelector(".sidebar");
    let sidebarBtn = document.querySelector(".sidebarBtn");
    sidebarBtn.onclick = function () {
      sidebar.classList.toggle("active");
      if (sidebar.classList.contains("active")) {
        sidebarBtn.classList.replace("bx-menu", "bx-menu-alt-right");
      } else
        sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
    }

    // open and close filter list
    let filterBtn = document.querySelector(".filter-list");
    let header = document.querySelector('.header');
    filterBtn.addEventListener('click', () => {
      header.classList.toggle('active');
    })

    // increase and decrease according to time
    let sortByTimeBtn = document.querySelector('#byname');
    sortByTimeBtn.addEventListener('click', () => {
      sortByTime = sortByTimeBtn.firstChild;
      if (sortByTime.classList.contains('fa-arrow-up')) {
        sortByTime.classList.replace('fa-arrow-up', 'fa-arrow-down');
      }
      else {
        sortByTime.classList.replace('fa-arrow-down', 'fa-arrow-up');
      }
    })

    //control user form
  </script>
</body>

</html>