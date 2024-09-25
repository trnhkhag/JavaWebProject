package Control;

import java.io.IOException;
import java.sql.Date;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import DAO.DAOadmin;
import Entity.OrderList;

/**
 * Servlet implementation class searchcontrol
 */
@WebServlet("/searchcontrol")
public class searchcontrol extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public searchcontrol() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		DAOadmin dao=new DAOadmin();
		
		String search=request.getParameter("search");
		String submit = request.getParameter("submit");
		
		if(search.equals("date")){
		String date=request.getParameter("date");
		List<OrderList> searchin4bydate=dao.getinfobyday(date);
		request.setAttribute("in4", searchin4bydate);
		
		}else if(search.equals("price")) {
		
		String from=request.getParameter("from");
		String to=request.getParameter("to");
		List<OrderList> searchin4bymoney=dao.getinfobymoney(from,to);
		request.setAttribute("in4", searchin4bymoney);
		}else if (search.equals("datiepnhan")) {
			  String status = request.getParameter("stt");
			  if(status=="Đã Tiếp Nhận") {
			    List<OrderList> searchin4bystt = dao.getinfobystt(status);
			    request.setAttribute("in4", searchin4bystt);
			  }else if(status=="Đang Giao") {
				    List<OrderList> searchin4bystt = dao.getinfobystt(status);
				    request.setAttribute("in4", searchin4bystt);
			  }else {
				  List<OrderList> searchin4bystt = dao.getinfobystt(status);
				    request.setAttribute("in4", searchin4bystt);
			  }
			}
		else {
		
		String txt = request.getParameter("searchbyname");
		List<OrderList> searchin4byname = dao.getinfobysearch(txt);
		request.setAttribute("in4", searchin4byname);
	
		}

		request.getRequestDispatcher("admin_order_list.jsp").forward(request, response);	


		}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
