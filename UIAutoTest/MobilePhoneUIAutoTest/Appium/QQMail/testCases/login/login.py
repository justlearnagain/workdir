import time
from appium import webdriver
from loginPage import loginPage

class TestLogin(object):
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "testZSXQ"
        caps["automationName"] = "uiautomator2"
        caps["appPackage"] = "com.tencent.androidqqmail"
        caps["appActivity"] = "com.tencent.qqmail.launcher.desktop.LauncherActivity"
        caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def test_login(self):
        login = loginPage(self.driver)
        # 进入多个编辑窗口、用户协议窗口、选择163邮箱页面
        login.userNotice()
        # 判断是否进入登录页面
        login.judgeLoginPage()
        # 输入正确的账号密码登录
        login.successLogin()
        time.sleep(2)
        self.driver.quit()

    def test_errLogin(self):
        login = loginPage(self.driver)
        # 进入多个编辑窗口、用户协议窗口、选择163邮箱页面
        login.userNotice()
        # 判断是否进入登录页面
        login.judgeLoginPage()
        # 输入错误的账号密码登录
        login.errorLogin()
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    errLogin = TestLogin()
    errLogin.test_errLogin()

    successLogin = TestLogin()
    successLogin.test_login()