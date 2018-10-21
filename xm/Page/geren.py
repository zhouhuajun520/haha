from Base.base import Base
import Page


class  Geren(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    def wodeyouhuiq(self):
        return self.element(Page.person_coupons_id).text

    def click_shezhi(self):
        self.click_1(Page.setting_btn_id)