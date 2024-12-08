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
    
def add_to_cart_with_quantity(driver, product, quantity):
    actions = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    time.sleep(1)
    actions.move_to_element(product).perform()
    time.sleep(1)
    product.find_element(By.CLASS_NAME, "add-to-cart").click()
    time.sleep(1)
    increase_quantity_button = driver.find_element(By.CLASS_NAME, "quantity-right-plus")
    for _ in range(quantity - 1):
        increase_quantity_button.click()
    driver.find_element(By.CLASS_NAME, "buy-now").click()
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

def get_alert_title_and_message(driver):
    title = driver.find_element(By.ID, "swal2-title").text
    message = driver.find_element(By.ID, "swal2-html-container").text
    return title, message

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
    
def input_random_quantity_for_products(driver):
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
    
def get_checkout_summary(driver):
    subtotal = float(driver.find_element(By.ID, "subtotal").text.replace("$", ""))
    shipping = float(driver.find_element(By.ID, "shipping").text.replace("$", ""))
    discount = float(driver.find_element(By.ID, "discount").text.replace("$", ""))
    total = float(driver.find_element(By.ID, "total").text.replace("$", ""))
    return subtotal, shipping, discount, total
    
# TC1: Test checkout with empty Full Name
def test_checkout_empty_full_name(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    product = get_random_product(driver)
    add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[1]/div/input').clear()
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    error_title, error_message = get_alert_title_and_message(driver)
    time.sleep(5)
    assert "Validation Error" in error_title and "Full Name is required" in error_message
    
# TC2 Test checkout with empty Address
def test_checkout_empty_address(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    product = get_random_product(driver)
    add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    input_checkout_form(driver, "John Smith", "", "0159478236", "test123@gmail.com")
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    error_title, error_message = get_alert_title_and_message(driver)
    time.sleep(5)
    assert "Validation Error" in error_title and "Address is required" in error_message
    
# TC3: Test checkout with empty phone number
def test_checkout_empty_phone(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    product = get_random_product(driver)
    add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "", "test123@gmail.com")
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    error_title, error_message = get_alert_title_and_message(driver)
    time.sleep(5)
    assert "Validation Error" in error_title and "Phone number is required" in error_message
    
# TC4: Test checkout with empty email
def test_checkout_empty_email(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    product = get_random_product(driver)
    add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "")
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    title, message = get_alert_title_and_message(driver)
    time.sleep(5)
    assert "Checkout Successful" in title and "Your order has been successfully placed!" in message
    
# TC5: Test checkout with invalid phone number
def test_checkout_invalid_phone(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    product = get_random_product(driver)
    add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "abcdefgh", "test123@gmail.com")
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    title, message = get_alert_title_and_message(driver)
    time.sleep(5)
    assert "Invalid Phone Number" in title and "Please enter a valid 10-digit phone number" in message
    
# TC6: Test checkout with invalid email
def test_checkout_invalid_email(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    product = get_random_product(driver)
    add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "12345678")
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    title, message = get_alert_title_and_message(driver)
    time.sleep(5)
    assert "Invalid Email" in title and "Please enter a valid email address" in message
    
# TC7: Test checkout 1000 total no coupon
def test_checkout_1000_total_no_coupon(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[3]/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    time.sleep(5)
    price = float(product.find_element(By.CLASS_NAME, "price-sale").text.replace("$", ""))
    time.sleep(5)
    add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    actual_subtotal, shipping, actual_discount, actual_total = get_checkout_summary(driver)
    expected_total = price + shipping
    assert price == actual_subtotal and 0 == actual_discount and expected_total == actual_total
    
# TC8: Test checkout 900 total with free ship coupon
def test_checkout_900_total_freeship_coupon(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[4]/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    time.sleep(1)
    price = float(product.find_element(By.CLASS_NAME, "price-sale").text.replace("$", ""))
    time.sleep(5)
    add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    coupon_select = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[5]/div/select')
    select = Select(coupon_select)
    select.select_by_value("FREESHIP")
    time.sleep(5)
    title, message = get_alert_title_and_message(driver)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    actual_subtotal, actual_shipping, actual_discount, actual_total = get_checkout_summary(driver)
    expected_shipping = 0
    expected_total = price + expected_shipping
    actual_total = float(driver.find_element(By.ID, "total").text.replace("$", ""))
    assert "Success" in title and "Free shipping applied" in message
    assert price == actual_subtotal and expected_shipping == actual_shipping and 0 == actual_discount and expected_total == actual_total
    
# TC9: Test checkout 10000 total with discount 100$ coupon
def test_checkout_10000_total_discount100_coupon(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[3]/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    time.sleep(1)
    price = float(product.find_element(By.CLASS_NAME, "price-sale").text.replace("$", ""))
    add_to_cart_with_quantity(driver, product, 10)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    coupon_select = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[5]/div/select')
    select = Select(coupon_select)
    select.select_by_value("DISCOUNT100")
    time.sleep(5)
    title, message = get_alert_title_and_message(driver)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    actual_subtotal, actual_shipping, actual_discount, actual_total = get_checkout_summary(driver)
    expected_subtotal = price * 10
    expected_shipping = 2.0
    expected_discount = 100
    expected_total = expected_subtotal + expected_shipping - expected_discount
    actual_total = float(driver.find_element(By.ID, "total").text.replace("$", ""))
    assert "Success" in title and "Discount of $100 applied" in message
    assert expected_subtotal == actual_subtotal and expected_shipping == actual_shipping and expected_discount == actual_discount and expected_total == actual_total
    
# TC10: Test checkout 9000 total with discount 10% coupon
def test_checkout_9000_total_discount10p_coupon(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[3]/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    time.sleep(1)
    price = float(product.find_element(By.CLASS_NAME, "price-sale").text.replace("$", ""))
    add_to_cart_with_quantity(driver, product, 9)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    coupon_select = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[5]/div/select')
    select = Select(coupon_select)
    select.select_by_value("DISCOUNT10P")
    time.sleep(5)
    title, message = get_alert_title_and_message(driver)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    actual_subtotal, actual_shipping, actual_discount, actual_total = get_checkout_summary(driver)
    expected_subtotal = price * 9
    expected_shipping = 2.0
    expected_discount = 0
    expected_total = expected_subtotal + expected_shipping - expected_discount
    actual_total = float(driver.find_element(By.ID, "total").text.replace("$", ""))
    assert "Error" in title and "Order must be at least $10000 to apply this coupon" in message
    assert expected_subtotal == actual_subtotal and expected_shipping == actual_shipping and expected_discount == actual_discount and expected_total == actual_total
    
# TC11: Test checkout 900 total with discount 100$ coupon
def test_checkout_900_total_discount100_coupon(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[4]/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    time.sleep(1)
    price = float(product.find_element(By.CLASS_NAME, "price-sale").text.replace("$", ""))
    add_to_cart(driver, product)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    coupon_select = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[5]/div/select')
    select = Select(coupon_select)
    select.select_by_value("DISCOUNT100")
    time.sleep(5)
    title, message = get_alert_title_and_message(driver)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    actual_subtotal, actual_shipping, actual_discount, actual_total = get_checkout_summary(driver)
    expected_subtotal = price
    expected_shipping = 2.0
    expected_discount = 0
    expected_total = expected_subtotal + expected_shipping - expected_discount
    actual_total = float(driver.find_element(By.ID, "total").text.replace("$", ""))
    assert "Error" in title and "Order must be at least $1000 to apply this coupon" in message
    assert expected_subtotal == actual_subtotal and expected_shipping == actual_shipping and expected_discount == actual_discount and expected_total == actual_total
   
# TC12: Test checkout 12000 total with discount 10% coupon
def test_checkout_10000_total_discount10p_coupon(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[3]/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    time.sleep(1)
    price = float(product.find_element(By.CLASS_NAME, "price-sale").text.replace("$", ""))
    add_to_cart_with_quantity(driver, product, 12)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    coupon_select = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[5]/div/select')
    select = Select(coupon_select)
    select.select_by_value("DISCOUNT10P")
    time.sleep(5)
    title, message = get_alert_title_and_message(driver)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    actual_subtotal, actual_shipping, actual_discount, actual_total = get_checkout_summary(driver)
    expected_subtotal = price * 12
    expected_shipping = 2.0
    expected_discount = expected_subtotal * 0.1
    expected_total = expected_subtotal + expected_shipping - expected_discount
    actual_total = float(driver.find_element(By.ID, "total").text.replace("$", ""))
    assert "Success" in title and "10% discount applied" in message
    assert expected_subtotal == actual_subtotal and expected_shipping == actual_shipping and expected_discount == actual_discount and expected_total == actual_total
     
# TC13: Test checkout 13256 total with discount 10% coupon
def test_checkout_13256_total_discount10p_coupon(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a').click()
    product = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[5]/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", product)
    time.sleep(1)
    price = float(product.find_element(By.CLASS_NAME, "price-sale").text.replace("$", ""))
    add_to_cart_with_quantity(driver, product, 4)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    coupon_select = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/form/div/div[5]/div/select')
    select = Select(coupon_select)
    select.select_by_value("DISCOUNT10P")
    time.sleep(5)
    title, message = get_alert_title_and_message(driver)
    driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
    time.sleep(1)
    actual_subtotal, actual_shipping, actual_discount, actual_total = get_checkout_summary(driver)
    expected_subtotal = price * 4
    expected_shipping = 2.0
    expected_discount = round(expected_subtotal * 0.1, 1)
    expected_total = round(expected_subtotal + expected_shipping - expected_discount, 1)
    actual_total = float(driver.find_element(By.ID, "total").text.replace("$", ""))
    assert "Success" in title and "10% discount applied" in message
    assert expected_subtotal == actual_subtotal and expected_shipping == actual_shipping and expected_discount == actual_discount and expected_total == actual_total
    
# TC14: Test checkout successful with single product
def test_checkout_successful_single_product(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    product = get_random_product(driver)
    add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "test123@gmail.com")
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    title, message = get_alert_title_and_message(driver)
    time.sleep(5)
    assert "Checkout Successful" in title and "Your order has been successfully placed!" in message
    
# TC15: Test checkout successful with multiple product
def test_checkout_successful_multiple_product(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    products = get_random_products(driver)
    for product in products:
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)
        add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "test123@gmail.com")
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    title, message = get_alert_title_and_message(driver)
    time.sleep(5)
    assert "Checkout Successful" in title and "Your order has been successfully placed!" in message
    
# TC16: Test checkout successful with multiple product with quantity
def test_checkout_successful_multiple_product_with_quantity(driver):
    driver.get(web_url)
    login(driver, "tester", "123456")
    products = get_random_products(driver)
    for product in products:
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)
        add_to_cart(driver, product)
    driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/ul/li[1]/a').click()
    input_random_quantity_for_products(driver)
    checkout_button = driver.find_element(By.XPATH, '/html/body/section[2]/div/div[2]/p/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
    time.sleep(5)
    checkout_button.click()
    time.sleep(5)
    input_checkout_form(driver, "John Smith", "542 W, 15th Street", "0159478236", "test123@gmail.com")
    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/div[2]/div/p/button').click()
    title, message = get_alert_title_and_message(driver)
    time.sleep(5)
    assert "Checkout Successful" in title and "Your order has been successfully placed!" in message