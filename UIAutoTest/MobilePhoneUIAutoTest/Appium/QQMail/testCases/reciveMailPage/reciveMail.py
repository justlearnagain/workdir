import sys
import time
from appium import webdriver
sys.path.append("../../")
from Pages.basePage import basePage
from reciveMailPage import reciveMailPage

class testReciveMail(object):
    def __init__(self, login):
        self.login = login

    # 进入收件箱
    def enterReciveMail(self):
        reciveMail = reciveMailPage(self.login.driver)
        reciveMail.enterReciveMail()

    # 打开所以邮箱
    def openAllMails(self):
        reciveMail = reciveMailPage(self.login.driver)
        reciveMail.openAllMails()

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

    recive = testReciveMail(login)
    recive.enterReciveMail()
    recive.openAllMails()