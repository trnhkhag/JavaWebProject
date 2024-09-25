package DAO;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

import Context.DBContext;
import Entity.OrderDetail;
import Entity.Product;

public class DAOOrderDetail {
	public boolean insert(OrderDetail orderDetail) {
		try {
			boolean isUpdated = false;
			Connection conn = DBContext.getConnection();
			String sql = "INSERT INTO chitietdonhang VALUES(?, ?, ?, ?)";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, orderDetail.getOrderId());
			stmt.setInt(2, orderDetail.getProductId());
			stmt.setInt(3, orderDetail.getQuantity());
			stmt.setDouble(4, orderDetail.getPrice());
			if (stmt.executeUpdate() > 0) {
				isUpdated = true;
			}
			stmt.close();
			conn.close();
			return isUpdated;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return false;
	}
	
	public List<OrderDetail> getAllOrderDetails(int userId) {
		try {
			List<OrderDetail> odlist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT od.*, p.* FROM chitietdonhang od JOIN donhang d ON od.MaDH = d.MaDH JOIN sanpham p ON od.MaSP = p.MaSP WHERE MaNguoiDung = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, userId);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				odlist.add(new OrderDetail(rs.getInt("MaDH"), rs.getInt("MaSP"), rs.getInt("SoLuong"), rs.getDouble("DonGia"), new Product(rs.getString("TenSP"), rs.getString("Hinh"), rs.getString("MoTa"))));
			}
			stmt.close();
			conn.close();
			return odlist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public static void main(String[] args) {
		DAOOrderDetail dao = new DAOOrderDetail();
		System.out.println(dao.getAllOrderDetails(36));
	}
}
