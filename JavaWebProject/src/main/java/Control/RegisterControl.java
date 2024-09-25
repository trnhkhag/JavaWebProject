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
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		this.getServletContext().getRequestDispatcher("/register.jsp").forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String username = request.getParameter("user");
		String password = request.getParameter("pass");
		String phone = request.getParameter("phone");
		String email = request.getParameter("email");
		boolean hasError = false;
		String errorString = null;
		
		DAOUser dao = new DAOUser();
		if (dao.isUsernameExist(username)) {
			hasError = true;
			errorString = "Username already exist!";
		}
		
		if (hasError) {
			request.setAttribute("errorString", errorString);
			request.getRequestDispatcher("/Register").forward(request, response);
		}
		else {
			dao.insert(new User(username, password, email, phone, "Customer"));
			request.setAttribute("user", username);
			request.setAttribute("pass", password);
			request.setAttribute("errorString", errorString);
			request.getRequestDispatcher("/login1.jsp").forward(request, response);
		}
	}

}
