import sys
import time
from selenium.webdriver.common.by import By
sys.path.append("../../")
from Pages.basePage import basePage
from config.data import loginData

class reciveMailPage(basePage):
    # 收件箱
    reciveMail = "com.tencent.androidqqmail:id/sh"
    # 收件箱上的未收件数量
    reciveNum = "com.tencent.androidqqmail:id/si"
    # 从收件箱返回
    reciveRtn = "com.tencent.androidqqmail:id/af1"
    # 所有的邮件
    allReciveMails = "com.tencent.androidqqmail:id/a3c"
    # 返回按钮
    returnBtn = "com.tencent.androidqqmail:id/af1"

    def __init__(self, driver):
        basePage.__init__(self, driver)

    # 进入收件箱页面
    def enterReciveMail(self):
        self.driver.implicitly_wait(10)
        # 收件箱的数量大于等于0
        #assert int(self.get_text(By.ID, self.reciveNum)) >= 0
        #self.click(By.ID, self.reciveNum)
        self.click(By.ID, self.reciveMail)

    # 打开所有邮箱
    def openAllMails(self):
        self.driver.implicitly_wait(10)
        # 先找到父元素，然后通过父元素找到子元素
        allMail = self.get_element(By.ID, self.allReciveMails).find_elements_by_class_name('android.widget.RelativeLayout')
        mailCount = len(allMail)
        print(mailCount)
        for i in range(0, mailCount-1):
            self.get_element(By.ID, self.allReciveMails).find_elements_by_class_name('android.widget.RelativeLayout')[i].click()
            self.click(By.ID, self.returnBtn)
            time.sleep(2)