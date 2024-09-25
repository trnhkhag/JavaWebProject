package DAO;

import java.sql.*;
import Entity.Product;
import Context.DBContext;
import java.util.*;

public class DAOProduct {
	private final int limit = 8;
	
	public boolean insert(Product product) {
		try {
			Connection conn = DBContext.getConnection();
			String sql = "INSERT INTO sanpham (TenSP, Gia, Hinh, LuongTon, TrangThai, Hang, MoTa, MaLoai) VALUES(?, ?, ?, ?, ?, ?, ?, ?)";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, product.getName());
			stmt.setDouble(2, product.getPrice());
			stmt.setString(3, product.getImage());
			stmt.setInt(4, product.getStock());
			stmt.setInt(5, product.getStatus());
			stmt.setString(6, product.getBrand());
			stmt.setString(7, product.getDesc());
			stmt.setInt(8, product.getCateId());
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
	
	public Product getProductById(int id) {
		try {
			Product p = null;
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM sanpham WHERE MaSP = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, id);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				p = new Product(rs.getInt("MaSP"), 
							    rs.getString("TenSP"), 
							    rs.getDouble("Gia"),
							    rs.getString("Hinh"), 
							    rs.getInt("LuongTon"), 
							    rs.getInt("TrangThai"), 
							    rs.getString("Hang"), 
							    rs.getString("MoTa"), 
							    rs.getInt("MaLoai"));
			}
			stmt.close();
			conn.close();
			return p;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public List<Product> getProductByFilter(List<String> categories, List<String> brands, double minPrice, double maxPrice, int page) {
		try {
			List<Product> plist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM sanpham";
			int i = 0;
			if (categories.size() > 0 || brands.size() > 0 || minPrice > 0 || maxPrice > 0) {
				sql += " WHERE ";
			}
			if (categories.size() > 0) {
				sql += "MaLoai in (";
				for (i = 0; i < categories.size() - 1; i++) {
					 sql += categories.get(i) + ", ";
				}
				sql += categories.get(i) + ")";
				if (brands.size() > 0) {
					sql += " AND ";
				}
				else if (minPrice > 0) {
					sql += " AND ";
				}
				else if (maxPrice > 0) {
					sql += " AND ";
				}
			}
			
			if (brands.size() > 0) {
				sql += "Hang in (";
				for (i = 0; i < brands.size() - 1; i++) {
					sql += "'" + brands.get(i) + "', ";
				}
				sql += "'" + brands.get(i) + "')";
				if (minPrice > 0) {
					sql += " AND ";
				}
				else if (maxPrice > 0) {
					sql += " AND ";
				}
			}
			if (minPrice > 0) {
				sql += "Gia >= " + minPrice;
				if (maxPrice > 0) {
					sql += " AND ";
				}
			}
			if (maxPrice > 0) {
				sql += "Gia <= " + maxPrice;
			}
			PreparedStatement stmt = conn.prepareStatement(sql + " LIMIT ?,?");
			stmt.setInt(1, limit * (page - 1));
			stmt.setInt(2, limit);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				plist.add(new Product(rs.getInt("MaSP"), 
							          rs.getString("TenSP"), 
							          rs.getDouble("Gia"),
							          rs.getString("Hinh"), 
							          rs.getInt("LuongTon"), 
							          rs.getInt("TrangThai"), 
							          rs.getString("Hang"), 
							          rs.getString("MoTa"), 
							          rs.getInt("MaLoai")));
			}
			stmt.close();
			conn.close();
			return plist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public Product getProduct(String id) {
		try {
			Product p = new Product();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM sanpham WHERE MaSP = " + id;
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				p = new Product(rs.getInt("MaSP"), 
				          rs.getString("TenSP"), 
				          rs.getDouble("Gia"),
				          rs.getString("Hinh"), 
				          rs.getInt("LuongTon"), 
				          rs.getInt("TrangThai"), 
				          rs.getString("Hang"), 
				          rs.getString("MoTa"), 
				          rs.getInt("MaLoai"));
			}
			stmt.close();
			conn.close();
			return p;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public List<Product> getAllProductWithCategory() {
		try {
			List<Product> plist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM sanpham JOIN loai on sanpham.MaLoai = loai.MaLoai";
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				plist.add(new Product(rs.getInt("MaSP"), 
							          rs.getString("TenSP"), 
							          rs.getDouble("Gia"),
							          rs.getString("Hinh"), 
							          rs.getInt("LuongTon"), 
							          rs.getInt("TrangThai"), 
							          rs.getString("Hang"), 
							          rs.getString("MoTa"), 
							          rs.getInt("MaLoai"),
							          rs.getString("TenLoai")));
			}
			stmt.close();
			conn.close();
			return plist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public List<Product> getAllProduct(int page) {
		try {
			List<Product> plist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM sanpham WHERE TrangThai = 1 LIMIT ?, ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, limit * (page - 1));
			stmt.setInt(2, limit);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				plist.add(new Product(rs.getInt("MaSP"), 
							          rs.getString("TenSP"), 
							          rs.getDouble("Gia"),
							          rs.getString("Hinh"), 
							          rs.getInt("LuongTon"), 
							          rs.getInt("TrangThai"), 
							          rs.getString("Hang"), 
							          rs.getString("MoTa"), 
							          rs.getInt("MaLoai")));
			}
			stmt.close();
			conn.close();
			return plist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public List<Product> getProductInCategory(String cid, int page) {
		try {
			List<Product> plist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM sanpham WHERE MaLoai = " + cid + " LIMIT ?, ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, limit * (page - 1));
			stmt.setInt(2, limit);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				plist.add(new Product(rs.getInt("MaSP"), 
							          rs.getString("TenSP"), 
							          rs.getDouble("Gia"),
							          rs.getString("Hinh"), 
							          rs.getInt("LuongTon"), 
							          rs.getInt("TrangThai"), 
							          rs.getString("Hang"), 
							          rs.getString("MoTa"), 
							          rs.getInt("MaLoai")));
			}
			stmt.close();
			conn.close();
			return plist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public int getNoOfProductInCategory(String cid) {
		try {
			int result = 0;
			Connection conn = DBContext.getConnection();
			String sql = "SELECT COUNT(MaSP) FROM sanpham WHERE MaLoai = " + cid;
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				result = rs.getInt(1);
			}
			stmt.close();
			conn.close();
			return result;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return 0;
	}
	
	public List<Product> getFirstNProduct(int n) {
		try {
			List<Product> plist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM sanpham WHERE TrangThai = 1 LIMIT " + n;
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				plist.add(new Product(rs.getInt("MaSP"), 
							          rs.getString("TenSP"), 
							          rs.getDouble("Gia"),
							          rs.getString("Hinh"), 
							          rs.getInt("LuongTon"), 
							          rs.getInt("TrangThai"), 
							          rs.getString("Hang"), 
							          rs.getString("MoTa"), 
							          rs.getInt("MaLoai")));
			}
			stmt.close();
			conn.close();
			return plist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public List<Product> searchProduct(String input, int page) {
		try {
			List<Product> plist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT * FROM sanpham WHERE TenSP LIKE '%" + input + "%' LIMIT ?,?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, limit * (page - 1));
			stmt.setInt(2, limit);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				plist.add(new Product(rs.getInt("MaSP"), 
							          rs.getString("TenSP"), 
							          rs.getDouble("Gia"),
							          rs.getString("Hinh"), 
							          rs.getInt("LuongTon"), 
							          rs.getInt("TrangThai"), 
							          rs.getString("Hang"), 
							          rs.getString("MoTa"), 
							          rs.getInt("MaLoai")));
			}
			stmt.close();
			conn.close();
			return plist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public int getNoOfSearchProduct(String input) {
		try {
			int result = 0;
			Connection conn = DBContext.getConnection();
			String sql = "SELECT COUNT(MaSP) FROM sanpham WHERE TenSP LIKE '%" + input + "%'";
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				result = rs.getInt(1);
			}
			stmt.close();
			conn.close();
			return result;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return 0;
	}
	
	public int getNoOfAllProduct() {
		try {
			int result = 0;
			Connection conn = DBContext.getConnection();
			String sql = "SELECT COUNT(MaSP) AS SoSP FROM sanpham";
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			if (rs.next()) {
				result = rs.getInt("SoSP");
			}
			stmt.close();
			conn.close();
			return result;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return 0;
	}
	
	public List<String> getAllBrand() {
		try {
			List<String> blist = new ArrayList<>();
			Connection conn = DBContext.getConnection();
			String sql = "SELECT DISTINCT Hang FROM sanpham";
			PreparedStatement stmt = conn.prepareStatement(sql);
			ResultSet rs = stmt.executeQuery();
			while (rs.next()) {
				blist.add(rs.getString("Hang"));
			}
			stmt.close();
			conn.close();
			return blist;
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public boolean update(Product product, int pid) {
		try {
			boolean isUpdated = false;
			Connection conn = DBContext.getConnection();
			String sql = "UPDATE sanpham SET TenSP = ?, MaLoai = ?, LuongTon = ?, TrangThai = ?, Gia = ?, Hang = ?, MoTa = ? WHERE MaSP = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setString(1, product.getName());
			stmt.setInt(2, product.getCateId());
			stmt.setInt(3, product.getStock());
			stmt.setInt(4, product.getStatus());
			stmt.setDouble(5, product.getPrice());
			stmt.setString(6, product.getBrand());
			stmt.setString(7, product.getDesc());
			stmt.setInt(8, pid);
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
	
	public boolean stopSelling(int id) {
		try {
			boolean isUpdated = false;
			Connection conn = DBContext.getConnection();
			String sql = "UPDATE sanpham SET TrangThai = 0 WHERE MaSP = ?";
			PreparedStatement stmt = conn.prepareStatement(sql);
			stmt.setInt(1, id);
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
	
	public static void main(String[] args) {
		DAOProduct dao = new DAOProduct();
		System.out.println(dao.getAllProduct(1));
//		List<String> categories = new ArrayList<>();
//		categories.add("1");
//		List<String> brands = new ArrayList<>();
//		brands.add("Casio");
//		System.out.println(dao.getProductByFilter(categories, brands, 100, 500));
	}
}
