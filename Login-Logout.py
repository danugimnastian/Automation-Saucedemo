import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Core.coreData import input
import coreLogin
import HtmlTestRunner
from selenium.webdriver.chrome.options import Options

Options = Options()

Options.add_experimental_option("excludeSwitches", ["enable-logging"])

class LoginLogout(unittest.TestCase):
    

    def testLoginSuccess(self):
        self.driver = webdriver.Chrome(options=Options)
        #Open Page
        self.driver.get(input.PageUrl)
        self.driver.maximize_window()
        #Login with Valid credentials
        coreLogin.test_login_success(self.driver)

    def testLockedoutUser(self):
        self.driver = webdriver.Chrome(options=Options)
        #Open Page
        self.driver.get(input.PageUrl)
        self.driver.maximize_window()
        #Login with Locked out User
        self.driver.find_element(By.ID,"user-name").send_keys(input.LokedUser)
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(input.Password)
        time.sleep(2)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        # Validate Login Failed
        results = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert("Epic") in results

    def testProblemUser(self):
        self.driver = webdriver.Chrome(options=Options)
        #Open Page
        self.driver.get(input.PageUrl)
        self.driver.maximize_window()
        #Login with Problem User 
        self.driver.find_element(By.ID,"user-name").send_keys(input.ProblemUser)
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(input.Password)
        time.sleep(2)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        # Validate Login 
        results = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").text
        assert("Add to cart") in results

    def testVisualUser(self):
        self.driver = webdriver.Chrome(options=Options)
        #Open Page
        self.driver.get(input.PageUrl)
        self.driver.maximize_window()
        #Login with Problem User 
        self.driver.find_element(By.ID,"user-name").send_keys(input.VisualUser)
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(input.Password)
        time.sleep(2)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        # Validate Login 
        results = self.driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Bike Light']").text
        assert("Bike") in results

    def testWrongPassword(self):
        self.driver = webdriver.Chrome(options=Options)
        #Open Page
        self.driver.get(input.PageUrl)
        self.driver.maximize_window()
        #Login with Wrong Password
        self.driver.find_element(By.ID,"user-name").send_keys(input.Username)
        time.sleep(2)
        self.driver.find_element(By.ID, "password").send_keys(input.WrongPassword)
        time.sleep(2)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        # Validate Login 
        results = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert("Epic sadface") in results

    def testEmpty(self):
        self.driver = webdriver.Chrome(options=Options)
        #Open Page
        self.driver.get(input.PageUrl)
        self.driver.maximize_window()
        #Login with Fields
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        #Validate Login Failed
        results = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert ("Epic sadface") in results

    def testLogout(self):
        self.driver = webdriver.Chrome(options=Options)
        #Open Page
        self.driver.get(input.PageUrl)
        self.driver.maximize_window()
        #Login with Valid credentials
        coreLogin.test_login_success(self.driver)
        #Logout
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        #Validate Logout Success
        results = self.driver.find_element(By.XPATH, "//div[@class='login_logo']").text
        assert("Swag Labs") in results

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportLoginLogout'))
