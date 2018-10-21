from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    def element(self, aa, timeout=15, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*aa))

    def elements(self, aa, timeout=15, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*aa))
    # def f1(self, aa, timeout=15, poll_frequency=1):
    #     return WebDriverWait(self.driver,  timeout, poll_frequency).until(lambda x: x.find_element)
    def click_1(self, aa, timeout=15, poll_frequency=1):
        self.element(aa).click()

    def send_1(self, aa, text, timeout=15, poll_frequency=1):
        send_1 = self.element(aa)
        send_1.clear()
        send_1.send_keys(text)

    def huadong(self, tag):
        ha = self.driver.get_window_size()
        kuang = ha.get("width")
        gao = ha.get("height")
        #向上滑动
        if tag == "1":
            self.driver.swipe(kuang * 0.5, gao * 0.8, kuang * 0.5, gao * 0.3,1000)
        #向下
        if tag == "2":
            self.driver.swipe(kuang * 0.5, gao * 0.3, kuang * 0.5, gao * 0.8,1000)
        #向左
        if tag == "3":
            self.driver.swipe(kuang * 0.8, gao * 0.5, kuang * 0.3, gao * 0.5,1000)
        #向右
        if tag == "4":
            self.driver.swipe(kuang * 0.3, gao * 0.5, kuang * 0.8, gao * 0.5,1000)
    def get_toast(self, mess):

        toast_xpath = "//*[contains(@text,'{}')]".format(mess)
        toast_message = self.driver((By.XPATH, toast_xpath), timeout=5, poll_frequency=0.5).text
        return toast_message