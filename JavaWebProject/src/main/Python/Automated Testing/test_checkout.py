import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://localhost:8080/JavaWebProject/Home'

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def login(driver):
    driver.get(link)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[3]/a').click()
    driver.find_element(By.ID, 'username').send_keys('khang123')
    driver.find_element(By.ID, 'password').send_keys('12345678')
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[4]/button[2]').click()
    
def test_valid_checkout(driver):
    login(driver)
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[1]/div/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[1]/div/div/div[2]/div/a[2]').click()
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a').click()
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/div[1]/div/div/label/input').click()
    assert 'Home' in driver.current_url