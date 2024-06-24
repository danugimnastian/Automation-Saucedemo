import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Core.coreData import input



def test_login_success(driver):
    time.sleep(3)
    driver.find_element(By.ID, "user-name").send_keys(input.Username)
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys(input.Password)
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()