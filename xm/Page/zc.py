from Base.base import Base
import Page


class Zhuce(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    def click_denglu(self):
        self.click_1(Page.exits_account_id)