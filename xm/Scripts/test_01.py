import sys,os


sys.path.append(os.getcwd())

from time import sleep

from Base.get_data import Get_data
from Base.get_driver import get_d
from Page.page_tongyi import Tongyi
import pytest
from selenium.common.exceptions import TimeoutException

def get_login_data():
    # 结果列表
    login_list = []
    data = Get_data().get_yaml_data("aolai.yml")
    # return data
    for i in data.keys():
        login_list.append((i, data.get(i).get("phone"), data.get(i).get("passwd"),
                           data.get(i).get("tag"), data.get(i).get("tag_message"),
                           data.get(i).get("expect_result")))
    return login_list


class Test_1():
    def setup_class(self):
        self.driver = Tongyi(get_d("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))
    def teardown_class(self):
        self.driver.driver.quit()
    @pytest.mark.parametrize("test_num,phone,passwd,tag,tag_message,expect_result", get_login_data())
    def test_wo(self,test_num,phone,passwd,tag,tag_message,expect_result):
        self.driver.tong_shouye().click_wode()
        self.driver.tong_zc().click_denglu()
        self.driver.tong_denglu().shulu("18858967808", "123456")
        if tag:
            try:
                try:
                    sleep(1)
                    assert expect_result  in  self.driver.tong_geren().wodeyouhuiq()
                except  AssertionError as a:
                    print(a.__str__())
                self.driver.tong_geren().click_shezhi()
                sleep(2)
                self.driver.tong_shezhi().hua()
            except TimeoutException :
                self.driver.tong_shezhi().tuichu(1)
                assert False
        else:
            try:
                tangc = self.driver.tong_shezhi().get_toast(tag_message)
                dlu = self.driver.tong_denglu().if_login_btn_exits()
                assert  dlu and expect_result == tangc
            except  TimeoutException:
                assert False
            finally:
                self.driver.tong_denglu().close_login_page()

