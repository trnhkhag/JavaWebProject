<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BKMT WATCH | Admin - Order_List</title>
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
        <a href="#" class="active">
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
        <span class="dashboard">Order list</span>
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

    <div class="home-content">
      <div class="header">
        <div class="nav">
        <form action="searchcontrol?search=name" method="post">
          <div class="search-box">
            <input type="text" name="searchbyname" placeholder="Search order">
             <button type="submit" name="submit"><i class='bx bx-search '></i>
             </button>
          </div>
          </form>
          <div class="action">
            <div class="add-order btn">
              <i class="bx bx-plus"></i>
            </div>
            <div class="filter-list btn">
              <i class="bx bx-filter"></i>
            </div>
          </div>
        </div>

        <div class="filter">
          <div class="option">
            <p class="title">Time & Date</p>
            <div class="option-list">
              <!-- <form action="" class="time">
                <label for="time">Time</label>
                <select name="time" id="time">
                  <option value="24h">Last 24 hours</option>
                  <option value="week">Last week</option>
                  <option value="month">Last month</option>
                </select>
              </form> -->
              <form action="searchcontrol?search=date" method="post" class="date">
                <label for="date">Date</label>
                  <div style="padding-top: 5px;">
                <input type="date" id="date" name="date" style="margin-left:20px">
                </div>
                <input style="background-color:yellow;margin-top:10px;" type="submit" name="submit">    
              </form>
            </div>
          </div>
          <div class="option">
            <p class="title">Price range</p>
            <div class="option-list">
              <form action="searchcontrol?search=price" method="post" class="price-range">
                <div style="padding-bottom: 5px;">
                  <label for="from">From</label>
                  <input type="text" id="from" name="from" placeholder=" 0$">
                </div>
                <div style="padding-top: 5px;">
                  <label for="to">To</label>
                  <input type="text" id="to" name="to" placeholder=" 1000$">
                </div>
                 <input style="margin:10px 48px;width:65px;background-color:yellow" type="submit" name="submit">    
              </form>
            </div>
          </div>
          <div class="option">
            <p class="title">Status</p>
            <div class="option-list">
              <form action="searchcontrol?search=datiepnhan" method="post" class="status">
								<select id="status" name="stt">
									<option value="Đã Tiếp Nhận">Đã Tiếp Nhận</option>
									<option value="Đang Giao">Đang Giao</option>
									<option value="Hoàn Thành">Hoàn Thành</option>
								</select>
                 <input style="margin:10px 48px;width:65px;background-color:yellow" type="submit" name="submit">    
				</form>
              
            </div>
          </div>
          <div class="option">
            <p class="title">Sort</p>
            <div class="option-list">
              <div class="sort">
                <button id="bytime"><i class="fa-solid fa-arrow-up"></i> By time</button>
              </div>
              <div class="sort">
                <button id="byprice"><i class="fa-solid fa-arrow-up"></i> By price</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="order-list">
        <table>
          <thead>
            <tr>              
            	<th >ID</th>
      
              <th>Customer</th>
              <th>Phone Number</th>
              <th>Total</th>
              <th>Date</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
          </thead>
          
          <c:forEach items="${in4}" var="o">          
          <tbody>
        						<td><span  >${o.madh}</span></td>								            
								<td>${o.hoten}</td>
								<td>${o.phone}</td>
								<td>${o.total}</td>
								<td>${o.date}</td>
   							<td><span name="stt1" <c:if test="${o.status=='Đang Giao'}">style="background-color: yellow;</c:if>
   							<c:if test="${o.status=='Đã Tiếp Nhận'}">style="background-color: red; color:white"</c:if>
   							<c:if test="${o.status=='Hoàn Thành'}">style="background-color: green; color:white"
   							</c:if> style="height:50px">${o.status}</span></td>								
								
								</span></td>
              <td>
                <form action="ProcessControl" method="post">
                <input type="hidden" name="madh" value="${o.madh}">
                <select name="status" style=" height:30px;border-radius:5px"> 
                    <option value="1">Đã Tiếp Nhận</option>
                    <option value="2">Đang Giao </option>
                    <option value="3">Hoàn Thành</option>   
                </select>
                   
                <button type="submit" ><i class='bx bxs-edit-alt'>
                  <span class="tooltip">Edit</span>
                	</i></button>
                <a href="OrderDetail?id=${o.madh}"><i class='bx bxs-detail'></i></a>
                    <span class="tooltip">Details</span>
            </form>
              </td>
            </tr>	
          </tbody>
          </c:forEach>
        </table>
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
    </div>
  </section>

<!--   <div class="modal order-form">
    <form action="ProcessControl" class="modal-content animate">
      <div class="header">
        <h2>XÁC NHẬN</h2>
      </div>
      <div class="container">
        <label for="status">Status</label>
                       
        <select name="status">
          <option value="1" name="1">Đã Tiếp Nhận</option>
          <option value="2" name="2">Đang Giao</option>
          <option value="3" name="3">Hoàn Thành</option>   
        </select>
      </div>
      <hr>
      <div class="footer">
        <button type="button" class="cancel">Cancel</button>
        <button type="submit" class="done">Done</button>
      </div>
    </form>
  </div> -->

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
    let sortByTimeBtn = document.querySelector('#bytime');
    sortByTimeBtn.addEventListener('click', () => {
      sortByTime = sortByTimeBtn.firstChild;
      if (sortByTime.classList.contains('fa-arrow-up')) {
        sortByTime.classList.replace('fa-arrow-up', 'fa-arrow-down');
      }
      else {
        sortByTime.classList.replace('fa-arrow-down', 'fa-arrow-up');
      }
    })

    // increase and decrease according to price
    let sortByPriceBtn = document.querySelector('#byprice');
    sortByPriceBtn.addEventListener('click', () => {
      sortByPrice = sortByPriceBtn.firstChild;
      if (sortByPrice.classList.contains('fa-arrow-up')) {
        sortByPrice.classList.replace('fa-arrow-up', 'fa-arrow-down');
      }
      else {
        sortByPrice.classList.replace('fa-arrow-down', 'fa-arrow-up');
      }
    })

    // control order form
    let orderForm= document.querySelector('.order-form');
    let editBtn = document.getElementsByClassName('bxs-edit-alt');
    let addBtn = document.querySelector('.add-order');
    for (let i = 0; i < editBtn.length; i++) {
      editBtn[i].addEventListener('click', () => {
        orderForm.style.display = 'flex';
      });
    }
    addBtn.addEventListener('click', () => {
      orderForm.style.display = 'flex';
    });
    let cancelBtn = document.querySelector('.cancel');
    cancelBtn.addEventListener('click', () => {
      orderForm.style.display = 'none';
    })
    window.onclick = (event) => {
      if (event.target == orderForm) {
        orderForm.style.display = 'none';
      }
    }
  </script>
</body>

</html>