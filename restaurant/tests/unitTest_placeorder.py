import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "warda"
        pwd = "maverick1a"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)

        # driver.get("http://127.0.0.1:8000/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"

        # To check if user is logged in
        try:
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a")
            elem.send_keys(Keys.RETURN)
            continue_test = True
            time.sleep(1)


        except NoSuchElementException:
            self.fail("login status is not shown")
            assert False
            time.sleep(1)

        except:
            self.fail("Log in might not successful! ")
            assert False
            time.sleep(1)


        if continue_test:
            # check menu option
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/ul/li/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            # pick from menu
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/a[2]")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[3]")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)

            # checkout
            elem = driver.find_element_by_xpath("/html/body/div/div/div/p/a[2]")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)

            elem = driver.find_element_by_xpath("/html/body/div/div/div/form/p[1]/input")
            elem.send_keys("Test First Name")
            elem = driver.find_element_by_id("id_last_name")
            elem.send_keys("Test Last Name")
            elem = driver.find_element_by_id("id_email")
            elem.send_keys("daweili@unomaha.edu")
            elem = driver.find_element_by_id("id_address")
            elem.send_keys("123 Main st.")
            elem = driver.find_element_by_id("id_postal_code")
            elem.send_keys("911911")
            elem = driver.find_element_by_id("id_city")
            elem.send_keys("Omaha")
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/div/div/div/form/p[7]/input")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)

            # Payment page, fill put credit card information
            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-number']")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@class='number' and @id='credit-card-number']"))).send_keys("4111111111111111")
            time.sleep(1)
            driver.switch_to.default_content()
            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@name='braintree-hosted-field-cvv']")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@class='cvv' and @id='cvv']"))).send_keys("123")
            time.sleep(1)
            driver.switch_to.default_content()
            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@name='braintree-hosted-field-expirationDate']")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@class='expirationDate' and @id='expiration']"))).send_keys("12/20")
            time.sleep(1)
            driver.switch_to.default_content()
            elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[3]")
            elem.send_keys(Keys.RETURN)
            time.sleep(5)

            try:
                # attempt to find "Thankyou for placing your order with us!Please check your email for order confirmation!",
                # if found, order has been placed
                elem = driver.find_element_by_xpath("/html/body/div/div/div/h3")
                assert True
                time.sleep(1)


            except NoSuchElementException:
                self.fail("Order/Payment not successful")
                assert False
                time.sleep(1)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
