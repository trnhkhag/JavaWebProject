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

import DAO.DAOProduct;
import Entity.Product;

@WebServlet("/AddToCart")
public class AddToCartControl extends HttpServlet {
    private static final long serialVersionUID = 1L;

    public AddToCartControl() {
        super();
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int pid = Integer.parseInt(request.getParameter("productId"));
        int quantity = Integer.parseInt(request.getParameter("quantity"));
        DAOProduct pdao = new DAOProduct();
        HttpSession session = request.getSession();

        // Retrieve the cart from the session or create a new one
        @SuppressWarnings("unchecked")
        List<Product> cart = (List<Product>) session.getAttribute("cart");
        if (cart == null) {
            cart = new ArrayList<>();
            session.setAttribute("cart", cart);
        }

        Product p = pdao.getProductById(pid);
        boolean found = false;

        // Check if the product already exists in the cart and update quantity if it does
        for (Product product : cart) {
            if (product.equals(p)) {
                product.setQuantity(product.getQuantity() + quantity);
                found = true;
                break;
            }
        }

        // If product is not in the cart, add it with the specified quantity
        if (!found) {
            p.setQuantity(quantity);
            cart.add(p);
        }

        // Calculate total
        double total = 0;
        for (Product product : cart) {
            total += product.getPrice() * product.getQuantity();
        }
        session.setAttribute("total", total);

        // Send a response message
        response.setContentType("text/plain");
        response.getWriter().write("Product added to cart successfully!");
    }
}
