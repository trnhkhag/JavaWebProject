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

@WebServlet("/ChangeQuantity")
public class ChangeQuantityControl extends HttpServlet {
    private static final long serialVersionUID = 1L;

    public ChangeQuantityControl() {
        super();
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int pid = Integer.parseInt(request.getParameter("productId"));
        String quantityStr = request.getParameter("quantity");
        
        HttpSession session = request.getSession();
        @SuppressWarnings("unchecked")
        List<Product> cart = (List<Product>) session.getAttribute("cart");

        int quantity;
        
        // Validate quantity input
        try {
            quantity = Integer.parseInt(quantityStr);
            if (quantity <= 0) {
                response.setContentType("text/plain");
                response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
                response.getWriter().write("Quantity must be a positive integer.");
                return;
            }
        } catch (NumberFormatException e) {
            response.setContentType("text/plain");
            response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
            response.getWriter().write("Invalid quantity format.");
            return;
        }

        // Update product quantity in cart if stock allows
        for (Product p : cart) {
            if (p.getId() == pid) {
                if (quantity > p.getStock()) {
                    response.setContentType("text/plain");
                    response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
                    response.getWriter().write("Quantity exceeds available stock.");
                    return;
                }
                p.setQuantity(quantity);
            }
        }

        // Calculate the new total
        double total = 0;
        for (Product product : cart) {
            total += product.getPrice() * product.getQuantity();
        }
        session.setAttribute("total", total);

        // Send success response
        response.setContentType("text/plain");
        response.getWriter().write("Quantity updated successfully.");
    }
}
