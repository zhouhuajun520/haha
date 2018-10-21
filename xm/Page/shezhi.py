from Base.base import Base
import Page


class  Shezhi(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    def  hua(self):
        self.huadong(1)

    def tuichu(self, tag=1):
        self.click_1(Page.logout_btn_id)
        #确定退出
        if  tag == "1":
            self.click_1(Page.logout_acc_btn_id)
        #取消退出
        else:
            self.click_1(Page.log_out_miss_btn_id)