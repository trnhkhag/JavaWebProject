package DAO;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

import Context.DBContext;
import Entity.OrderList;
import Entity.Product;

public class DAOadmin {
	public List<OrderList> getinfo() {
		try {
			List<OrderList> info = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM donhang";
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				info.add(new OrderList(rs.getString("MaDH"),
						rs.getString("HoTen"),
										rs.getString("SDT"),
										rs.getString("TrangThai"),
										rs.getDouble("ThanhTien"),
										rs.getDate("NgayLap")
						));
				          
							          
			}
			stmt.close();
			conn.close();
			return info;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	public List<OrderList> getinfobyday(String date) {
		try {
			List<OrderList> info = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM donhang WHERE NgayLap= ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1,date);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				info.add(new OrderList(rs.getString("MaDH"),
						rs.getString("HoTen"),
										rs.getString("SDT"),
										rs.getString("TrangThai"),
										rs.getDouble("ThanhTien"),
										rs.getDate("NgayLap")
						));
				          
							          
			}
			stmt.close();
			conn.close();
			return info;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	public List<OrderList> getinfobymoney(String s1,String s2) {
		try {
			List<OrderList> info = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM donhang WHERE ThanhTien BETWEEN ? AND ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1,s1);
			stmt.setString(2,s2);

			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				info.add(new OrderList(rs.getString("MaDH"),
						rs.getString("HoTen"),
										rs.getString("SDT"),
										rs.getString("TrangThai"),
										rs.getDouble("ThanhTien"),
										rs.getDate("NgayLap")
						));
				          
							          
			}
			stmt.close();
			conn.close();
			return info;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	public List<OrderList> getinfobysearch(String txt) {
		try {
			List<OrderList> info = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM donhang WHERE HoTen Like ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1,"%"+ txt +"%");

			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				info.add(new OrderList(rs.getString("MaDH"),
						rs.getString("HoTen"),
										rs.getString("SDT"),
										rs.getString("TrangThai"),
										rs.getDouble("ThanhTien"),
										rs.getDate("NgayLap")
						));
				          
							          
			}
			stmt.close();
			conn.close();
			return info;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	public String updatestatus(String status,String madh) {
	    String result = "";
	    try {
	        Connection conn = DBContext.getConnection();
	        String sql = "UPDATE donhang SET TrangThai=? WHERE MaDH=?";
	        PreparedStatement stmt = conn.prepareStatement(sql);
	        stmt.setString(1, status);
	        stmt.setString(2, madh);

	        int rows = stmt.executeUpdate();
	        conn.close();
	        if (rows > 0) {
	            result = "Update successful";
	        } else {
	            result = "No rows updated";
	        }
	    } catch (Exception ex) {
	        System.out.println("ERROR: " + ex.getMessage());
	        result = "Update failed: " + ex.getMessage();
	    }
	    return result;
	}
	public List<OrderList> getinfobystt(String stt) {
		try {
			List<OrderList> info = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM donhang WHERE TrangThai=?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1,stt);

			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				info.add(new OrderList(rs.getString("MaDH"),
										rs.getString("HoTen"),
										rs.getString("SDT"),
										rs.getString("TrangThai"),
										rs.getDouble("ThanhTien"),
										rs.getDate("NgayLap")
						));
				          
							          
			}
			stmt.close();
			conn.close();
			return info;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}

	public List<OrderList> info(String madh) {
		try {
			List<OrderList> info = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM donhang WHERE MaDH=?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1,madh);

			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				info.add(new OrderList(rs.getString("MaDH"),
										rs.getString("TrangThai"),
										rs.getDouble("ThanhTien"),
										rs.getDate("NgayLap")
						));
				          
							          
			}
			stmt.close();
			conn.close();
			return info;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	public List<OrderList> infoo(String madh) {
		try {
			List<OrderList> info = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM donhang WHERE MaDH=?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				info.add(new OrderList(rs.getString("MaDH"),
						rs.getString("HoTen"),
										rs.getString("SDT"),
										rs.getString("TrangThai"),
										rs.getDouble("ThanhTien"),
										rs.getDate("NgayLap")
						));
				          
							          
			}
			stmt.close();
			conn.close();
			return info;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	public static void main(String[] args) {
		DAOadmin dao = new DAOadmin();
		
		List<OrderList> a=dao.getinfobystt("Đã Tiếp Nhận");
		System.out.println(a);
	}
}
