package Control;

import java.io.IOException;
import java.io.PrintWriter;

import com.google.gson.Gson;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import DAO.DAOProduct;
import Entity.Product;
/**
 * Servlet implementation class GetProductInfoControl
 */
@WebServlet("/GetProductInfo")
public class GetProductInfoControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
    /**
     * @see HttpServlet#HttpServlet()
     */
    public GetProductInfoControl() {
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
		response.setContentType("application/json");
		response.setCharacterEncoding("UTF-8");
		int pid = Integer.parseInt(request.getParameter("productId"));
		DAOProduct pdao = new DAOProduct();
		Product p = pdao.getProductById(pid);
		String pString = new Gson().toJson(p);
		PrintWriter out = response.getWriter();
		out.print(pString);
        out.flush();
	}

}
