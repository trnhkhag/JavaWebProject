package Entity;

public class OrderDetail {
	private int orderId;
	private int productId;
	private int quantity;
	private double price;
	private Product product; 
	
	
	public OrderDetail(int orderId, int productId, int quantity, double price) {
		super();
		this.orderId = orderId;
		this.productId = productId;
		this.quantity = quantity;
		this.price = price;
	}


	public OrderDetail(int orderId, int productId, int quantity, double price, Product product) {
		super();
		this.orderId = orderId;
		this.productId = productId;
		this.quantity = quantity;
		this.price = price;
		this.product = product;
	}


	public int getOrderId() {
		return orderId;
	}


	public void setOrderId(int orderId) {
		this.orderId = orderId;
	}


	public int getProductId() {
		return productId;
	}


	public void setProductId(int productId) {
		this.productId = productId;
	}


	public int getQuantity() {
		return quantity;
	}


	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}


	public double getPrice() {
		return price;
	}


	public void setPrice(double price) {
		this.price = price;
	}


	public Product getProduct() {
		return product;
	}


	public void setProduct(Product product) {
		this.product = product;
	}


	@Override
	public String toString() {
		return "OrderDetail [orderId=" + orderId + ", productId=" + productId + ", quantity=" + quantity + ", price="
				+ price + "]";
	}
}
