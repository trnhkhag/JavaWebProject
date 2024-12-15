package Control;

import java.io.IOException;
import java.util.Properties;
import java.util.Random;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import DAO.DAOUser;

/**
 * Servlet implementation class ForgotpasswordControl
 */
@WebServlet("/Forgotpassword")
public class ForgotpasswordControl extends HttpServlet {
    private static final long serialVersionUID = 1L;

    public ForgotpasswordControl() {
        super();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.getRequestDispatcher("/forgotpassword.jsp").forward(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String email = request.getParameter("email");

        boolean hasError = false;
        StringBuilder errorString = new StringBuilder();

        if (email == null || email.isEmpty()) {
            hasError = true;
            errorString.append("Email is required. ");
        }

        DAOUser dao = new DAOUser();
        if (!dao.isEmailExist(email)) {
            hasError = true;
            errorString.append("Your email is not connected to any account.");
        }

        if (hasError) {
            // Pass error messages back to the forgot password page
            request.setAttribute("errorString", errorString.toString());
            request.getRequestDispatcher("/forgotpassword.jsp").forward(request, response);
        } else {
            // Generate a 6-digit random code
            String code = generateVerificationCode();

            // Send email
            try {
                sendEmail(email, code);
                request.setAttribute("successMessage", "A verification code has been sent to your email.");
                // Save the code in the session for verification later
                request.getSession().setAttribute("verificationCode", code);
                request.getSession().setAttribute("email", email);
                request.getRequestDispatcher("/entercode.jsp").forward(request, response);
            } catch (MessagingException e) {
                request.setAttribute("errorString", "Failed to send email. Please try again later.");
                request.getRequestDispatcher("/forgotpassword.jsp").forward(request, response);
            }
        }
    }

    // Generate a 6-digit random number as a string
    private String generateVerificationCode() {
        Random random = new Random();
        int code = 100000 + random.nextInt(900000); // Generate a number between 100000 and 999999
        return String.valueOf(code);
    }

    // Send an email with the verification code
    private void sendEmail(String recipientEmail, String code) throws MessagingException {
        // Set up email properties
        Properties props = new Properties();
        props.put("mail.smtp.host", "smtp.gmail.com"); // SMTP server
        props.put("mail.smtp.port", "587"); // TLS port
        props.put("mail.smtp.auth", "true"); // Enable authentication
        props.put("mail.smtp.starttls.enable", "true"); // Enable STARTTLS

        // Create session with an email account (you'll need a valid email and password)
        final String senderEmail = "hkhang.trn@gmail.com";
        final String senderPassword = "hbbk eatc tctt dgsr";
        Session session = Session.getInstance(props, new javax.mail.Authenticator() {
            protected javax.mail.PasswordAuthentication getPasswordAuthentication() {
                return new javax.mail.PasswordAuthentication(senderEmail, senderPassword);
            }
        });

        // Create the email message
        Message message = new MimeMessage(session);
        message.setFrom(new InternetAddress(senderEmail));
        message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(recipientEmail));
        message.setSubject("Your Verification Code");
        message.setText("Your verification code is: " + code);

        // Send the email
        Transport.send(message);
    }
}
