package DAO;

import java.sql.*;
import Entity.Order;
import Context.DBContext;
import java.util.*;

public class DAOOrder {
	public boolean insert(Order order) {
		try {
			Connection conn = DBContext.getConnection();
			String sql = "INSERT INTO donhang (NgayLap, ThanhTien, MaNguoiDung) VALUES(?, ?, ?)";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, order.getDate());
			stmt.setDouble(2, order.getTotal());
			stmt.setInt(3, order.getUserId());
			boolean isInserted = false;
			if (stmt.executeUpdate() > 0) {
				isInserted = true;
			}
			stmt.close();
			conn.close();
			return isInserted;
		} catch (Exception ex) {
			// TODO: handle exception
			ex.printStackTrace();
		}
		return false;
	}
	
	public int getLatestOrderId() {
		try {
			int id = -1;
			Connection conn = DBContext.getConnection();
			String sql = "SELECT MAX(MaDH) FROM donhang";
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				id = rs.getInt(1);
			}
			stmt.close();
			conn.close();
			return id;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return -1;
	}
	
	public List<Order> getAllOrders(int userId) {
		try {
			List<Order> olist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM donhang WHERE MaNguoiDung = ? ORDER BY NgayLap DESC";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, userId);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				olist.add(new Order(rs.getInt("MaDH"), 
							        rs.getString("NgayLap"), 
							        rs.getString("TrangThai"), 
							        rs.getDouble("ThanhTien"),
							        rs.getInt("MaNguoiDung")));
			}
			stmt.close();
			conn.close();
			return olist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public double getStatistical(int month, int year) {
		try {
			double statistical = 0;
			Connection conn = DBContext.getConnection();
			String sql = "SELECT SUM(ThanhTien) AS doanhthu FROM donhang WHERE MONTH(NgayLap) = ? AND YEAR(NgayLap) = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, month);
			stmt.setInt(2, year);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				statistical = rs.getDouble("doanhthu");
			}
			stmt.close();
			conn.close();
			return statistical;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return 0;
	}
	
	public static void main(String[] args) {
		DAOOrder dao = new DAOOrder();
		System.out.println(dao.getStatistical(5, 2023));
	}
}
