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
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/ul/li/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            # pick from soup
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/ul/li[6]/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/a[2]")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[3]")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            # pick from entree
            elem = driver.find_element_by_xpath("/html/body/div/div/div/p/a[1]")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/ul/li[5]/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/a[2]")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[3]")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)

            # edit card
            elem = driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr[1]/td[4]/a")
            elem.send_keys(Keys.RETURN)
            time.sleep(1)

            #try:
                #elem = driver.find_element_by_xpath("")
                #elem.send_keys(Keys.RETURN)
                #time.sleep(1)
                #assert True

            #except NoSuchElementException:
                #self.fail("remove not shown")
                #assert False
            #time.sleep(1)

            # if continue_test:
            #     try:
            #         elem = driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr[1]/td[3]/form/select")
            #         elem.send_keys(Keys.RETURN)
            #         elem.send_keys("2")
            #         time.sleep(1)
            #         elem.send_keys(Keys.RETURN)
            #         time.sleep(1)
            #         elem = driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr[1]/td[3]/form/input[2]")
            #         elem.send_keys(Keys.RETURN)
            #         assert True
            #
            #     except NoSuchElementException:
            #         self.fail("can not updated cart")
            #         assert False
            #     time.sleep(1)

            # if continue_test:
            #     # input payment information
            #     elem = driver.find_element_by_id("credit-card-number")
            #     elem.send_keys("4111111111111111")
            #     elem = driver.find_element_by_id("cvv")
            #     elem.send_keys("123")
            #     elem = driver.find_element_by_id("expiration")
            #     elem.send_keys("12/20")
            #
            #     time.sleep(1)
            #
            #     # click pay
            #     elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[3]")
            #     elem.send_keys(Keys.RETURN)
            #     time.sleep(10)
            # try:
            #     # find payment was successful
            #     elem = driver.find_element_by_xpath("/html/body/div/div/div/h2")
            #     assert True
            # except NoSuchElementException:
            #     self.fail("payment was NOT successful")
            #     assert False
            # time.sleep(3)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
