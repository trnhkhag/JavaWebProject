package Entity;

import java.sql.Date;

public class OrderList {
	private String madh;
	private String hoten;
	private String user;
	private String email;
	private String sdt;
	private String address;
	private String sanpham;
	private String image;
	private String status;
	private String pmcode;
	private double total;
	private Date date;
	
	public OrderList(String madh, String status, double total, Date date) {
		super();
		this.madh = madh;
		this.status = status;
		this.total = total;
		this.date = date;
	}
	public OrderList(String madh, String hoten, String sdt, String status, double total, Date date) {
		super();
		this.madh = madh;
		this.hoten = hoten;
		this.sdt = sdt;
		this.status = status;
		this.total = total;
		this.date = date;
	}
	public String getMadh() {
		return madh;
	}
	public void setMadh(String madh) {
		this.madh = madh;
	}
	public String getHoten() {
		return hoten;
	}
	public void setHoten(String hoten) {
		this.hoten = hoten;
	}
	public String getUser() {
		return user;
	}
	public void setUser(String user) {
		this.user = user;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getSdt() {
		return sdt;
	}
	public void setSdt(String sdt) {
		this.sdt = sdt;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getSanpham() {
		return sanpham;
	}
	public void setSanpham(String sanpham) {
		this.sanpham = sanpham;
	}
	public String getImage() {
		return image;
	}
	public void setImage(String image) {
		this.image = image;
	}
	public String getStatus() {
		return status;
	}
	public void setStatus(String status) {
		this.status = status;
	}
	public String getPmcode() {
		return pmcode;
	}
	public void setPmcode(String pmcode) {
		this.pmcode = pmcode;
	}
	public double getTotal() {
		return total;
	}
	public void setTotal(double total) {
		this.total = total;
	}
	public Date getDate() {
		return date;
	}
	public void setDate(Date date) {
		this.date = date;
	}
	public static void main(String[] args) {
	}

}
