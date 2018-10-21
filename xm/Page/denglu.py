from Base.base import Base
import Page



class Denglu(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def shulu(self, name, passwd):
        self.send_1(Page.login_account_id, name)
        self.send_1(Page.login_passwd_id, passwd)
        self.click_1(Page.login_btn_id)
    def if_login_btn_exits(self):
        # 判断登录按钮是否存在 存在返回True 不存在返回False
        try:
            self.element(Page.login_btn_id)
            return True
        except Exception as e:
            return False
    def close_login_page(self):
        # 关闭登录页
        self.click_1(Page.login_close_btn_id)
