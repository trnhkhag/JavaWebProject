import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
# Website home page url
web_url = "http://localhost:8080/JavaWebProject/Home"

def login(driver, username, password):
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[3]/a').click()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[4]/button[2]').click()
    
def add_to_cart(driver, product):
    actions = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    time.sleep(1)
    actions.move_to_element(product).perform()
    time.sleep(1)
    product.find_element(By.CLASS_NAME, "buy-now").click()
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()

# TC1: Test browsing product 1 by clicking image from home page
def test_product_1_browsing_home_image(driver):
    driver.get(web_url)
    product = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[1]/div/a/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    home_product_name = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[1]/div/div/h3/a').text
    home_product_price = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[1]/div/div/div[1]/div/p/span').text
    time.sleep(5)
    product.click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert home_product_name == detail_product_name and home_product_price == detail_product_price
    
# TC2: Test browsing product 1 by clicking product detail button from home page
def test_product_1_browsing_home_button(driver):
    driver.get(web_url)
    product = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[1]/div/a/div')
    actions = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    home_product_name = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[1]/div/div/h3/a').text
    home_product_price = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[1]/div/div/div[1]/div/p/span').text
    time.sleep(5)
    actions.move_to_element(product).perform()
    driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[1]/div/div/div[2]/div/a[1]').click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert home_product_name == detail_product_name and home_product_price == detail_product_price
    
# TC3: Test browsing product 2 by clicking image from home page
def test_product_2_browsing_home_image(driver):
    driver.get(web_url)
    product = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[5]/div/a/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    home_product_name = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[5]/div/div/h3/a').text
    home_product_price = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[5]/div/div/div[1]/div/p/span').text
    time.sleep(5)
    product.click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert home_product_name == detail_product_name and home_product_price == detail_product_price
    
# TC4: Test browsing product 2 by clicking product detail button from home page
def test_product_2_browsing_home_button(driver):
    driver.get(web_url)
    product = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[5]/div/a/div')
    actions = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    home_product_name = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[5]/div/div/h3/a').text
    home_product_price = driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[5]/div/div/div[1]/div/p/span').text
    time.sleep(5)
    actions.move_to_element(product).perform()
    driver.find_element(By.XPATH, '/html/body/section[4]/div[2]/div/div[5]/div/div/div[2]/div/a[1]').click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert home_product_name == detail_product_name and home_product_price == detail_product_price

# TC5: Test browsing product 1 by clicking image from shop page
def test_product_1_browsing_shop_image(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[1]/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    shop_product_name = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[1]/div/div/h3/a').text
    shop_product_price = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[1]/div/div/div[1]/div/p/span[2]').text
    time.sleep(5)
    product.click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert shop_product_name == detail_product_name and shop_product_price == detail_product_price
    
# TC6: Test browsing product 1 by clicking product detail button from shop page
def test_product_1_browsing_shop_button(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[1]/div')
    actions = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    shop_product_name = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[1]/div/div/h3/a').text
    shop_product_price = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[1]/div/div/div[1]/div/p/span[2]').text
    time.sleep(5)
    actions.move_to_element(product).perform()
    driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[1]/div/div/div[2]/div/a[1]').click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert shop_product_name == detail_product_name and shop_product_price == detail_product_price
    
# TC7: Test browsing product 1 by clicking image from shop page
def test_product_2_browsing_shop_image(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[5]/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    shop_product_name = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[5]/div/div/h3/a').text
    shop_product_price = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[5]/div/div/div[1]/div/p/span[2]').text
    time.sleep(5)
    product.click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert shop_product_name == detail_product_name and shop_product_price == detail_product_price
    
# TC8: Test browsing product 2 by clicking product detail button from shop page
def test_product_2_browsing_shop_button(driver):
    driver.get(web_url)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[5]/div')
    actions = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    shop_product_name = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[5]/div/div/h3/a').text
    shop_product_price = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[5]/div/div/div[1]/div/p/span[2]').text
    time.sleep(5)
    actions.move_to_element(product).perform()
    driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[5]/div/div/div[2]/div/a[1]').click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert shop_product_name == detail_product_name and shop_product_price == detail_product_price
    
# TC9: Test browsing product 1 from cart page
def test_product_1_browsing_cart(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product_1 = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[2]/div')
    product_2 = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[6]/div')
    add_to_cart(driver, product_1)
    add_to_cart(driver, product_2)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    cart_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/div/table/tbody/tr/td[3]/h3').text
    cart_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/div/table/tbody/tr/td[3]/p[2]').text[7:]
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/div/table/tbody/tr/td[2]').click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert cart_product_name == detail_product_name and cart_product_price == detail_product_price
    
# TC10: Test browsing product 2 from cart page
def test_product_2_browsing_cart(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product_1 = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[2]/div')
    product_2 = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[6]/div')
    add_to_cart(driver, product_1)
    add_to_cart(driver, product_2)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    cart_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/div/table/tbody/tr[2]/td[3]/h3').text
    cart_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/div/table/tbody/tr[2]/td[3]/p[2]').text[7:]
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/div/table/tbody/tr[2]/td[2]').click()
    detail_product_name = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/h3').text
    detail_product_price = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[2]/p[1]/span').text
    time.sleep(5)
    assert cart_product_name == detail_product_name and cart_product_price == detail_product_price