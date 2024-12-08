import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

total_products = 12
items_per_page = 8

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
def login(driver):
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[1]/input").send_keys("khang")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[2]/input").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
def go_to_next_page(driver, index):
    try:
        xpath = f"//a[@href='Shop?page={index}']"
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)
    except Exception as e:
        print(f"Không tìm thấy trang: {e}")
def get_random_product(driver):
    xpath = f"//a[@href='Shop']"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(3)

    random_number = random.randint(1, total_products)
    page = get_page_from_index(random_number)
    scroll_product_page(driver)
    if (page == 1):
        xpath = f"(//div[@class='col-md-6 col-lg-3 ftco-animate fadeInUp ftco-animated']//div[@class='product'])[{random_number}]"
        product = driver.find_element(By.XPATH, xpath)
        return product
    else:
        temp_element2 = driver.find_element(By.XPATH,
                                            "(//div[@class='col-md-6 col-lg-3 ftco-animate fadeInUp ftco-animated']//div[@class='product'])[5]")
        driver.execute_script("arguments[0].scrollIntoView();", temp_element2)
        go_to_next_page(driver, page)
        scroll_product_page(driver)
        index_product = random_number % 8
        xpath = f"(//div[@class='col-md-6 col-lg-3 ftco-animate fadeInUp ftco-animated']//div[@class='product'])[{index_product}]"
        product = driver.find_element(By.XPATH, xpath)
        return product
def get_page_from_index(index):
    return (index // items_per_page) + 1
def scroll_product_page(driver):
    temp_element = driver.find_element(By.XPATH, "/html/body/section/div/div[2]/form/div[2]/input")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element)
    time.sleep(1)
    temp_element1 = driver.find_element(By.XPATH,
                                        "(//div[@class='col-md-6 col-lg-3 ftco-animate fadeInUp ftco-animated']//div[@class='product'])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", temp_element1)
    time.sleep(1)
def select_product(driver):
    products = get_random_product(driver)
    product_link = products.find_element(By.XPATH, ".//a[@href]")
    return product_link
def select_list_product(driver, random_product):
    i = 1
    dict_product_name_text = {}
    while i<=random_product:
        product_link = select_product(driver)
        product_link.click()
        time.sleep(1)
        product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
        driver.execute_script("arguments[0].scrollIntoView();", product)
        time.sleep(1)

        product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
        product_name_1_text = product_name.text
        if product_name_1_text in dict_product_name_text:
            dict_product_name_text[product_name_1_text] += 1
        else:
            dict_product_name_text[product_name_1_text] = 1
        driver.find_element(By.ID, "add_to_cart").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        i+=1
    return dict_product_name_text

def test_add_single_product(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)
    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
    product_name_text =  product_name.text
    driver.find_element(By.ID, "add_to_cart").click()
    time.sleep(1)
    try:
        title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
        title_message_text = title_message.text
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
        time.sleep(3)
        product_name_in_cart = driver.find_element(By.XPATH, "//td[@class='product-name']/h3")
        product_name_text_in_cart = product_name_in_cart.text
        assert product_name_text == product_name_text_in_cart and title_message_text == 'Success!'
    except NoSuchElementException:
        assert False
def test_add_multiple_products(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    random_product = random.randint(2, 4)
    dict_product_name_text = select_list_product(driver, random_product)

    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
    time.sleep(3)
    dict_product_name_in_cart = {}
    product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")
    length_dict = 1
    for element in product_name_elements:
        product_element = driver.find_element(By.XPATH, f"(//td[@class='product-name'])[{length_dict}]")
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", product_element)
        time.sleep(1)
        product_name = element.find_element(By.XPATH, ".//h3").text

        quantity = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input").get_attribute("value")
        length_dict += 1
        dict_product_name_in_cart[product_name] = int(quantity)
    print(dict_product_name_text, dict_product_name_in_cart)
    assert dict_product_name_text == dict_product_name_in_cart
def test_add_same_product_multiple_times(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
    product_name_text = product_name.text
    add_to_car_btn = driver.find_element(By.ID, "add_to_cart")
    add_to_car_btn.click()
    time.sleep(1)

    title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
    title_message_text = title_message.text
    time.sleep(1)
    confirm_action = driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled")
    confirm_action.click()
    time.sleep(1)
    add_to_car_btn.click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
    time.sleep(3)
    product_name_in_cart = driver.find_element(By.XPATH, "//td[@class='product-name']/h3")
    product_name_text_in_cart = product_name_in_cart.text
    quantity = driver.find_element(By.XPATH, "//td[@class='product-name']/div[@class='cart_quantity']/input").get_attribute("value")
    assert product_name_text == product_name_text_in_cart and title_message_text == 'Success!' and int(quantity) == 2
def test_add_product_by_btn(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)
    product = get_random_product(driver)
    if product:
        actions = ActionChains(driver)

        # Thực hiện hành động hover
        actions.move_to_element(product).perform()
        time.sleep(3)
        add_to_cart_btn = product.find_element(By.XPATH, "//a[@class='buy-now d-flex justify-content-center align-items-center mx-1']")
        add_to_cart_btn.click()
        product_name = product.find_element(By.XPATH, "//h3")
        product_name_text = product_name.text
        time.sleep(1)
        title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
        title_message_text = title_message.text
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
        time.sleep(3)

        product_name_in_cart = driver.find_element(By.XPATH, "//td[@class='product-name']/h3")
        product_name_text_in_cart = product_name_in_cart.text
        assert product_name_text.lower() == product_name_text_in_cart.lower() and title_message_text == 'Success!'
def test_add_product_positive_qty(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
    product_name_text = product_name.text
    random_quantity = random.randint(1, 51)
    plus_quantity_btn = driver.find_element(By.CSS_SELECTOR, ".quantity-right-plus.btn")
    i = 1
    while i<=random_quantity:
        plus_quantity_btn.click()
        i+=1
    random_quantity += 1
    time.sleep(3)
    driver.find_element(By.ID, "add_to_cart").click()
    time.sleep(1)

    title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
    title_message_text = title_message.text
    time.sleep(1)
    message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
    message_text = message.text
    driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
    time.sleep(3)
    try:
        product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")

        for element in product_name_elements:
            product_name = element.find_element(By.XPATH, ".//h3").text
            quantity = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input").get_attribute("value")
            # print(product_name_text, product_name, random_quantity, quantity)
            assert (product_name_text == product_name and random_quantity == int(quantity) and title_message_text == 'Success!')
    except NoSuchElementException:
        assert title_message.text == 'Error!' and message_text == "Requested quantity exceeds available stock."
def test_add_product_0_qty(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")

    minus_quantity_btn = driver.find_element(By.CSS_SELECTOR, ".quantity-left-minus.btn")
    minus_quantity_btn.click()
    time.sleep(1)
    driver.find_element(By.ID, "add_to_cart").click()
    time.sleep(1)

    title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
    title_message_text = title_message.text
    time.sleep(1)
    message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
    message_text = message.text
    driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, "//td[@class='product-name']/h3")
        assert False
    except:
        assert title_message_text == 'Error!' and message_text == 'Quantity must be greater than zero'
def test_update_positive_qty_in_cart_page(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
    product_name_text = product_name.text
    driver.find_element(By.ID, "add_to_cart").click()
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
        time.sleep(2)
        product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")

        for element in product_name_elements:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            product_name = element.find_element(By.XPATH, ".//h3").text
            quantity = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input")
            random_qty = int(random.randint(2, 51))
            driver.execute_script("arguments[0].value = arguments[1];", quantity, random_qty)

            # Kích hoạt sự kiện onchange (nếu trang web cần)
            driver.execute_script("""
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """, quantity)

            time.sleep(2)
            title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
            title_message_text = title_message.text
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
            time.sleep(2)
        product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")
        for element in product_name_elements:
            quantity_after = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input").get_attribute("value")
            if(title_message_text== 'Success!'):
                assert int(quantity_after) == random_qty
            else:
                assert int(quantity_after) == 1
    except NoSuchElementException:
        assert False
def test_update_negative_qty_in_cart_page(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
    product_name_text = product_name.text
    driver.find_element(By.ID, "add_to_cart").click()
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
        time.sleep(2)
        product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")

        for element in product_name_elements:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            product_name = element.find_element(By.XPATH, ".//h3").text
            quantity = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input")
            current_value = quantity.get_attribute("value")
            random_qty = int(random.randint(-5, 0))
            driver.execute_script("arguments[0].value = arguments[1];", quantity, random_qty)

            # Kích hoạt sự kiện onchange (nếu trang web cần)
            driver.execute_script("""
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """, quantity)

            time.sleep(2)
            title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
            title_message_text = title_message.text
            time.sleep(1)
            message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
            message_text = message.text
            driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
            time.sleep(2)
        product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")
        for element in product_name_elements:
            quantity_after = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input").get_attribute("value")
            assert (int(quantity_after) == int(current_value) and title_message_text == 'Error!'
                    and message_text == "Quantity must be a positive integer.")
    except NoSuchElementException:
        assert False
def test_update_qty_products_in_cart_page(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    random_product = random.randint(2, 3)
    dict_product_name_text = select_list_product(driver, random_product)
    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
    time.sleep(3)

    dict_new_quantity = {}
    length_dict = 1
    while length_dict<=len(dict_product_name_text):
        try:
            product_element = driver.find_element(By.XPATH, f"(//td[@class='product-name'])[{length_dict}]")
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", product_element)
            time.sleep(1)
            product_name = product_element.find_element(By.XPATH, ".//h3").text
            quantity = product_element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input")

            random_qty = int(random.randint(2, 5))
            driver.execute_script("arguments[0].value = arguments[1];", quantity, random_qty)

            # Kích hoạt sự kiện onchange (nếu trang web cần)
            driver.execute_script("""
                            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                        """, quantity)

            dict_new_quantity[product_name] = random_qty
            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
            time.sleep(2)
            length_dict += 1
        except:
            continue
    product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")

    for element in product_name_elements:
        quantity_after = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input").get_attribute("value")
        product_name = element.find_element(By.XPATH, ".//h3").text

        if product_name in dict_new_quantity:
            print(product_name, quantity_after)
            if dict_new_quantity[product_name] != int(quantity_after):
                assert False
                return
        else:
            print(f"{product_name} không có trong dict_new_quantity.")
    assert True
def test_add_product_without_login(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
    driver.find_element(By.ID, "add_to_cart").click()
    time.sleep(1)
    title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
    title_message_text = title_message.text
    time.sleep(1)
    message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
    message_text = message.text
    driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, "//td[@class='product-name']/h3")
        assert False
    except:
        assert title_message_text == 'Error!' and message_text=='Please log in to add products to your cart.'
def test_add_product_by_btn_without_login(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)

    product = get_random_product(driver)
    if product:
        actions = ActionChains(driver)

        # Thực hiện hành động hover
        actions.move_to_element(product).perform()
        time.sleep(3)
        add_to_cart_btn = product.find_element(By.XPATH,
                                               "//a[@class='buy-now d-flex justify-content-center align-items-center mx-1']")
        add_to_cart_btn.click()
        product_name = product.find_element(By.XPATH, "//h3")
        time.sleep(1)
        title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
        title_message_text = title_message.text
        time.sleep(1)
        message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
        message_text = message.text
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
        time.sleep(3)

        try:
            driver.find_element(By.XPATH, "//td[@class='product-name']/h3")
            assert False
        except:
            assert title_message_text == 'Error!' and message_text == 'Please log in to add products to your cart.'
def test_remove_product(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
    product_name_text = product_name.text
    driver.find_element(By.ID, "add_to_cart").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
    time.sleep(3)
    product_name_in_cart = driver.find_element(By.XPATH, "//td[@class='product-name']/h3")
    driver.execute_script("arguments[0].scrollIntoView();", product_name_in_cart)
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='cart_product_remove']//a").click()
    time.sleep(2)
    title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
    title_message_text = title_message.text
    message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
    message_text = message.text
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "//td[@class='product-name']/h3")
        assert False
    except:
        assert title_message_text == 'Success!' and message_text == 'Product removed successfully.'
def test_update_positive_qty_by_btn_in_cart_page(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
    product_name_text = product_name.text
    driver.find_element(By.ID, "add_to_cart").click()
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
        time.sleep(2)
        product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")

        for element in product_name_elements:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            product_name = element.find_element(By.XPATH, ".//h3").text
            quantity = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input")
            random_qty = int(random.randint(2, 51))
            index_random = 1
            while index_random<=random_qty:
                driver.execute_script("""
                    let input = arguments[0];
                    input.stepUp();  // Tăng 1 đơn vị
                    input.dispatchEvent(new Event('change'));  // Kích hoạt sự kiện onchange
                """, quantity)
                index_random+=1

            time.sleep(1)

            time.sleep(2)
            title_message = driver.find_element(By.CSS_SELECTOR, ".swal2-title")
            title_message_text = title_message.text
            message = driver.find_element(By.CSS_SELECTOR, ".swal2-html-container")
            message_text = message.text
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
            time.sleep(2)
        product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")
        for element in product_name_elements:
            quantity_after = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input").get_attribute("value")
            if(title_message_text== 'Success!'):
                assert int(quantity_after) == int(random_qty) + 1
            else:
                time.sleep(2)
                assert int(quantity_after) == 1 and message_text == "Quantity exceeds available stock."
    except NoSuchElementException:
        assert False
def test_update_negative_qty_by_btn_in_cart_page(driver):
    driver.get("http://localhost:8080/JavaWebProject/")
    time.sleep(3)
    login(driver)

    product_link = select_product(driver)
    product_link.click()
    time.sleep(1)
    product = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", product)
    time.sleep(1)
    product_name = driver.find_element(By.XPATH, "//h3[@class='RL']")
    product_name_text = product_name.text
    driver.find_element(By.ID, "add_to_cart").click()
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, ".swal2-confirm.swal2-styled").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
        time.sleep(2)
        product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")

        for element in product_name_elements:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            product_name = element.find_element(By.XPATH, ".//h3").text
            quantity = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input")
            driver.execute_script("""
                        let input = arguments[0];
                        input.stepDown();  // Tăng 1 đơn vị
                        input.dispatchEvent(new Event('change'));  // Kích hoạt sự kiện onchange
                    """, quantity)

            time.sleep(1)
        product_name_elements = driver.find_elements(By.XPATH, "//td[@class='product-name']")
        for element in product_name_elements:
            quantity_after = element.find_element(By.XPATH, ".//div[@class='cart_quantity']//input").get_attribute(
                "value")
        assert int(quantity_after) == 1
    except NoSuchElementException:
        assert False