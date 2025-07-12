from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest, time
from selenium.webdriver.common.by import By


def setup_function(function):
    global driver

    options = Options()
    chrome_driver_location = Service("/var/lib/jenkins/chromedriver-linux64/chromedriver")

    options.binary_location = "/var/lib/jenkins/chrome-linux64/chrome"

    driver = webdriver.Chrome(service=chrome_driver_location, options=options)

    driver.implicitly_wait(20)


def test_login():
    driver.get("https://school.gdquest.com/auth/login")

    driver.find_element(By.ID, "email-email").send_keys("kyoyagami666kof@gmail.com")
    driver.find_element(By.ID, "password-password").send_keys("kyoyagami666")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/form/button").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/header/div/nav/div[1]/div/form/button").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/header/div/nav/div[1]/a/span[1]/span[1]").click()


def teardown_function():
    print(driver.title)

    time.sleep(5)

    driver.quit()