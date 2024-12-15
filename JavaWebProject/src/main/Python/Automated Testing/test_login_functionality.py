import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import imaplib
import email
from email.header import decode_header
import random

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


url_home = "http://localhost:8188/JavaWebProject/Home"
url_login = "http://localhost:8188/JavaWebProject/Login"
msg_username = "Please enter your username."
msg_password = "Please enter your password."
msg_email = "Please enter a valid email address."
msg_invalid =  "Invalid username or password"
msg_password_short = "Password must be at least 6 characters long."
msg_forgot_password_email_not_exists = "Your email is not connected to any account."
msg_password_not_match = "Passwords do not match."
msg_fail_code = "Invalid code. Please try again."
msg_invalid_code = "Please enter a valid code."

def Login(driver, username, password):
    driver.get(url_home)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"username").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
    time.sleep(1)
    
def test_login_success(driver):
    status = 1
    Login(driver, "khang", "12345678")
    if url_home in get_current_url(driver):
        status = 2
    time.sleep(1)
    assert status == 2

def test_login_success_with_rememmberme(driver): 
    driver.get(url_home)
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
    if url_home in get_current_url(driver):
        status = 2
    time.sleep(1)
    assert status == 2

def test_login_without_username(driver):
    Login(driver, "", "12345678")
    assert msg_username in get_error_message(driver)

def test_login_without_password(driver):
    Login(driver, "khang", "")
    assert msg_password in get_error_message(driver)

def test_login_empty(driver):
    Login(driver, "", "")
    assert msg_username in get_error_message(driver)

def test_login_with_username_not_exist(driver):
    Login(driver, "asdf", "12345678")
    assert msg_invalid in get_error_invalid(driver)

def test_login_with_wrong_password(driver):
    Login(driver, "khang", "1234566666")
    assert msg_invalid in get_error_invalid(driver)

def test_login_with_short_password(driver):
    Login(driver, "khang", "1")
    assert msg_password_short in get_error_message(driver)

def test_login_sql_injection_based_on_1_equal_1_isAlwaysTrue(driver):
    Login(driver, "105 OR 1=1", "105 OR 1=1")
    assert msg_invalid in get_error_invalid(driver)

def test_login_sql_injection_based_on_equal_isAlwaysTrue(driver):
    Login(driver, '" or ""="','" or ""="')
    assert msg_invalid in get_error_invalid(driver)

def test_login_sql_injection_based_onBatchedSQLStatements(driver):
    Login(driver, "105; DROP TABLE donhang", "105; DROP TABLE donhang")
    assert msg_invalid in get_error_invalid(driver)

def test_logout(driver):
    Login(driver, "khang", "12345678")
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    assert url_login in get_current_url(driver)

def test_forgot_password_with_email_not_exists(driver):
    driver.get(url_home)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[2]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"email").send_keys("asdasdasdasdasd@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    assert msg_forgot_password_email_not_exists in get_error_invalid(driver)

def test_forgot_password_with_invalid_email(driver):
    driver.get(url_home)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[2]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"email").send_keys("haaaa.com")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    assert msg_email in get_error_message(driver)

def get_verification_code(email_user, email_pass):
    # Kết nối tới server Gmail IMAP
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_user, email_pass)

    # Chọn mailbox (thường là "INBOX")
    mail.select("Inbox")

    # Tìm email với subject chứa `subject_keyword`
    status, messages = mail.search(None, '(SUBJECT "Your verification code")')

    if status != "OK" or not messages[0]:
        raise Exception("Không tìm thấy email phù hợp.")

    # Lấy email mới nhất
    latest_email_id = messages[0].split()[-1]
    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

    if status != "OK":
        raise Exception("Không thể lấy email.")

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            # Decode email
            msg = email.message_from_bytes(response_part[1])
            # Nếu email có nhiều phần, chỉ lấy text
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = msg.get_payload(decode=True).decode()

            # Tìm mã xác nhận trong nội dung email
            import re
            match = re.search(r"\b\d{6}\b", body)  # Giả sử mã xác nhận là 6 chữ số
            if match:
                return match.group(0)

    return None

email_user = "duong0023@gmail.com"
email_pass = "ibammoxasknmyttc"

def test_forgot_password_success(driver):
    driver.get(url_home)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[2]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"email").send_keys("duong0023@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    time.sleep(10)
    verification_code = get_verification_code(email_user, email_pass)
    time.sleep(10)
    driver.find_element(By.ID,"code").send_keys(verification_code)
    time.sleep(3)
    driver.find_element(By.ID,"submit").click()
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID,"cpass").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    time.sleep(1)
    assert url_login in get_current_url(driver)

def test_forgot_password_with_wrong_code(driver):
    driver.get(url_home)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[2]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"email").send_keys("duong0023@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    time.sleep(3)
    verification_code = random.randint(100000, 999999)
    driver.find_element(By.ID,"code").send_keys(verification_code)
    time.sleep(3)
    driver.find_element(By.ID,"submit").click()
    time.sleep(1)
    assert msg_fail_code in get_error_invalid(driver)

def test_forgot_password_with_invalid_code(driver):
    driver.get(url_home)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[2]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"email").send_keys("duong0023@@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    time.sleep(3)
    driver.find_element(By.ID,"code").send_keys("abc123")
    time.sleep(3)
    driver.find_element(By.ID,"submit").click()
    time.sleep(1)
    
    assert msg_invalid_code in get_error_message(driver)

def test_forgot_password_with_pass_not_match(driver):
    driver.get(url_home)
    driver.find_element(By.XPATH, "/html/body/nav/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/div[2]/a").click()
    time.sleep(1)
    driver.find_element(By.ID,"email").send_keys("duong0023@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    time.sleep(10)
    verification_code = get_verification_code(email_user, email_pass)
    time.sleep(10)
    driver.find_element(By.ID,"code").send_keys(verification_code)
    time.sleep(3)
    driver.find_element(By.ID,"submit").click()
    time.sleep(1)
    driver.find_element(By.ID,"pass").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID,"cpass").send_keys("1111111")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    time.sleep(1)
    assert msg_password_not_match in get_error_message(driver)

def get_current_url(driver):
    return driver.current_url

def get_error_message(driver):
    return driver.find_element(By.ID, "swal2-html-container").text

def get_error_invalid(driver):
    return driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/p").text