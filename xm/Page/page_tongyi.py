from Page.denglu import Denglu
from Page.geren import Geren
from Page.shezhi import Shezhi
from Page.shouye import Shouye
from Page.zc import Zhuce


class Tongyi():
    def __init__(self, driver):
        self.driver = driver

    def  tong_denglu(self):
        return  Denglu(self.driver)
    def  tong_geren(self):
        return  Geren(self.driver)
    def tong_shezhi(self):
        return  Shezhi(self.driver)
    def tong_shouye(self):
        return  Shouye(self.driver)
    def tong_zc(self):
        return  Zhuce(self.driver)