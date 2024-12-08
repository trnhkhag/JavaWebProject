package Test;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

import DAO.DAOProduct;
import Entity.Product;

class DAOProductTest {

	@Test
	public void testInsertProduct() {
	    DAOProduct daoProduct = new DAOProduct();
	    Product product = new Product(0, "Test Product", 99.99, "test.jpg", 100, 1, "Test Brand", "Test Description", 1);
	    boolean result = daoProduct.insert(product);
	    assertTrue(result, "The product should be inserted successfully.");
	}
	
	@Test
	public void testGetProductById() {
	    DAOProduct daoProduct = new DAOProduct();
	    Product product = daoProduct.getProductById(58); // Assuming product with ID 58 exists in the database.
	    assertNotNull(product, "Product should not be null.");
	    assertEquals(58, product.getId(), "The product ID should match.");
	}

	@Test
	public void testGetProductByFilter() {
	    DAOProduct daoProduct = new DAOProduct();
	    List<String> categories = Arrays.asList("1", "2");
	    List<String> brands = Arrays.asList("Casio", "Rolex");
	    List<Product> products = daoProduct.getProductByFilter(categories, brands, 1000.0, 10000.0, 1);

	    assertNotNull(products, "The product list should not be null.");
	    assertFalse(products.isEmpty(), "The product list should contain matching products.");
	}

	@Test
	public void testGetAllProductWithCategory() {
	    DAOProduct daoProduct = new DAOProduct();
	    List<Product> products = daoProduct.getAllProductWithCategory();

	    assertNotNull(products, "The product list should not be null.");
	    assertFalse(products.isEmpty(), "The product list should not be empty.");
	}

	@Test
	public void testUpdateProduct() {
	    DAOProduct daoProduct = new DAOProduct();
	    Product product = new Product(0, "Updated Product", 150.0, "updated.jpg", 50, 1, "Updated Brand", "Updated Description", 1);
	    boolean result = daoProduct.update(product, 58); // Assuming product with ID 58 exists.
	    assertTrue(result, "The product should be updated successfully.");
	}

	@Test
	public void testStopSelling() {
	    DAOProduct daoProduct = new DAOProduct();
	    boolean result = daoProduct.stopSelling(58); // Assuming product with ID 58 exists.
	    assertTrue(result, "The product should be marked as not for sale.");
	}

	@Test
	public void testGetNoOfFilteredProducts() {
	    DAOProduct daoProduct = new DAOProduct();
	    List<String> categories = Arrays.asList("1");
	    List<String> brands = Arrays.asList("Casio");
	    int count = daoProduct.getNoOfFilteredProducts(categories, brands, 100.0, 500.0);

	    assertTrue(count >= 0, "The count of filtered products should be non-negative.");
	}

}
