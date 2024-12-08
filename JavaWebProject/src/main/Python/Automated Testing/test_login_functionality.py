import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
# Website home page url
web_url = "http://localhost:8080/JavaWebProject/Home"

def test_login_success(driver):
    driver.get(web_url)
    status = 1
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys("khang")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("12345678")
    time.sleep(1)
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    if "http://localhost:8080/JavaWebProject/Home" in get_current_url(driver):
        status = 2
    time.sleep(1)
    assert status == 2

def test_login_success_with_rememmberme(driver): 
    driver.get(web_url)
    status = 1
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys("khang")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[3]/input").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    if "http://localhost:8080/JavaWebProject/Home" in get_current_url(driver):
        status = 2
    time.sleep(1)
    assert status == 2

def test_login_without_username(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    assert "Please enter your username." in get_error_message(driver)

def test_login_without_password(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys("khang")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    assert "Please enter your password." in get_error_message(driver)

def test_login_empty(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    assert "Please enter your username." in get_error_message(driver)

def test_login_with_username_not_exist(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys("asdf")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    error_message = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text
    assert "Invalid username or password" in error_message

def test_login_with_wrong_password(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys("khang")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("1234566666")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    error_message = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text
    assert "Invalid username or password" in error_message

def test_login_with_short_password(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys("khang")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("1")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    assert "Password must be at least 6 characters long." in get_error_message(driver)

def test_login_sql_injection_based_on_1_equal_1_isAlwaysTrue(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys("105 OR 1=1")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("105 OR 1=1")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    error_message = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text
    assert "Invalid username or password" in error_message

def test_login_sql_injection_based_on_equal_isAlwaysTrue(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys('" or ""="')
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys('" or ""="')
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    error_message = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text
    assert "Invalid username or password" in error_message

def test_login_sql_injection_based_onBatchedSQLStatements(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys("105; DROP TABLE donhang")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("105; DROP TABLE donhang")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    error_message = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text
    assert "Invalid username or password" in error_message



def test_logout(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys("khang")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    assert "http://localhost:8080/JavaWebProject/Login" in get_current_url(driver)

def get_error_message(driver):
    return driver.find_element(By.ID, "swal2-html-container").text
def get_current_url(driver):
    return driver.current_url