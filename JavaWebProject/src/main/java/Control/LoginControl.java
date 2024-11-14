package Control;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import DAO.DAOUser;
import Entity.Product;
import Entity.User;

/**
 * Servlet implementation class LoginControl
 */
@WebServlet("/Login")
public class LoginControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginControl() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		RequestDispatcher dispatcher = this.getServletContext().getRequestDispatcher("/login1.jsp");
		dispatcher.forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String username = request.getParameter("username");
        String password = request.getParameter("password");
        boolean hasError = false;
        String errorString = null;

        // Check if username is empty
        if (username == null || username.isEmpty()) {
            hasError = true;
            errorString = "Username cannot be empty.";
        }
        // Check if password is empty
        else if (password == null || password.isEmpty()) {
            hasError = true;
            errorString = "Password cannot be empty.";
        }
        // Check if password length is less than 6 characters
        else if (password.length() < 6) {
            hasError = true;
            errorString = "Password must be at least 6 characters long.";
        } else {
            // Validate username and password against the database
            DAOUser dao = new DAOUser();
            if (!dao.check(username, password)) {
                hasError = true;
                errorString = "Invalid username or password.";
            }
        }

        if (hasError) {
            request.setAttribute("username", username);
            request.setAttribute("errorString", errorString);
            RequestDispatcher dispatcher = this.getServletContext().getRequestDispatcher("/login1.jsp");
            dispatcher.forward(request, response);
        } else {
            // Login successful, set session attributes and redirect accordingly
            DAOUser udao = new DAOUser();
            User user = udao.getUser(username, password);
            HttpSession session = request.getSession();
            session.setAttribute("user", username);
            session.setAttribute("pass", password);
            session.setAttribute("role", user.getRole());
            
            if ("Admin".equals(user.getRole())) {
                response.sendRedirect(request.getContextPath() + "/admin_index.html");
            } else {
                session.setAttribute("cart", new ArrayList<Product>());
                response.sendRedirect(request.getContextPath() + "/Home");
            }
        }
	}

}
