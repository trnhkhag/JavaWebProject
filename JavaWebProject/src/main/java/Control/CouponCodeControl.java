package Control;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class CouponCodeControl
 */
@WebServlet("/CouponCode")
public class CouponCodeControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public CouponCodeControl() {
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
		// Get session
	    HttpSession session = request.getSession();

	    // Set response content type to JSON
	    response.setContentType("application/json");
	    response.setCharacterEncoding("UTF-8");

	    // Get the coupon code from the request
	    String coupon = request.getParameter("coupon");
	    PrintWriter out = response.getWriter();

	    // Get subtotal, shipping fee, and total from session
	    double shipping = (double) session.getAttribute("shipping");
	    double subtotal = (double) session.getAttribute("subtotal");
//	    double total = (double) session.getAttribute("total");

	    try {
	        // Process coupon code
	        if (coupon == null || coupon.isEmpty()) {
	            response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
	            out.write("{\"message\":\"Invalid coupon code.\"}");
	        } else {
	            String message;
	            switch (coupon) {
	                case "FREESHIP":
	                    // Apply free shipping
	                    session.setAttribute("shipping", 0.0);
	                    session.setAttribute("total", subtotal); // Update total to exclude shipping
	                    message = "Free shipping applied successfully!";
	                    break;

	                case "DISCOUNT100":
	                    // Apply $100 discount for orders above $1000
	                    if (subtotal >= 1000) {
	                        subtotal -= 100;
	                        session.setAttribute("subtotal", subtotal);
	                        session.setAttribute("total", subtotal + shipping); // Update total
	                        message = "Discount of $100 applied successfully!";
	                    } else {
	                        response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
	                        out.write("{\"message\":\"Order value must be at least $1000 for this coupon.\"}");
	                        return;
	                    }
	                    break;

	                case "DISCOUNT10P":
	                    // Apply 10% discount for orders above $2000
	                    if (subtotal >= 2000) {
	                        double discount = subtotal * 0.1;
	                        subtotal -= discount;
	                        session.setAttribute("subtotal", subtotal);
	                        session.setAttribute("total", subtotal + shipping); // Update total
	                        message = "10% discount applied! You saved $" + discount;
	                    } else {
	                        response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
	                        out.write("{\"message\":\"Order value must be at least $2000 for this coupon.\"}");
	                        return;
	                    }
	                    break;

	                default:
	                    response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
	                    out.write("{\"message\":\"Invalid coupon code.\"}");
	                    return;
	            }

	            // Respond with success message
	            out.write("{\"message\":\"" + message + "\"}");
	        }
	    } catch (Exception e) {
	        // Handle unexpected errors
	        response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
	        out.write("{\"message\":\"An error occurred while processing the coupon code. Please try again later.\"}");
	    } finally {
	        out.close();
	    }
	}

}
