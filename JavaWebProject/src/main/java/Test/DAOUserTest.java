package Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;
import java.util.List;

import Entity.User;
import DAO.DAOUser;

public class DAOUSERTest {
    private DAOUser daoUser;

    @BeforeEach
    public void setUp() {
        daoUser = new DAOUser();
    }

    @Test
    public void testInsert() {
    	User user = new User("tommy", "123456", "admin@gmail.com", "0311233211", "Customer");
        boolean result = daoUser.insert(user);
//        System.out.println("Insert result: " + result);
	        assertTrue(result, "Insert user should return true if the insertion is successful");
	        
    }

   @Test
   public void testInsertInvalidUser() {
       User invalidUser = new User("", "12345", "invalid-email", "12345", "InvalidRole");
       boolean result = daoUser.insert(invalidUser);
       assertFalse(result, "Insert should return false if the user data is invalid");
   }

    @Test
    public void testDelete() {
        int userId = 50; 
        boolean result = daoUser.delete(userId);
        assertTrue(result, "Delete should return true if the deletion is successful");
    }
    
    @Test
    public void testDeleteNonExistentUser() {
        int nonExistentUserId = 99999; 
        boolean result = daoUser.delete(nonExistentUserId);
        assertFalse(result, "Delete should return false if the user ID does not exist");
    }

    @Test
    public void testCheckValidUser() {
        String username = "khang";
        String password = "12345678";
        boolean result = daoUser.check(username, password);
        assertTrue(result, "Check should return true if the user exists");
    }

    @Test
    public void testCheckInvalidUser() {
        String username = "invalidUser";
        String password = "invalidPass";
        boolean result = daoUser.check(username, password);
        assertFalse(result, "Check should return false if the user does not exist");
    }
    
    @Test
    public void testCheckInvalidPassword() {
        String username = "khang";
        String invalidPassword = "wrongPassword";
        boolean result = daoUser.check(username, invalidPassword);
        assertFalse(result, "Check should return false if the password is incorrect");
    }

    @Test
    public void testGetUserByValidCredentials() {
        String username = "khang";
        String password = "12345678";
        User user = daoUser.getUser(username, password);
        assertNotNull(user, "GetUser should return a User object if the credentials are valid");
        assertEquals(username, user.getUsername());
    }

    @Test
    public void testGetUserByInvalidCredentials() {
        String username = "invalidUser";
        String password = "invalidPass";
        User user = daoUser.getUser(username, password);
        assertNull(user, "GetUser should return null if the credentials are invalid");
    }

    @Test
    public void testUpdate() {
        int userId = 52; 
        String newUsername = "duongUpdated";
        String newPassword = "00000000";
        String newEmail = "hihi@gmail.com";
        String newPhone = "0987654321";
        String newRole = "admin";

        boolean result = daoUser.update(userId, newUsername, newPassword, newEmail, newPhone, newRole);
        assertTrue(result, "Update should return true if the update is successful");
        
        User updatedUser = daoUser.getUserById(userId);
        assertEquals(newUsername, updatedUser.getUsername(), "Username should be updated");
        assertEquals(newPassword, updatedUser.getPassword(), "Password should be updated");
        assertEquals(newEmail, updatedUser.getEmail(), "Email should be updated");
        assertEquals(newPhone, updatedUser.getPhone(), "Phone should be updated");
        assertEquals(newRole, updatedUser.getRole(), "Role should be updated");
        
    }
    
    @Test
    public void testUpdateWithoutChanges() {
        int userId = 52; 
        String username = "khang"; // Same as current value
        String password = "12345678"; // Same as current value
        String email = "khang@gmail.com"; // Same as current value
        String phone = "0987654321"; // Same as current value
        String role = "user"; // Same as current value

        boolean result = daoUser.update(userId, username, password, email, phone, role);
        assertFalse(result, "Update should return false if no changes were made");
    }
    
    @Test
    public void testIsUsernameExist() {
        String username = "khang";
        boolean result = daoUser.isUsernameExist(username);
        assertTrue(result, "isUsernameExist should return true if the username exists");
    }

    @Test
    public void testGetUserAfterDelete() {
        int deletedUserId = 58; 
        daoUser.delete(deletedUserId);
        User user = daoUser.getUserById(deletedUserId);
        assertNull(user, "GetUser should return null if the user has been deleted");
    }
    
    @Test
    public void testGetAllUsers() {
        List<User> users = daoUser.getAllUsers();
        assertNotNull(users, "GetAllUsers should return a list of users");
        assertTrue(users.size() > 0, "The user list should not be empty");
    }
}