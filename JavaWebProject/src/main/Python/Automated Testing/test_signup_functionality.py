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

url_success = "http://localhost:8080/JavaWebProject/login1.jsp"
msg_without_username = "Username is required."
msg_invalid_email = "Please enter a valid email address."
msg_invalid_phone = "Please enter a valid 10-digit phone number."
msg_without_password = "Password must be at least 6 characters long."
msg_pass_not_match = "Passwords do not match."
msg_account_exits = "Username already exists."
msg_email_exits = "Email already exists."
msg_phone_exits = "Phone already exists."

def register(driver, username, email, phone, password, confirmpassword):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/a").click()
    time.sleep(1)
    driver.find_element(By.ID, "user").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys(email)
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys(phone)
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID,"confpass").send_keys(confirmpassword)
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[6]/input[2]").click()
    time.sleep(1)

def test_register_success(driver):
    register(driver, "duongtooaaasss", "dongduongg@gmail.com", "0334445556", "123456", "123456")
    assert url_success in get_current_url(driver)

def test_register_without_username(driver):
    register(driver, "", "dongduong@gmail.com", "0334445556", "123456", "123456")
    assert msg_without_username in get_error_message(driver)

def test_register_invalid_email(driver):
    register(driver, "duongtoo", "dongduonggmailcom", "0334445556", "123456", "123456")
    assert msg_invalid_email in get_error_message(driver)

def test_register_invalid_phone(driver):
    register(driver, "duongtoo", "duong0023@gmail.com", "0334445556a", "123456", "123456")
    assert msg_invalid_phone in get_error_message(driver)

def test_register_without_password(driver):
    register(driver, "duongtoo", "duong0023@gmail.com", "0334445556", "", "123456")
    assert msg_without_password in get_error_message(driver)

def test_register_password_not_match(driver):
    register(driver, "duongtoo", "duong0023@gmail.com", "0334445556", "123456", "111111")
    assert msg_pass_not_match in get_error_message(driver)

def test_register_account_exits(driver): 
    register(driver, "duong", "dongduongg@gmail.com", "0334445556", "123456", "123456")
    assert msg_account_exits in get_error_valid(driver)

def test_register_email_exits(driver): 
    register(driver, "duongtoo321", "dongduongg@gmail.com", "0334445556", "123456", "123456")
    assert msg_email_exits in get_error_valid(driver)

def test_register_phone_exits(driver): 
    register(driver, "dongduong11321", "dongduongg1@gmail.com", "0334445556", "123456", "123456")
    assert msg_phone_exits in get_error_valid(driver)

def get_error_valid(driver):
    return driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text

def get_error_message(driver):
    return driver.find_element(By.ID, "swal2-html-container").text
    
def get_current_url(driver):
    return driver.current_url