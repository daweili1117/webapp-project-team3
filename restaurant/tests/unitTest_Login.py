
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class restaurant_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "testcase"
        pwd = "testcase123"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        #
        # driver.get("http://127.0.0.1:8000/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(3)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        # time.sleep(5)

        try:
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(2)


        except NoSuchElementException:
            self.fail("login status is not shown")
            assert False
            time.sleep(1)

        except:
            self.fail("Log in might not successful! ")
            assert False
            time.sleep(1)
        time.sleep(2)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
