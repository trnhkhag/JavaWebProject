package Control;

import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import DAO.DAOProduct;
import Entity.Product;

/**
 * Servlet implementation class AddToCartControl
 */
@WebServlet("/AddToCart")
public class AddToCartControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AddToCartControl() {
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
		DAOProduct pdao = new DAOProduct();
		HttpSession session = request.getSession();
		@SuppressWarnings("unchecked")
		List<Product> cart = (List<Product>) session.getAttribute("cart");
		Product p = pdao.getProductById(pid);
		if (cart.contains(p)) {
			for (Product product : cart) {
				if (product.equals(p)) {
					product.setQuantity(product.getQuantity() + 1);
				}
			}
		}
		else {
			p.setQuantity(Integer.parseInt(request.getParameter("quantity")));
			cart.add(p);
		}
		double total = 0;
		for (Product product : cart) {
			total += product.getPrice() * product.getQuantity();
		}
		session.setAttribute("total", total);
		session.setAttribute("cart", cart);
	}

}
