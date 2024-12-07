package Control;

import java.io.IOException;
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
import Entity.User;
import java.util.*;
/**
 * Servlet implementation class OrderHistoryControl
 */
@WebServlet("/OrderHistory")
public class OrderHistoryControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public OrderHistoryControl() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		HttpSession session = request.getSession();
		String username = (String) session.getAttribute("user");
		if (username == null) {
            response.sendRedirect("Login");
            return;
        }
		
		DAOOrder odao = new DAOOrder();
		DAOUser udao = new DAOUser();
		DAOOrderDetail oddao = new DAOOrderDetail();
		
		User currentUser = udao.getUserByUsername(username);
		int userId = currentUser.getId();
		List<Order> olist = odao.getAllOrders(userId);
		List<OrderDetail> odlist = oddao.getAllOrderDetails(userId);
		request.setAttribute("odlist", odlist);
		request.setAttribute("olist", olist);
		request.setAttribute("currentUser", currentUser);
		request.getRequestDispatcher("/orderHistory.jsp").forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
