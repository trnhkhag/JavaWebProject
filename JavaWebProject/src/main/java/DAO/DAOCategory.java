package DAO;

import java.sql.*;
import java.util.*;
import Entity.Category;
import Context.DBContext;

public class DAOCategory {
	public List<Category> getAllCategories() {
		try {
			List<Category> clist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * from loai";
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				clist.add(new Category(rs.getInt("MaLoai"),
									   rs.getString("TenLoai")));
			}
			stmt.close();
			conn.close();
			return clist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public static void main(String[] args) {
		DAOCategory dao = new DAOCategory();
		System.out.println(dao.getAllCategories());
	}
}
