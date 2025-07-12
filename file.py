from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By


def setup_function(function):
    global driver

    options = Options()
    chrome_driver_location = Service("/var/lib/jenkins/chromedriver-linux64/chromedriver")

    options.binary_location = "/var/lib/jenkins/chrome-linux64/chrome"

    driver = webdriver.Chrome(service=chrome_driver_location, options=options)


def test_login():
    driver.get("https://school.gdquest.com/auth/login")

    driver.find_element(By.ID, "email-email").send_keys("kyoyagami666kof@gmai.com")
    driver.find_element(By.ID, "password-password").send_keys("kyoyagami666")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/form/button").click()


def teardown_function():
    print(driver.title)

    driver.quit()