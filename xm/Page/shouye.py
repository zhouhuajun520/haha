from Base.base import Base
import Page


class Shouye(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    def click_wode(self):
        self.click_1(Page.my_btn_id)