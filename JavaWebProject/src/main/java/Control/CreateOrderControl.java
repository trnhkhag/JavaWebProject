package Control;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import DAO.DAOOrder;
import DAO.DAOOrderDetail;
import DAO.DAOUser;
import Entity.Order;
import Entity.OrderDetail;
import Entity.Product;
import Entity.User;

/**
 * Servlet implementation class CreateOrderControl
 */
@WebServlet("/CreateOrder")
public class CreateOrderControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public CreateOrderControl() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		DAOOrder odao = new DAOOrder();
		DAOUser udao = new DAOUser();
		DAOOrderDetail oddao = new DAOOrderDetail();
		String fullname = request.getParameter("fullname");
		String address = request.getParameter("address");
		String phone = request.getParameter("phone");
		String email = request.getParameter("email");
		HttpSession session = request.getSession();
		String username = (String) session.getAttribute("user");
		double total = (Double) session.getAttribute("total");
		@SuppressWarnings("unchecked")
		List<Product> cart = (List<Product>) session.getAttribute("cart");
		User user = udao.getUserByUsername(username);
		int userId = user.getId();
		udao.update(username, fullname, email, address, phone);
		odao.insert(new Order(java.time.LocalDate.now().toString(), total, userId));
		int orderId = odao.getLatestOrderId();
		for (Product p : cart) {
			oddao.insert(new OrderDetail(orderId, p.getId(), p.getQuantity(), p.getPrice()));
		}
		session.setAttribute("cart", new ArrayList<Product>());
		request.getRequestDispatcher("/Home").forward(request, response);
	}

}
