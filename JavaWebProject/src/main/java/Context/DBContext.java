package Context;

import java.sql.*;

public class DBContext {
	private static String url = "jdbc:mysql://localhost:3306/webprojectdb";
	private static String username = "root";
	private static String password = "";
	
	public static Connection getConnection() {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			return DriverManager.getConnection(url, username, password);
		} catch (Exception ex) {
			// TODO: handle exception
			System.out.println("ERROR: " + ex.getMessage());
		}
		return null;
	}
	
	public static void main(String[] args) {
		Connection conn = DBContext.getConnection();
		System.out.println(conn);
	}
}
