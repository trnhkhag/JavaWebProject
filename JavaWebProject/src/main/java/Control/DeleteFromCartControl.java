package Control;

import java.io.IOException;
import java.util.Iterator;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import Entity.Product;

/**
 * Servlet implementation class DeleteFromCartControl
 */
@WebServlet("/DeleteFromCart")
public class DeleteFromCartControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public DeleteFromCartControl() {
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
		HttpSession session = request.getSession();
		@SuppressWarnings("unchecked")
		List<Product> cart = (List<Product>) session.getAttribute("cart");
		Iterator<Product> itr = cart.iterator();
		while (itr.hasNext()) {
			Product p = (Product) itr.next();
			if (p.getId() == pid) {
				itr.remove();
			}
		}
		double total = 0;
		for (Product product : cart) {
			total += product.getPrice() * product.getQuantity();
		}
		session.setAttribute("total", total);
	}

}
