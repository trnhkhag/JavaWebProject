package Control;

import java.io.IOException;
import java.io.PrintWriter;
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

        boolean productRemoved = false;
        if (cart != null) {
            Iterator<Product> itr = cart.iterator();
            while (itr.hasNext()) {
                Product p = itr.next();
                if (p.getId() == pid) {
                    itr.remove();
                    productRemoved = true;
                    break;
                }
            }
        }

        // Recalculate total price if product was removed
        double total = 0;
        if (productRemoved) {
            for (Product product : cart) {
                total += product.getPrice() * product.getQuantity();
            }
            session.setAttribute("total", total);
        }

        // Set response content type to plain text and output result
        response.setContentType("text/plain");
        PrintWriter out = response.getWriter();

        if (productRemoved) {
            out.print("Product removed successfully.");
        } else {
            out.print("Product not found in cart.");
        }

        out.flush();
	}

}
