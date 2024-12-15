package Control;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class EntercodeControl
 */
@WebServlet("/Entercode")
public class EntercodeControl extends HttpServlet {
    private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#HttpServlet()
     */
    public EntercodeControl() {
        super();
    }

    /**
     * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Get the code entered by the user
        String enteredCode = request.getParameter("code");

        // Get the generated code stored in the session
        HttpSession session = request.getSession();
        String sessionCode = (String) session.getAttribute("verificationCode");
        String email = (String) session.getAttribute("email");

        // Validate the entered code
        if (enteredCode == null || enteredCode.isEmpty()) {
            // Code is empty
            request.setAttribute("errorString", "Code cannot be empty.");
            request.getRequestDispatcher("/entercode.jsp").forward(request, response);
            return;
        }

        if (sessionCode == null) {
            // No code in session (e.g., session expired)
            request.setAttribute("errorString", "Session expired. Please request a new code.");
            request.getRequestDispatcher("/entercode.jsp").forward(request, response);
            return;
        }

        if (enteredCode.equals(sessionCode)) {
            // Code is valid
            session.removeAttribute("verificationCode"); // Clear the code from the session
            request.setAttribute("successMessage", "Code verified successfully!");
            request.getRequestDispatcher("/changepassword.jsp").forward(request, response);
        } else {
            // Code is invalid
            request.setAttribute("errorString", "Invalid code. Please try again.");
            request.getRequestDispatcher("/entercode.jsp").forward(request, response);
        }
    }
}
