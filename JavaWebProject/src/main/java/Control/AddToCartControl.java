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
        HttpSession session = request.getSession();

        // Check if the user is logged in
        String username = (String) session.getAttribute("user");
        if (username == null) {
            // User not logged in; send error response
            response.setContentType("text/plain");
            response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
            response.getWriter().write("Please log in to add products to your cart.");
            return;
        }

        // Proceed with adding the product to the cart if user is logged in
        int pid = Integer.parseInt(request.getParameter("productId"));
        int quantity = Integer.parseInt(request.getParameter("quantity"));
        DAOProduct pdao = new DAOProduct();

        // Retrieve the product by ID
        Product p = pdao.getProductById(pid);
        if (p == null) {
            response.setContentType("text/plain");
            response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
            response.getWriter().write("Product not found.");
            return;
        }

        // Check if requested quantity exceeds available stock
        int availableStock = p.getStock();  // Assuming getStock() method exists in Product class
        if (quantity > availableStock) {
            response.setContentType("text/plain");
            response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
            response.getWriter().write("Requested quantity exceeds available stock.");
            return;
        }

        // Retrieve the cart from the session or create a new one if it doesn't exist
        @SuppressWarnings("unchecked")
        List<Product> cart = (List<Product>) session.getAttribute("cart");
        if (cart == null) {
            cart = new ArrayList<>();
            session.setAttribute("cart", cart);
        }

        boolean found = false;

        // Check if the product already exists in the cart and update quantity if it does
        for (Product product : cart) {
            if (product.equals(p)) {
                int newQuantity = product.getQuantity() + quantity;
                
                // Check again if the updated quantity exceeds stock
                if (newQuantity > availableStock) {
                    response.setContentType("text/plain");
                    response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
                    response.getWriter().write("Updated quantity exceeds available stock.");
                    return;
                }
                
                product.setQuantity(newQuantity);
                found = true;
                break;
            }
        }

        // If product is not in the cart, add it with the specified quantity
        if (!found) {
            p.setQuantity(quantity);
            cart.add(p);
        }

        // Calculate the total
        double total = 0;
        for (Product product : cart) {
            total += product.getPrice() * product.getQuantity();
        }
        session.setAttribute("total", total);

        // Send success response
        response.setContentType("text/plain");
        response.getWriter().write("Product added to cart successfully!");
    }
}
