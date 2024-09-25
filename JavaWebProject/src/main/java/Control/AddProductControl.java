package Control;

import java.io.File;
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
 * Servlet implementation class AddProductControl
 */
@WebServlet("/AddProduct")
@MultipartConfig(fileSizeThreshold = 1024 * 1024 * 2, maxFileSize = 1024 * 1024 * 50, maxRequestSize = 1024 * 1024 * 50)
public class AddProductControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AddProductControl() {
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
		String pname = request.getParameter("pname");
		int pcategory = Integer.parseInt(request.getParameter("pcategory"));
		int pstock = Integer.parseInt(request.getParameter("pstock"));
		int pstatus = Integer.parseInt(request.getParameter("pstatus"));
		double pprice = Double.parseDouble(request.getParameter("pprice"));
		String brand = request.getParameter("pbrand");
		String pdesc = request.getParameter("pdesc");
		String pimageName = "images/" + request.getPart("pimage").getSubmittedFileName();
		
		DAOProduct pdao = new DAOProduct();
		pdao.insert(new Product(pname, pprice, pimageName, pstock, pstatus, brand, pdesc, pcategory));
		response.sendRedirect("AdminProduct");
	}

//	private String extractFileName(Part part) {
//		String contentDisp = part.getHeader("content-disposition");
//		String[] items = contentDisp.split(";");
//		for (String s : items) {
//			if (s.trim().startsWith("filename")) {
//				return s.substring(s.indexOf("=") + 2, s.length() - 1);
//			}
//		}
//		return "";
//	}

	public File getFolderUpload() {
		File folderUpload = new File("C:\\Users\\trnhk\\eclipse-workspace\\JavaWebProject\\src\\main\\webapp\\images");
		if (!folderUpload.exists()) {
			folderUpload.mkdirs();
		}
		return folderUpload;
	}
}
