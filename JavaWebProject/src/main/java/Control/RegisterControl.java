package Control;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import DAO.DAOUser;
import Entity.User;

/**
 * Servlet implementation class RegisterControl
 */
@WebServlet("/Register")
public class RegisterControl extends HttpServlet {
    private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#HttpServlet()
     */
    public RegisterControl() {
        super();
    }

    /**
     * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.getServletContext().getRequestDispatcher("/register.jsp").forward(request, response);
    }

    /**
     * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("user");
        String password = request.getParameter("pass");
        String phone = request.getParameter("phone");
        String email = request.getParameter("email");

        // Server-side validation
        boolean hasError = false;
        StringBuilder errorString = new StringBuilder();

        if (username == null || username.isEmpty()) {
            hasError = true;
            errorString.append("Username is required. ");
        }
        if (email == null || email.isEmpty()) {
            hasError = true;
            errorString.append("Email is required. ");
        }
        if (phone == null || phone.isEmpty()) {
            hasError = true;
            errorString.append("Phone number is required. ");
        }
        if (password == null || password.isEmpty()) {
            hasError = true;
            errorString.append("Password is required. ");
        } else if (password.length() < 6) {
            hasError = true;
            errorString.append("Password must be at least 6 characters. ");
        }

        // Check if username already exists
        DAOUser dao = new DAOUser();
        if (dao.isUsernameExist(username)) {
            hasError = true;
            errorString.append("Username already exists. ");
        }

        if (hasError) {
            // Pass error messages back to the registration page
            request.setAttribute("errorString", errorString.toString());
            request.getRequestDispatcher("/register.jsp").forward(request, response);
        } else {
            // Proceed to insert the user and redirect to the login page
            dao.insert(new User(username, password, email, phone, "Customer"));
            request.setAttribute("user", username);
            request.setAttribute("pass", password);
            response.sendRedirect("login1.jsp");  // Redirect to login page after successful registration
        }
    }
}
