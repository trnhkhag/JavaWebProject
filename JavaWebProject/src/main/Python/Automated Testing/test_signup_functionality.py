import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
# Website home page url
web_url = "http://localhost:8080/JavaWebProject/Home"

def test_register_success(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "user").send_keys("duonggtoo")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("dongduongg@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("0334445556")
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)
    assert "http://localhost:8080/JavaWebProject/login1.jsp" in get_current_url(driver)

def test_register_without_username(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("dongduong@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("0334445556")
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)
    assert "Username is required." in get_error_message(driver)

def test_register_invalid_email(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "user").send_keys("duongtoo")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("dongduonggmailcom")
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("0334445556")
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)
    assert "Please enter a valid email address." in get_error_message(driver)

def test_register_invalid_phone(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "user").send_keys("duongtoo")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("duong0023@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("0334445556a")
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)
    assert "Please enter a valid 10-digit phone number." in get_error_message(driver)

def test_register_without_password(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "user").send_keys("duongtoo")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("duong0023@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("0334445556")
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)
    assert "Password must be at least 6 characters long." in get_error_message(driver)
def test_register_password_not_match(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "user").send_keys("duongtoo")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("duong0023@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("0334445556")
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys("1234567")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)
    assert "Passwords do not match." in get_error_message(driver)

def test_register_account_exits(driver): 
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "user").send_keys("duonggtoo")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("dongduongg@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("0334445556")
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)
    error_msg = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text
    assert "Username already exists." in error_msg

def test_register_email_exits(driver): 
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "user").send_keys("dongduong")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("dongduongg@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("0123456789")
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)
    error_msg = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text
    assert "Email already exists." in error_msg

def test_register_phone_exits(driver): 
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "user").send_keys("dongduong11")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("dongduongg1@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("0334445556")
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)
    error_msg = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text
    assert "Phone already exists." in error_msg

def get_error_message(driver):
    return driver.find_element(By.ID, "swal2-html-container").text
    
def get_current_url(driver):
    return driver.current_url
