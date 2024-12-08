package Test;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

import org.junit.jupiter.api.*;

import DAO.DAOOrderDetail;
import Entity.Order;
import Entity.OrderDetail;
class DAOOrderDetailTest {

	private DAOOrderDetail daoOrderDetail;
	private OrderDetail orderDetail_1;
	private OrderDetail orderDetail_2;
	@BeforeEach
	void setUp() {
		daoOrderDetail = new DAOOrderDetail();
	}

//	@Test
//	void testInsert() {
//		orderDetail_1 = new OrderDetail(30, 55, 1, 9280);
//		orderDetail_2 = new OrderDetail(30, 54, 1, 18980);
//		boolean isInsert_1 = daoOrderDetail.insert(orderDetail_1);
//		boolean isInsert_2 = daoOrderDetail.insert(orderDetail_2);
//		assertTrue(isInsert_1 && isInsert_2, "The order should be inserted successfully into the database.");
//	}
//	
	@Test
	void testGetAllOrderDetails() {
		List<OrderDetail> oderDetail_id48 = daoOrderDetail.getAllOrderDetails(48);
		
		assertNotNull(oderDetail_id48, "The Order Detail list should not be null");
		assertTrue(oderDetail_id48.size()>0, "The Order Detail list should not be empty if id exist");
	}
	
	@Test
	void testGetAllOrderDetailsWithNonExistentId() {
		List<OrderDetail> oderDetail_id1 = daoOrderDetail.getAllOrderDetails(1);
		
		assertNotNull(oderDetail_id1, "The Order Detail list should not be null");
		assertFalse(oderDetail_id1.size()>0, "The Order Detail list should not be empty if id not exist");
	}
}
