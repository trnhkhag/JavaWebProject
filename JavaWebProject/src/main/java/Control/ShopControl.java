package Control;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.*;

import DAO.DAOCategory;
import DAO.DAOProduct;
import Entity.Category;
import Entity.Product;

/**
 * Servlet implementation class ShopControl
 */
@WebServlet("/Shop")
public class ShopControl extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ShopControl() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		DAOProduct pdao = new DAOProduct();
        DAOCategory cdao = new DAOCategory();
        List<String> blist = pdao.getAllBrand();
        List<Category> clist = cdao.getAllCategories();

        int currentPage = (request.getParameter("page") == null) ? 1 : Integer.parseInt(request.getParameter("page"));
        List<Product> plist = new ArrayList<>();
        int productNum = 0;
        StringBuilder queryString = new StringBuilder(); // To store the filter parameters for pagination

        if (request.getParameter("cid") != null) {
            String cid = request.getParameter("cid");
            plist = pdao.getProductInCategory(cid.trim(), currentPage);
            productNum = pdao.getNoOfProductInCategory(cid);
            queryString.append("&cid=").append(cid);
        } else if (request.getParameter("search-input") != null) {
            String searchInput = request.getParameter("search-input");
            plist = pdao.searchProduct(searchInput, currentPage);
            productNum = pdao.getNoOfSearchProduct(searchInput);
            queryString.append("&search-input=").append(searchInput);
        } else if (request.getParameter("filterSubmit") != null) {
            List<String> categories = new ArrayList<>();
            List<String> brands = new ArrayList<>();

            for (Category c : clist) {
                String categoryId = request.getParameter("category" + c.getId());
                if (categoryId != null) {
                    categories.add(categoryId);
                    queryString.append("&category").append(c.getId()).append("=").append(categoryId);
                }
            }

            for (String b : blist) {
                String brand = request.getParameter(b);
                if (brand != null) {
                    brands.add(brand);
                    queryString.append("&").append(b).append("=").append(brand);
                }
            }

            Double minPrice = Double.parseDouble(request.getParameter("minPrice"));
            Double maxPrice = Double.parseDouble(request.getParameter("maxPrice"));

            plist = pdao.getProductByFilter(categories, brands, minPrice, maxPrice, currentPage);
            productNum = pdao.getNoOfFilteredProducts(categories, brands, minPrice, maxPrice);

            queryString.append("&minPrice=").append(minPrice);
            queryString.append("&maxPrice=").append(maxPrice);
        } else {
            plist = pdao.getAllProduct(currentPage);
            productNum = pdao.getNoOfAllProduct();
        }

        int numPage = (int) Math.ceil(productNum / 8.0);

        // Set attributes for JSP
        request.setAttribute("numPage", numPage);
        request.setAttribute("curPage", currentPage);
        request.setAttribute("blist", blist);
        request.setAttribute("clist", clist);
        request.setAttribute("plist", plist);
        request.setAttribute("queryString", queryString.toString());

        request.getRequestDispatcher("/shop.jsp").forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
