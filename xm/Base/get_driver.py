from appium import webdriver

def get_d(a , b):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['appPackage'] = a
    desired_caps['appActivity'] = b
    return webdriver.Remote('http://192.168.45.23:4723/wd/hub', desired_caps)