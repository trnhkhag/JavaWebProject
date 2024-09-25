package Entity;

public class Order {
	int id;
	String date;
	String status;
	double total;
	int userId;
	
	public Order(String date, double total, int userId) {
		super();
		this.date = date;
		status = "Waiting";
		this.total = total;
		this.userId = userId;
	}


	public Order(int id, String date, String status, double total, int userId) {
		super();
		this.id = id;
		this.date = date;
		this.status = status;
		this.total = total;
		this.userId = userId;
	}


	public int getId() {
		return id;
	}


	public void setId(int id) {
		this.id = id;
	}


	public String getDate() {
		return date;
	}


	public void setDate(String date) {
		this.date = date;
	}


	public String getStatus() {
		return status;
	}


	public void setStatus(String status) {
		this.status = status;
	}


	public double getTotal() {
		return total;
	}


	public void setTotal(double total) {
		this.total = total;
	}


	public int getUserId() {
		return userId;
	}


	public void setUserId(int userId) {
		this.userId = userId;
	}


	@Override
	public String toString() {
		return "Order [id=" + id + ", date=" + date + ", status=" + status + ", total=" + total + ", userId=" + userId
				+ "]";
	}
}
