package Control;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import DAO.DAOProduct;
import Entity.Product;

/**
 * Servlet implementation class EditProductControl
 */
@WebServlet("/EditProduct")
@MultipartConfig(fileSizeThreshold = 1024 * 1024 * 2, maxFileSize = 1024 * 1024 * 50, maxRequestSize = 1024 * 1024 * 50)
public class EditProductControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public EditProductControl() {
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
		int pid = Integer.parseInt(request.getParameter("pid"));
		String pname = request.getParameter("pname");
		int pcategory = Integer.parseInt(request.getParameter("pcategory"));
		int pstock = Integer.parseInt(request.getParameter("pstock"));
		int pstatus = Integer.parseInt(request.getParameter("pstatus"));
		double pprice = Double.parseDouble(request.getParameter("pprice"));
		String brand = request.getParameter("pbrand");
		String pdesc = request.getParameter("pdesc");
		String pimageName = "images/" + request.getPart("pimage").getSubmittedFileName();
		DAOProduct pdao = new DAOProduct();
		if (request.getPart("pimage").getSubmittedFileName() != null) {
			pdao.update(new Product(pname, pprice, pimageName, pstock, pstatus, brand, pdesc, pcategory), pid);
		}
		else {
			pdao.update(new Product(pname, pprice, pstock, pstatus, brand, pdesc, pcategory), pid);
		}
		response.sendRedirect("AdminProduct");
	}

}
