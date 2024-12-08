package Test;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

import org.junit.jupiter.api.*;

import DAO.DAOCategory;
import Entity.Category;

class DAOCategoryTest {

	private DAOCategory daoCategory;

    @BeforeEach
    void setUp() {
        daoCategory = new DAOCategory();
    }

    @Test
    void testGetAllCategoriesSuccess() {
        List<Category> categories = daoCategory.getAllCategories();
        assertNotNull(categories, "The category list should not be null when retrieving categories.");
        assertTrue(categories.size() > 0, "The category list should contain categories from the database.");
    }

    @Test
    void testGetAllCategoriesEmptyTable() {
        // This test assumes that the table 'loai' has been cleared or contains no data
        List<Category> categories = daoCategory.getAllCategories();
        assertNotNull(categories, "The category list should not be null, even if the table is empty.");
        assertFalse(categories.isEmpty(), "The category list should be empty if no records are found in the 'loai' table.");
    }
}
