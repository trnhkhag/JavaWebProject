package Entity;

public class User {
	private int id;
	private String fullname;
	private String username;
	private String password;
	private String email;
	private String phone;
	private String address;
	private String role;
	
	public User(String username, String password, String email, String phone, String role) {
		super();
		this.username = username;
		this.password = password;
		this.email = email;
		this.phone = phone;
		this.role = role;
	}

	public User(String fullname, String username, String password, String email, String phone, String address,
			String role) {
		super();
		this.fullname = fullname;
		this.username = username;
		this.password = password;
		this.email = email;
		this.phone = phone;
		this.address = address;
		this.role = role;
	}

	public User(int id, String fullname, String username, String password, String email, String phone, String address,
			String role) {
		super();
		this.id = id;
		this.fullname = fullname;
		this.username = username;
		this.password = password;
		this.email = email;
		this.phone = phone;
		this.address = address;
		this.role = role;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getFullname() {
		return fullname;
	}

	public void setFullname(String fullname) {
		this.fullname = fullname;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public String getRole() {
		return role;
	}

	public void setRole(String role) {
		this.role = role;
	}

	@Override
	public String toString() {
		return "User [id=" + id + ", fullname=" + fullname + ", username=" + username + ", password=" + password
				+ ", email=" + email + ", phone=" + phone + ", address=" + address + ", role=" + role + "]";
	}
}
