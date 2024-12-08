import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import random
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
    
def get_random_product(driver):
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    products = driver.find_elements(By.CLASS_NAME, "product")
    product_list = []
    for p in products:
        product_list.append(p)
    product = random.choice(product_list)
    return product

def get_random_products(driver):
    num_product = random.randint(2, 6)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    products = driver.find_elements(By.CLASS_NAME, "product")
    product_list = []
    for p in products:
        product_list.append(p)
    product = random.sample(product_list, num_product)
    return product

def input_random_quantity_for_products(driver):
    quantity_list = []
    quantity_fields = driver.find_elements(By.CLASS_NAME, "cart_quantity_input")
    for i in range(len(quantity_fields)):
        quantity_field = driver.find_elements(By.CLASS_NAME, "cart_quantity_input")[i]
        time.sleep(1)
        quantity = random.randint(1, 10)
        driver.execute_script("arguments[0].value = arguments[1];", quantity_field, quantity)
        driver.execute_script("""
                            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                        """, quantity_field)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
        quantity_list.append(quantity)
    return list(map(str, quantity_list)).sort()
        
def get_product_name_and_price_list_in_cart(driver):
    product_infos = driver.find_elements(By.CLASS_NAME, "product-name")
    product_name_list = []
    product_price_list = []
    for product_info in product_infos:
        product_name = product_info.find_element(By.TAG_NAME, "h3").text
        product_name_list.append(product_name)
        product_price = product_info.find_element(By.CLASS_NAME, "price").text
        product_price_list.append(product_price)
    return product_name_list.sort(), product_price_list.sort()

def get_product_name_price_quantity_list_in_order_history(driver, order):
    order_items = order.find_elements(By.CLASS_NAME, "order-item")
    product_name_list = []
    product_price_list = []
    product_quantity_list = []
    for order_item in order_items:
        product_name = order_item.find_element(By.CLASS_NAME, "headtexthis").text[14:]
        product_name_list.append(product_name)
        product_quantity = order_item.find_element(By.CLASS_NAME, "numproduct").text[10:]
        product_quantity_list.append(product_quantity)
        product_price = order_item.find_element(By.CLASS_NAME, "item-price").text
        product_price_list.append(product_price)
    return product_name_list.sort(), product_price_list.sort(), product_quantity_list.sort()

def input_checkout_form(driver, fullname, address, phone, email):
    full_name_field = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[1]/div/input')
    address_field = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[2]/div/input')
    phone_field = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[3]/div/input')
    email_field = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[4]/div/input')
    full_name_field.clear()
    full_name_field.send_keys(fullname)
    address_field.clear()
    address_field.send_keys(address)
    phone_field.clear()
    phone_field.send_keys(phone)
    email_field.clear()
    email_field.send_keys(email)
    
def get_checkout_summary(driver):
    subtotal = float(driver.find_element(By.ID, "subtotal").text.replace("$", ""))
    shipping = float(driver.find_element(By.ID, "shipping").text.replace("$", ""))
    discount = float(driver.find_element(By.ID, "discount").text.replace("$", ""))
    total = float(driver.find_element(By.ID, "total").text.replace("$", ""))
    return subtotal, shipping, discount, total

# TC1: Test view single order history no coupon
def test_view_single_order_history_no_coupon(driver):
    driver.get(web_url)
    login(driver, "khang123", "12345678")
    products = get_random_products(driver)
    for product in products:
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)
        add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    cart_product_quantity_list = input_random_quantity_for_products(driver)
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(1)
    cart_product_name_list, cart_product_price_list = get_product_name_and_price_list_in_cart(driver)
    checkout_button.click()
    time.sleep(1)
    checkout_total = driver.find_element(By.ID, "total").text
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "test123@gmail.com")
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/p/a[1]').click()
    time.sleep(1)
    order = driver.find_elements(By.CLASS_NAME, "order-list")[0]
    oh_product_name_list, oh_product_price_list, oh_product_quantity_list = get_product_name_price_quantity_list_in_order_history(driver, order)
    order_total = order.find_element(By.CLASS_NAME, "mnhis").text
    assert checkout_total == order_total and cart_product_name_list == oh_product_name_list and cart_product_price_list == oh_product_price_list and cart_product_quantity_list == oh_product_quantity_list
    
# TC2: Test view single order history with free ship coupon
def test_view_order_single_order_history_with_freeship_coupon(driver):
    driver.get(web_url)
    login(driver, "khang123", "12345678")
    products = get_random_products(driver)
    for product in products:
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)
        add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    cart_product_quantity_list = input_random_quantity_for_products(driver)
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(1)
    cart_product_name_list, cart_product_price_list = get_product_name_and_price_list_in_cart(driver)
    checkout_button.click()
    time.sleep(1)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "test123@gmail.com")
    coupon_select = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[5]/div/select')
    select = Select(coupon_select)
    select.select_by_value("FREESHIP")
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    checkout_total = driver.find_element(By.ID, "total").text
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/p/a[1]').click()
    time.sleep(1)
    order = driver.find_elements(By.CLASS_NAME, "order-list")[0]
    oh_product_name_list, oh_product_price_list, oh_product_quantity_list = get_product_name_price_quantity_list_in_order_history(driver, order)
    order_total = order.find_element(By.CLASS_NAME, "mnhis").text
    assert checkout_total == order_total and cart_product_name_list == oh_product_name_list and cart_product_price_list == oh_product_price_list and cart_product_quantity_list == oh_product_quantity_list
    
# TC3: Test view single order history with discount 100 coupon
def test_view_order_single_order_history_with_discount100_coupon(driver):
    driver.get(web_url)
    login(driver, "khang123", "12345678")
    products = get_random_products(driver)
    for product in products:
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)
        add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    cart_product_quantity_list = input_random_quantity_for_products(driver)
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(1)
    cart_product_name_list, cart_product_price_list = get_product_name_and_price_list_in_cart(driver)
    checkout_button.click()
    time.sleep(1)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "test123@gmail.com")
    coupon_select = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[5]/div/select')
    select = Select(coupon_select)
    select.select_by_value("DISCOUNT100")
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    checkout_total = driver.find_element(By.ID, "total").text
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/p/a[1]').click()
    time.sleep(1)
    order = driver.find_elements(By.CLASS_NAME, "order-list")[0]
    oh_product_name_list, oh_product_price_list, oh_product_quantity_list = get_product_name_price_quantity_list_in_order_history(driver, order)
    order_total = order.find_element(By.CLASS_NAME, "mnhis").text
    assert checkout_total == order_total and cart_product_name_list == oh_product_name_list and cart_product_price_list == oh_product_price_list and cart_product_quantity_list == oh_product_quantity_list
    
# TC4: Test view single order history with discount 10% coupon
def test_view_order_single_order_history_with_discount10p_coupon(driver):
    driver.get(web_url)
    login(driver, "khang123", "12345678")
    products = get_random_products(driver)
    for product in products:
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)
        add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    cart_product_quantity_list = input_random_quantity_for_products(driver)
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(1)
    cart_product_name_list, cart_product_price_list = get_product_name_and_price_list_in_cart(driver)
    checkout_button.click()
    time.sleep(1)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "test123@gmail.com")
    coupon_select = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[5]/div/select')
    select = Select(coupon_select)
    select.select_by_value("DISCOUNT10P")
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    checkout_total = driver.find_element(By.ID, "total").text
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/p/a[1]').click()
    time.sleep(1)
    order = driver.find_elements(By.CLASS_NAME, "order-list")[0]
    oh_product_name_list, oh_product_price_list, oh_product_quantity_list = get_product_name_price_quantity_list_in_order_history(driver, order)
    order_total = order.find_element(By.CLASS_NAME, "mnhis").text
    assert checkout_total == order_total and cart_product_name_list == oh_product_name_list and cart_product_price_list == oh_product_price_list and cart_product_quantity_list == oh_product_quantity_list
    
# TC5: Test view multiple order history
def test_view_multiple_order_history(driver):
    driver.get(web_url)
    checkout_total_list = []
    login(driver, "khang123", "12345678")
    for _ in range(2):
        products = get_random_products(driver)
        for product in products:
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView(true);", product)
            time.sleep(1)
            add_to_cart(driver, product)
        driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
        cart_product_quantity_list = input_random_quantity_for_products(driver)
        checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
        driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
        time.sleep(1)
        cart_product_name_list, cart_product_price_list = get_product_name_and_price_list_in_cart(driver)
        checkout_button.click()
        time.sleep(1)
        checkout_total = driver.find_element(By.ID, "total").text
        checkout_total_list.append(checkout_total)
        input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "test123@gmail.com")
        driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
        time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/p/a[1]').click()
    time.sleep(1)
    checkout_total_list.reverse()
    for i in range(2):
        order = driver.find_elements(By.CLASS_NAME, "order-list")[i]
        oh_product_name_list, oh_product_price_list, oh_product_quantity_list = get_product_name_price_quantity_list_in_order_history(driver, order)
        order_total = order.find_element(By.CLASS_NAME, "mnhis").text
        assert checkout_total_list[i] == order_total and cart_product_name_list == oh_product_name_list and cart_product_price_list == oh_product_price_list and cart_product_quantity_list == oh_product_quantity_list