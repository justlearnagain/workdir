import sys
import time
from appium import webdriver
sys.path.append("../../")
from Pages.basePage import basePage
from mainPage import mainPage

class testMain(object):
    def __init__(self, login):
        self.login = login

    # 进入主页页面
    def enterMain(self):
        mainEmail = mainPage(self.login.driver)
        mainEmail.judgeMainPage()
        time.sleep(3)

    # 进入收件箱
    def enterReciveMail(self):
        reciveMail = mainPage(self.login.driver)
        reciveMail.enterReciveMail()
        time.sleep(3)

    # 进入星标邮件
    def enterStarMail(self):
        starMail = mainPage(self.login.driver)
        starMail.enterStarMail()
        time.sleep(3)

    # 进入附件管理
    def enterAttMail(self):
        attMail = mainPage(self.login.driver)
        attMail.enterAttMail()
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

    main = testMain(login)
    main.enterMain()
    main.enterReciveMail()
    main.enterStarMail()
    main.enterAttMail()