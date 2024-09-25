package Entity;

public class Product {
	private int id;
	private String name;
	private double price;
	private String image;
	private int stock;
	private int status;
	private String brand;
	private String desc;
	private int cateId;
	private String category;
	private int quantity;
	
	public Product() {}
	
	public Product(String name, String image, String desc) {
		super();
		this.name = name;
		this.image = image;
		this.desc = desc;
	}
	
	public Product(String name, double price, int stock, int status, String brand, String desc,
			int cateId) {
		super();
		this.name = name;
		this.price = price;
		this.stock = stock;
		this.status = status;
		this.brand = brand;
		this.desc = desc;
		this.cateId = cateId;
		quantity = 1;
	}

	public Product(String name, double price, String image, int stock, int status, String brand, String desc,
			int cateId) {
		super();
		this.name = name;
		this.price = price;
		this.image = image;
		this.stock = stock;
		this.status = status;
		this.brand = brand;
		this.desc = desc;
		this.cateId = cateId;
		quantity = 1;
	}

	public Product(int id, String name, double price, String image, int stock, int status, String brand,
			String desc, int cateId) {
		super();
		this.id = id;
		this.name = name;
		this.price = price;
		this.image = image;
		this.stock = stock;
		this.status = status;
		this.brand = brand;
		this.desc = desc;
		this.cateId = cateId;
		quantity = 1;
	}
	
	public Product(int id, String name, double price, String image, int stock, int status, String brand,
			String desc, int cateId, String category) {
		super();
		this.id = id;
		this.name = name;
		this.price = price;
		this.image = image;
		this.stock = stock;
		this.status = status;
		this.brand = brand;
		this.desc = desc;
		this.cateId = cateId;
		this.category = category;
		quantity = 1;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

	public String getImage() {
		return image;
	}

	public void setImage(String image) {
		this.image = image;
	}

	public int getStock() {
		return stock;
	}

	public void setStock(int stock) {
		this.stock = stock;
	}

	public int getStatus() {
		return status;
	}

	public void setStatus(int status) {
		this.status = status;
	}

	public String getBrand() {
		return brand;
	}

	public void setBrand(String brand) {
		this.brand = brand;
	}

	public String getDesc() {
		return desc;
	}

	public void setDesc(String desc) {
		this.desc = desc;
	}

	public int getCateId() {
		return cateId;
	}

	public void setCateId(int cateId) {
		this.cateId = cateId;
	}

	public String getCategory() {
		return category;
	}

	public void setCategory(String category) {
		this.category = category;
	}

	public int getQuantity() {
		return quantity;
	}

	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}

	@Override
	public String toString() {
		return "Product [id=" + id + ", name=" + name + ", price=" + price + ", image=" + image + ", stock=" + stock
				+ ", status=" + status + ", brand=" + brand + ", desc=" + desc + ", cateId=" + cateId + ", category="
				+ category + "]";
	}
	
	@Override
	public boolean equals(Object obj) {
		// TODO Auto-generated method stub
		Product p = (Product) obj;
		return (p.getId() == this.id);
	}
}
