import sys
import time
from appium import webdriver
sys.path.append("../../")
from Pages.basePage import basePage
from postMailPage import postMailPage

class testPostMail(object):
    def __init__(self, login):
        self.login = login

    # 进入发件页面
    def enterPostMail(self):
        reciveMail = postMailPage(self.login.driver)
        reciveMail.enterPostMail()
        time.sleep(3)

    # 发送邮件
    def postMail(self):
        reciveMail = postMailPage(self.login.driver)
        reciveMail.postMail()
        time.sleep(3)

if __name__ == '__main__':
    caps = {}
    caps["platformName"] = "android"
    caps["deviceName"] = "testZSXQ"
    caps["automationName"] = "uiautomator2"
    caps["appPackage"] = "com.tencent.androidqqmail"
    caps["appActivity"] = "com.tencent.qqmail.launcher.desktop.LauncherActivity"
    caps["ensureWebviewsHavePages"] = True
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    login = basePage(driver)
    login.Login()

    post = testPostMail(login)
    post.enterPostMail()
    post.postMail()