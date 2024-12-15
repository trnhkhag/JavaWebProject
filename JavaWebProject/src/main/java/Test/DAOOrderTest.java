package Test;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import org.junit.jupiter.api.*;

import DAO.DAOOrder;
import Entity.Order;

class DAOOrderTest {
	
	private DAOOrder daoOrder;
	private Order order;
	
	
	@BeforeEach
	void setUp() {
        daoOrder = new DAOOrder();
        
    }
	
	@Test
	void testInsert() {
		order = new Order("2024-10-13", 28260, 49);
		boolean isInserted = daoOrder.insert(order);
		assertTrue(isInserted, "The order should be inserted successfully into the database.");
	}
	
	@Test 
	void testLatestOrderId () {
		int id = daoOrder.getLatestOrderId();
		
		assertEquals(17, id, "The latest order ID should match the expected value.");
	}
	
	@Test 
	void TestGetAllOrdersSuccess() {
		List<Order> oderList_id48 = daoOrder.getAllOrders(48);

		assertNotNull(oderList_id48, "The order list should not be null");
		assertTrue(oderList_id48.size()>0, "The order list should not be empty if id exist");
		
		
	}
	
	@Test
	void testGetAllOrdersWithNonExistentId() {
		List<Order> oderList_id1 = daoOrder.getAllOrders(1);
		
		assertFalse(oderList_id1.size()>0, "The order list should be empty if id not exist");
		assertNotNull(oderList_id1, "The order list should not be null, even if the table is empty.");
	}
	
	@Test
	void TestGetStatistical() {
		double valid_statistical = daoOrder.getStatistical(5, 2023);
		double invalid_statistical = daoOrder.getStatistical(0, 2024);
		
		assertEquals(13380, valid_statistical);
		assertEquals(0, invalid_statistical);
	}
}
