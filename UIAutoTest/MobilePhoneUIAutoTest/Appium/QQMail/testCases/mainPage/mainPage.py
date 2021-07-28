import sys
from selenium.webdriver.common.by import By
sys.path.append("../../")
from Pages.basePage import basePage
from config.data import loginData

class mainPage(basePage):
    # 主页上的邮箱
    mainTitle = "com.tencent.androidqqmail:id/afc"
    # 主页上的返回按钮
    mainBackBtn = "com.tencent.androidqqmail:id/af1"
    # 收件箱
    reciveMail = "com.tencent.androidqqmail:id/sh"
    # 收件箱上的未收件数量
    reciveNum = "com.tencent.androidqqmail:id/si"
    # 从收件箱返回
    reciveRtn = "com.tencent.androidqqmail:id/af1"
    # 星标邮件
    starMail = "星标邮件"
    # 从星标邮件反馈
    starMailRtn = "com.tencent.androidqqmail:id/af1"
    # 附件管理
    attMail = "附件管理"
    # 从星标邮件反馈
    attMailRtn = "com.tencent.androidqqmail:id/af1"

    def __init__(self, driver):
        basePage.__init__(self, driver)

    # 判断是否主页页面
    def judgeMainPage(self):
        self.driver.implicitly_wait(10)
        assert self.get_text(By.ID, self.mainTitle) == "smallteaforever@163.com"
        assert self.get_att("content-desc", By.ID, self.mainBackBtn) == "返回"

    # 进入收件箱
    def enterReciveMail(self):
        self.driver.implicitly_wait(10)
        # 收件箱的数量大于等于0
        #assert int(self.get_text(By.ID, self.reciveNum)) >= 0
        #self.click(By.ID, self.reciveNum)
        self.click(By.ID, self.reciveMail)
        self.click(By.ID, self.reciveRtn)

    # 进入星标邮件
    def enterStarMail(self):
        self.driver.implicitly_wait(10)
        self.get_element_byAccId(self.starMail).click()
        self.click(By.ID, self.starMailRtn)

    # 进入附件管理
    def enterAttMail(self):
        self.driver.implicitly_wait(10)
        self.get_element_byAccId(self.attMail).click()
        self.click(By.ID, self.attMailRtn)

