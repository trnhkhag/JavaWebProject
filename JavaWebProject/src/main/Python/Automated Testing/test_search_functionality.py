import math

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import random
import string

product_names = ["Ceramica", "Aquis", "Chronoris", "Drivers", "Big Crown ProPilot", "Diamaster", "Coupole", "Hyperchrome",
                 "Submariner", "Oyster Perpetual", "Explorer", "Deepsea"]
items_per_page = 8

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def get_total_page():
    return math.ceil(len(product_names) / items_per_page)

def go_to_next_page(driver, index):
    try:
        xpath = f"//a[@href='Shop?page={index}']"
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)
    except Exception as e:
        print(f"Không tìm thấy trang: {e}")
        assert False

def test_search_with_single_lower_character(driver):

    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    random_char = random.choice(string.ascii_lowercase)

    count = sum(1 for name in product_names if random_char.lower() in name.lower())

    driver.find_element(By.XPATH, "//*[@id='right']/form/input").send_keys(random_char)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='right']/form/button").click()
    time.sleep(1)
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(2)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == count

def test_search_with_single_uppercase_character(driver):

    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    random_char = random.choice(string.ascii_uppercase)

    count = sum(1 for name in product_names if random_char.lower() in name.lower())

    driver.find_element(By.XPATH, "//*[@id='right']/form/input").send_keys(random_char)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='right']/form/button").click()
    time.sleep(1)
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(2)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == count

def test_search_with_exactly_word(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)

    random_product = random.choice(product_names)
    driver.find_element(By.XPATH, "//*[@id='right']/form/input").send_keys(random_product)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='right']/form/button").click()
    time.sleep(1)
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(2)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == 1

def test_search_with_split_word(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)

    random_product = random.choice(product_names)
    trimmed_product = random_product[0:4] if len(random_product) > 4 else random_product
    print(f"Tên sản phẩm sau khi cắt: {trimmed_product}")

    driver.find_element(By.XPATH, "//*[@id='right']/form/input").send_keys(trimmed_product)
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='right']/form/button").click()
    time.sleep(3)
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(3)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) > 0

# Fail do khi tìm kiếm bằng khoảng trắng thì phải ra toàn bộ sản phẩm
def test_search_with_whitespace(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='right']/form/input").send_keys(" ")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='right']/form/button").click()
    time.sleep(1)

    all_products = []
    page = 1

    total_page = get_total_page()

    while True:
        temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
        driver.execute_script("arguments[0].scrollIntoView();", temp_element)
        time.sleep(2)

        list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
        for product in list_product:
            all_products.append(product.text)

        if page == total_page:
            break
        temp_element1 = driver.find_element(By.XPATH,
                                            "(//div[@class='col-md-6 col-lg-3 ftco-animate fadeInUp ftco-animated']//div[@class='product'])[1]")
        driver.execute_script("arguments[0].scrollIntoView();", temp_element1)
        time.sleep(2)
        temp_element2 = driver.find_element(By.XPATH,
                                            "(//div[@class='col-md-6 col-lg-3 ftco-animate fadeInUp ftco-animated']//div[@class='product'])[5]")
        driver.execute_script("arguments[0].scrollIntoView();", temp_element2)
        time.sleep(2)
        page += 1
        go_to_next_page(driver, page)

    assert len(all_products) == len(product_names)

def test_search_with_special_character(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)

    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
    length = 3
    random_string = ''.join(random.choice(special_characters) for _ in range(length))
    print(f"Chuỗi ký tự đặc biệt random: {random_string}")

    driver.find_element(By.XPATH, "//*[@id='right']/form/input").send_keys(random_string)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='right']/form/button").click()
    time.sleep(1)
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/section/div/div[3]/div[1]")
        assert False

    except NoSuchElementException:
        assert True

def test_search_with_uppercase_keyword(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    random_product = random.choice(product_names)
    uppercase_product = random_product.upper()
    driver.find_element(By.XPATH, "//*[@id='right']/form/input").send_keys(uppercase_product)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='right']/form/button").click()
    time.sleep(1)
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(2)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == 1

def test_search_with_lower_keyword(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    random_product = random.choice(product_names)

    # Chuyển thành chữ thường
    lowercase_product = random_product.lower()
    driver.find_element(By.XPATH, "//*[@id='right']/form/input").send_keys(lowercase_product)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='right']/form/button").click()
    time.sleep(1)
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(2)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == 1

def test_search_with_keyword_containing_whitespace(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    names_with_spaces = [name for name in product_names if " " in name]
    random_name = random.choice(names_with_spaces)

    driver.find_element(By.XPATH, "//*[@id='right']/form/input").send_keys(random_name)
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='right']/form/button").click()
    time.sleep(3)
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(3)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == 1