package DAO;

import java.sql.*;
import Context.DBContext;
import Entity.User;
import java.util.*;

public class DAOUser {
	public boolean insert(User user) {
		try {
			Connection conn = DBContext.getConnection();
			Statement stmt = conn.createStatement();
			String sql = "INSERT INTO nguoidung (TenDangNhap, MatKhau, email, SoDienThoai, role) VALUES(";
			sql += "'" + user.getUsername() + "', '";
			sql += user.getPassword() + "', '";
			sql += user.getEmail() + "', '";
			sql += user.getPhone() + "', '";
			sql += user.getRole() + "');";
			if (stmt.executeUpdate(sql) > 0) {
				stmt.close();
				conn.close();
				return true;
			}
		} catch (Exception ex) {
			// TODO: handle exception
			ex.printStackTrace();
		}
		return false;
	}
	
	public boolean delete(int id) {
		try {
			Connection conn = DBContext.getConnection();
			Statement stmt = conn.createStatement();
			String sql = "DELETE FROM nguoidung WHERE MaNguoiDung = " + id;
			boolean isDeleted = false;
			if (stmt.executeUpdate(sql) > 0) {
				isDeleted = true;
			}
			stmt.close();
			conn.close();
			return isDeleted;
		} catch (Exception ex) {
			// TODO: handle exception
			ex.printStackTrace();
		}
		return false;
	}
	
//	public boolean update(int id, User newUser) {
//		try {
//			Connection conn = DBConnection.getConnection();
//			Statement stmt = conn.createStatement();
//			String sql = "UPDATE nguoidung SET ";
//			sql += "MaNguoiDung = " + newUser.getId();
//			sql += ", HoTen = " + newUser.getFullname();
//			sql += ", TenDangNhap = " + newUser.getUsername();
//			sql += ", MatKhau = " + newUser.getPassword();
//			sql += ", email = " + newUser.getEmail();
//			sql += ", SoDienThoai = " + newUser.getPhone();
//			sql += ", DiaChi = " + newUser.getAddress();
//			sql += ", role = " + newUser.getRole();
//		} catch (Exception ex) {
//			// TODO: handle exception
//			ex.printStackTrace();
//		}
//	}
	
	public boolean check(String username, String password) {
		try {
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM nguoidung WHERE TenDangNhap = ? AND MatKhau = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, username);
			stmt.setString(2, password);
			ResultSet rs = stmt.executeQuery();
			boolean isExist = false;
			if (rs.next()) {
				isExist = true;
			}
			stmt.close();
			conn.close();
			return isExist;
		} catch (Exception ex) {
			// TODO: handle exception
			ex.printStackTrace();
		}
		return false;
	}
	
	public User getUser(String username, String password) {
		try {
			User user = null;
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM nguoidung WHERE TenDangNhap = ? AND MatKhau = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, username);
			stmt.setString(2, password);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				user = new User(rs.getInt("MaNguoiDung"), 
						        rs.getString("HoTen"), 
						        rs.getString("TenDangNhap"), 
						        rs.getString("MatKhau"), 
						        rs.getString("Email"), 
						        rs.getString("SoDienThoai"), 
						        rs.getString("DiaChi"), 
						        rs.getString("Role"));
			}
			stmt.close();
			conn.close();
			return user;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public boolean update(int id, String username, String password, String email, String phone, String role) {
		try {
			boolean isUpdated = false;
			Connection conn = DBContext.getConnection();
			String sql = "UPDATE nguoidung SET TenDangNhap = ?, MatKhau = ?, Email = ?, SoDienThoai = ?, Role = ? WHERE MaNguoiDung = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, username);
			stmt.setString(2, password);
			stmt.setString(3, email);
			stmt.setString(4, phone);
			stmt.setString(5, role);
			stmt.setInt(6, id);
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
	
	public boolean update(String username, String fullname, String email, String address, String phone) {
		try {
			boolean isUpdated = false;
			Connection conn = DBContext.getConnection();
			String sql = "UPDATE nguoidung SET HoTen = ?, Email = ?, DiaChi = ?, SoDienThoai = ? WHERE TenDangNhap = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, fullname);
			stmt.setString(2, email);
			stmt.setString(3, address);
			stmt.setString(4, phone);
			stmt.setString(5, username);
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
	
	public boolean update(String email, String password) {
		try {
			boolean isUpdated = false;
			Connection conn = DBContext.getConnection();
			String sql = "UPDATE nguoidung SET MatKhau = ? WHERE Email = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, password);
			stmt.setString(2, email);
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
	
	public boolean isUsernameExist(String username) {
		try {
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM nguoidung WHERE TenDangNhap = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, username);
			ResultSet rs = stmt.executeQuery();
			boolean isExist = false;
			if (rs.next()) {
				isExist = true;
			}
			stmt.close();
			conn.close();
			return isExist;
		} catch (Exception ex) {
			// TODO: handle exception
			ex.printStackTrace();
		}
		return false;
	}
	
	public boolean isEmailExist(String email) {
		try {
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM nguoidung WHERE Email = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, email);
			ResultSet rs = stmt.executeQuery();
			boolean isExist = false;
			if (rs.next()) {
				isExist = true;
			}
			stmt.close();
			conn.close();
			return isExist;
		} catch (Exception ex) {
			// TODO: handle exception
			ex.printStackTrace();
		}
		return false;
	}
	
	public User getUserByUsername(String username) {
		try {
			User user = null;
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM nguoidung WHERE TenDangNhap = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, username);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				user = new User(rs.getInt("MaNguoiDung"),
								rs.getString("HoTen"), 
						        rs.getString("TenDangNhap"), 
						        rs.getString("MatKhau"), 
						        rs.getString("Email"), 
						        rs.getString("SoDienThoai"), 
						        rs.getString("DiaChi"),
						        rs.getString("Role"));
			}
			stmt.close();
			conn.close();
			return user;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public User getUserById(int id) {
		try {
			User user = null;
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM nguoidung WHERE MaNguoiDung = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, id);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				user = new User(rs.getInt("MaNguoiDung"),
								rs.getString("HoTen"), 
						        rs.getString("TenDangNhap"), 
						        rs.getString("MatKhau"), 
						        rs.getString("Email"), 
						        rs.getString("SoDienThoai"), 
						        rs.getString("DiaChi"),
						        rs.getString("Role"));
			}
			stmt.close();
			conn.close();
			return user;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public List<User> getAllUsers() {
		try {
			List<User> ulist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM nguoidung";
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				ulist.add(new User(rs.getInt("MaNguoiDung"),
								   rs.getString("HoTen"), 
							       rs.getString("TenDangNhap"), 
							       rs.getString("MatKhau"), 
							       rs.getString("Email"), 
							       rs.getString("SoDienThoai"), 
							       rs.getString("DiaChi"), 
							       rs.getString("Role")));
			}
			stmt.close();
			conn.close();
			return ulist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public static void main(String[] args) {
		DAOUser dao = new DAOUser();
		System.out.println(dao.getUser("khang", "12345678"));
	}
}
