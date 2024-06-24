import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Core.coreData import input
import coreLogin as coreLogin
import HtmlTestRunner
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_experimental_option("excludeSwitches", ["enable-logging"])


class PurchaseTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        # Open Page
        self.driver.get(input.PageUrl)
        self.driver.maximize_window()

    
    def testPurchase(self): #Sorting from Low Price to High
        #Login Page 
        coreLogin.test_login_success(self.driver)

        #Sorting
        self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//option[@value='lohi']").click()
        #Validate Sorting Price
        result = self.driver.find_element(By.XPATH, "//div[normalize-space()='Sauce Labs Onesie']").text
        assert("Sauce Labs Onesie") in result

        #Add to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        #Validate Add item to cart Success
        result = self.driver.find_element(By.ID, "remove-sauce-labs-onesie").text
        assert("Remove") in result   
    
        #Navigate to Check the Item
        self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()
        time.sleep(1)
        #Validate Item already added at Cart
        result = self.driver.find_element(By.XPATH, "//div[@class='cart_quantity_label']").text
        assert ("QTY") in result  

        #Checkout
        self.driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        #Fill the Data
        self.driver.find_element(By.ID, "first-name").send_keys(input.FirstName)
        time.sleep(1)
        self.driver.find_element(By.ID, "last-name").send_keys(input.LastName)
        time.sleep(1)
        self.driver.find_element(By.ID, "postal-code").send_keys(input.Zip)
        time.sleep(2)
        #Click Continue
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(2)
        #click Finish
        self.driver.find_element(By.ID, "finish").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "back-to-products").click()
        #Validate
        result = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        assert ("Products") in result                 

    def tearDown(self):
        # Close Webdriver Session
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportPurchasedItem'))