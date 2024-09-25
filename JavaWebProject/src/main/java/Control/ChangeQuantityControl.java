package Control;

import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import Entity.Product;

/**
 * Servlet implementation class ChangeQuantityControl
 */
@WebServlet("/ChangeQuantity")
public class ChangeQuantityControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ChangeQuantityControl() {
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
		int pid = Integer.parseInt(request.getParameter("productId"));
		int quantity = Integer.parseInt(request.getParameter("quantity"));
		HttpSession session = request.getSession();
		@SuppressWarnings("unchecked")
		List<Product> cart = (List<Product>) session.getAttribute("cart");
		for (Product p : cart) {
			if (p.getId() == pid) {
				p.setQuantity(quantity);
			}
		}
		double total = 0;
		for (Product product : cart) {
			total += product.getPrice() * product.getQuantity();
		}
		session.setAttribute("total", total);
	}

}
