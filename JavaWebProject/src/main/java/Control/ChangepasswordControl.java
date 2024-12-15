package Control;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import DAO.DAOUser;

/**
 * Servlet implementation class ChangepasswordControl
 */
@WebServlet("/Changepassword")
public class ChangepasswordControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ChangepasswordControl() {
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
	    // Get the password entered by the user
	    String password = request.getParameter("password");
	    
	    // Get the email stored in the session
	    HttpSession session = request.getSession();
	    String email = (String) session.getAttribute("email");
	    
	    DAOUser dao = new DAOUser();
	    boolean hasError = false;
	    String errorMessage = "";

	    // Validate inputs
	    if (email == null || email.isEmpty()) {
	        hasError = true;
	        errorMessage = "Session expired. Please try again.";
	    }

	    if (password == null || password.isEmpty()) {
	        hasError = true;
	        errorMessage = "Password cannot be empty.";
	    } else if (password.length() < 6) {
	        hasError = true;
	        errorMessage = "Password must be at least 6 characters long.";
	    }

	    if (hasError) {
	        request.setAttribute("errorString", errorMessage);
	        request.getRequestDispatcher("/changepassword.jsp").forward(request, response);
	        return;
	    }

	    // Proceed with updating the password
	    try {
	        // Update password in the database
	        boolean isUpdated = dao.update(email, password);

	        if (isUpdated) {
	        	// Invalidate the current session for security
	            session.invalidate();
	            
	            request.setAttribute("successMessage", "Password updated successfully!");
	            response.sendRedirect(request.getContextPath() + "/Login");
	        } else {
	            request.setAttribute("errorString", "Failed to update password. Please try again.");
	            request.getRequestDispatcher("/changepassword.jsp").forward(request, response);
	        }
	    } catch (Exception e) {
	        e.printStackTrace();
	        request.setAttribute("errorString", "An error occurred while updating the password. Please try again later.");
	        request.getRequestDispatcher("/changepassword.jsp").forward(request, response);
	    }
	}

}
