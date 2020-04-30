import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "testcase"
        pwd = "testcase123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        #
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
        # time.sleep(5)

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
        time.sleep(1)

        if continue_test:
            # check menu option
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[5]/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_name("name")
            elem.send_keys("Test Name")
            elem = driver.find_element_by_name("email")
            elem.send_keys("daweili@unomaha.edu")
            elem = driver.find_element_by_name("num")
            elem.send_keys("911")

            elem = driver.find_element_by_name("date")
            elem.send_keys("05/12/2020")
            elem = driver.find_element_by_name("time")

            elem.send_keys("12:10 10")
            elem = driver.find_element_by_name("guests")
            elem.send_keys("2")
            elem = driver.find_element_by_name("requests")
            elem.send_keys("I do not have any requests!!!")

            time.sleep(2)


            try:
                elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/form/button")
                elem.send_keys(Keys.RETURN)
                time.sleep(2)
                assert True


            except NoSuchElementException:
                self.fail("Reservation NOT successful")
                assert False
                time.sleep(1)


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
