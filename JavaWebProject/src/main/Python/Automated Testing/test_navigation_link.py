import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
    
web_url = "http://localhost:8080/JavaWebProject/Home"

def test_navigation(driver):
    driver.get(web_url)
    xpaths = [
    "/html/body/nav/div/div[1]/ul/li[1]/a",
    "/html/body/nav/div/div[1]/ul/li[2]/a",
    "/html/body/nav/div/div[1]/ul/li[3]/a",
    "/html/body/nav/div/div[1]/ul/li[4]/a",
    "/html/body/nav/div/div[3]/ul/li[1]/a/i",
    "/html/body/nav/div/div[3]/ul/li[2]/a/i"
]
    for start_xpath in xpaths:
        driver.find_element(By.XPATH, start_xpath).click()
        time.sleep(1)
        for target_xpath in xpaths:
            temp = driver.find_element(By.XPATH, target_xpath)
            text_title_case = temp.text.title()  
            # print("Checking navigation for: ", temp2.text)
            if start_xpath != target_xpath: 
                driver.find_element(By.XPATH, target_xpath).click()
                # print("Url: ", driver.current_url)
                time.sleep(2)
                assert text_title_case in driver.current_url , f"Navigation failed for {target_xpath}"

def test_link(driver):
    home_page = web_url
    driver.get(home_page)
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        url = link.get_attribute("href")
        print(f"Checking: {url}")

        if url is None or url == "":
            print("URL is either not configured for anchor tag or it is empty")
            continue

        if not url.startswith(home_page):
            print(f"URL belongs to another domain, skipping it: {url}")
            continue

        try:
            response = requests.head(url, allow_redirects=True)

            if response.status_code >= 400:
                print(f"{url} is a broken link")
            else:
                print(f"{url} is a valid link")

        except requests.exceptions.RequestException as e:
            print(f"Error checking {url}: {e}")