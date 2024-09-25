package Control;

import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import DAO.DAOCategory;
import DAO.DAOProduct;
import Entity.Category;
import Entity.Product;

/**
 * Servlet implementation class AdminProductControl
 */
@WebServlet("/AdminProduct")
public class AdminProductControl extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public AdminProductControl() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		DAOProduct pdao = new DAOProduct();
		DAOCategory cdao = new DAOCategory();
		List<Product> plist = pdao.getAllProductWithCategory();
		List<Category> clist = cdao.getAllCategories();
		request.setAttribute("clist", clist);
		request.setAttribute("plist", plist);
		request.getRequestDispatcher("/admin_product.jsp").forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		
	}
}
