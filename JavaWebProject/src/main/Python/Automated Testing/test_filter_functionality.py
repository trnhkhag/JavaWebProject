import math
import random

import pytest
import time
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

total_products = 12
items_per_page = 8
total_products_men = 5
total_products_women = 4
total_products_couple = 1
total_products_unisex = 2
total_products_men_oris = 3
total_products_women_rado = 2
total_products_couple_rolex = 0
total_products_unisex_rado = 0
total_products_men_women = 9

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def scroll_product_page(driver):
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(1)
    temp_element1 = driver.find_element(By.XPATH,
                                        "(//div[@class='col-md-6 col-lg-3 ftco-animate fadeInUp ftco-animated']//div[@class='product'])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element1)
    time.sleep(1)

def go_to_next_page_all(driver, index):
    try:
        xpath = f"//a[@href='Shop?page={index}']"

        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)
    except Exception as e:
        print(f"Không tìm thấy trang: {e}")
def go_to_next_page(driver, index):
    try:
        xpath = f"//div[@class='block-27']/ul/li[{index}]"
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)
    except Exception as e:
        print(f"Không tìm thấy trang: {e}")

def get_total_page(total):
    return math.ceil(total / items_per_page)

def count_total_product(driver, total_page):
    all_products = []
    page = 1
    try:
        while True:
            scroll_product_page(driver)

            list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
            for product in list_product:
                all_products.append(product.text)

            if page == total_page:
                break

            time.sleep(2)
            temp_element2 = driver.find_element(By.XPATH,
                                                "(//div[@class='col-md-6 col-lg-3 ftco-animate fadeInUp ftco-animated']//div[@class='product'])[5]")
            driver.execute_script("arguments[0].scrollIntoView();", temp_element2)
            time.sleep(2)
            page += 1
            go_to_next_page(driver, page)
        return all_products
    except NoSuchElementException:
        return all_products

def test_filter_by_category_all(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)


    total_page = get_total_page(total_products)
    all_products = count_total_product(driver, total_page)

    assert len(all_products) == total_products

def test_filter_by_category_men(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']").click()
    time.sleep(1)

    total_page = get_total_page(total_products_men)
    all_products = count_total_product(driver, total_page)


    assert len(all_products) == total_products_men

def test_filter_by_category_women(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='Shop?cid=2&page=1' and @class='active']").click()
    time.sleep(1)

    total_page = get_total_page(total_products_women)

    all_products = count_total_product(driver, total_page)

    assert len(all_products) == total_products_women

def test_filter_by_category_couple(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='Shop?cid=3&page=1' and @class='active']").click()
    time.sleep(1)


    total_page = get_total_page(total_products_couple)

    all_products = count_total_product(driver, total_page)

    assert len(all_products) == total_products_couple

def test_filter_by_category_unisex(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='Shop?cid=4' and @class='active']").click()
    time.sleep(1)

    total_page = get_total_page(total_products_unisex)

    all_products = count_total_product(driver, total_page)

    assert len(all_products) == total_products_unisex

def test_filter_by_category_men_and_brand_oris(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    driver.find_element(By.ID, "category1").click()
    time.sleep(1)
    driver.find_element(By.ID, "Oris").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)

    total_page = get_total_page(total_products_men_oris)

    all_products = count_total_product(driver, total_page)

    assert len(all_products) == total_products_men_oris

def test_filter_by_category_women_and_brand_rado(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    driver.find_element(By.ID, "category2").click()
    time.sleep(1)
    driver.find_element(By.ID, "Rado").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)

    total_page = get_total_page(total_products_women_rado)

    all_products = count_total_product(driver, total_page)

    assert len(all_products) == total_products_women_rado

def test_filter_by_category_couple_and_brand_rolex(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    driver.find_element(By.ID, "category3").click()
    time.sleep(1)
    driver.find_element(By.ID, "Rolex").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)


    total_page = get_total_page(total_products_couple_rolex)

    all_products = count_total_product(driver, total_page)

    assert len(all_products) == total_products_couple_rolex

def test_filter_by_category_unisex_and_brand_rado(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    driver.find_element(By.ID, "category4").click()
    time.sleep(1)
    driver.find_element(By.ID, "Rado").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)


    total_page = get_total_page(total_products_unisex_rado)

    all_products = count_total_product(driver, total_page)

    assert len(all_products) == total_products_unisex_rado

def test_filter_by_min_price_less_than_0(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    min_price = driver.find_element(By.XPATH, "//input[@name='minPrice']")
    random_price = int(random.randint(-10000, -5000))
    driver.execute_script("arguments[0].value = arguments[1];", min_price, random_price)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)
    try:
        title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
        title_message_text = title_message.text
        time.sleep(1)
        message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
        message_text = message.text
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        assert title_message_text == 'Invalid Price' and message_text == 'Price values cannot be negative.'
    except:
        assert False

def test_filter_by_max_price_less_than_0(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    max_price = driver.find_element(By.XPATH, "//input[@name='maxPrice']")
    random_price = int(random.randint(-5000, -1000))
    driver.execute_script("arguments[0].value = arguments[1];", max_price, random_price)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)
    try:
        title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
        title_message_text = title_message.text
        time.sleep(1)
        message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
        message_text = message.text
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        assert title_message_text == 'Invalid Price' and message_text == 'Price values cannot be negative.'
    except:
        assert False

def test_filter_by_max_price_min_price(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    max_price = driver.find_element(By.XPATH, "//input[@name='maxPrice']")
    random_max_price = int(random.randint(1500, 7000))
    min_price = driver.find_element(By.XPATH, "//input[@name='minPrice']")
    random_min_price = int(random.randint(1000, 5000))
    driver.execute_script("arguments[0].value = arguments[1];", max_price, random_max_price)
    driver.execute_script("arguments[0].value = arguments[1];", min_price, random_min_price)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)
    try:
        title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
        title_message_text = title_message.text
        time.sleep(1)
        message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
        message_text = message.text
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        assert title_message_text == 'Invalid Price Range' and message_text == 'Min price cannot be greater than Max price.'
    except NoSuchElementException:
        scroll_product_page(driver)
        list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
        assert len(list_product) > 0

def test_filter_by_price_with_non_numeric_input(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    max_price = driver.find_element(By.XPATH, "//input[@name='maxPrice']")
    min_price = driver.find_element(By.XPATH, "//input[@name='minPrice']")
    random_char = random.choice(string.ascii_lowercase)
    driver.execute_script("arguments[0].value = arguments[1];", max_price, random_char)
    driver.execute_script("arguments[0].value = arguments[1];", min_price, random_char)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)
    try:
        title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
        title_message_text = title_message.text
        time.sleep(1)
        message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
        message_text = message.text
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        assert title_message_text == 'Missing Input' and message_text == 'Both Min Price and Max Price are required.'
    except NoSuchElementException:
        assert False

def test_filter_by_category_men_price(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    driver.find_element(By.ID, "category1").click()
    time.sleep(1)
    max_price = driver.find_element(By.XPATH, "//input[@name='maxPrice']")
    max_price_value = 1450
    min_price = driver.find_element(By.XPATH, "//input[@name='minPrice']")
    min_price_value = 1300
    driver.execute_script("arguments[0].value = arguments[1];", max_price, max_price_value)
    driver.execute_script("arguments[0].value = arguments[1];", min_price, min_price_value)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)
    scroll_product_page(driver)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == 2

def test_filter_by_category_unisex_price(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    driver.find_element(By.ID, "category4").click()
    time.sleep(1)
    max_price = driver.find_element(By.XPATH, "//input[@name='maxPrice']")
    random_max_price = 9500
    min_price = driver.find_element(By.XPATH, "//input[@name='minPrice']")
    random_min_price = 8000
    driver.execute_script("arguments[0].value = arguments[1];", max_price, random_max_price)
    driver.execute_script("arguments[0].value = arguments[1];", min_price, random_min_price)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)
    scroll_product_page(driver)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == 1

def test_filter_by_category_women_and_brand_rado_price(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    driver.find_element(By.ID, "category2").click()
    time.sleep(1)
    driver.find_element(By.ID, "Rado").click()
    time.sleep(1)
    max_price = driver.find_element(By.XPATH, "//input[@name='maxPrice']")
    max_price_value  = 2500
    min_price = driver.find_element(By.XPATH, "//input[@name='minPrice']")
    min_price_value  = 2000
    driver.execute_script("arguments[0].value = arguments[1];", max_price, max_price_value)
    driver.execute_script("arguments[0].value = arguments[1];", min_price, min_price_value)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)
    scroll_product_page(driver)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == 1

def test_filter_by_category_men_and_brand_oris_price(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    driver.find_element(By.ID, "category1").click()
    time.sleep(1)
    driver.find_element(By.ID, "Oris").click()
    time.sleep(1)
    max_price = driver.find_element(By.XPATH, "//input[@name='maxPrice']")
    random_max_price = 1450
    min_price = driver.find_element(By.XPATH, "//input[@name='minPrice']")
    random_min_price = 1350
    driver.execute_script("arguments[0].value = arguments[1];", max_price, random_max_price)
    driver.execute_script("arguments[0].value = arguments[1];", min_price, random_min_price)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)
    scroll_product_page(driver)
    list_product = driver.find_elements(By.CSS_SELECTOR, ".col-md-6.col-lg-3.ftco-animate.fadeInUp.ftco-animated")
    assert len(list_product) == 2

def test_filter_by_category_men_women(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(1)
    scroll_element = driver.find_element(By.XPATH, "//a[@href='Shop?cid=1&page=1' and @class='active']")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    time.sleep(1)
    driver.find_element(By.ID, "category1").click()
    time.sleep(1)
    driver.find_element(By.ID, "category2").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input").click()
    time.sleep(1)

    total_page = get_total_page(total_products_men_women)

    all_products = count_total_product(driver, total_page)
    print(total_page)
    assert len(all_products) == total_products_men_women