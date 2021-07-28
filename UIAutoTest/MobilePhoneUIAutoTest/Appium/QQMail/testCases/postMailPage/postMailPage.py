import sys
import time
from selenium.webdriver.common.by import By
sys.path.append("../../")
from Pages.basePage import basePage
from config.data import loginData

class postMailPage(basePage):
    # 进入发邮件的按钮
    postMailBtn = "com.tencent.androidqqmail:id/af6"
    # 点击写邮件
    postMailTextView = "com.tencent.androidqqmail:id/a2l"
    # 取消按钮
    cancerBtn = "com.tencent.androidqqmail:id/af0"

    def __init__(self, driver):
        basePage.__init__(self, driver)

    # 进入发邮箱页面
    def enterPostMail(self):
        self.driver.implicitly_wait(10)
        self.click(By.ID, self.postMailBtn)
        # 通过id找到发邮件的按钮，是一个list，取到第一个值
        postMailBtn = self.get_elements(By.ID, self.postMailTextView)
        # postMailBtn[0].click() 这和下面的两种方式都可以
        self.tap(postMailBtn[0])

    # 发送邮箱
    def postMail(self):
        self.driver.implicitly_wait(10)
        # 以下语句只会返回['NATIVE_APP']，原因是app中webView未启动调试模式
        ele = self.driver.contexts
        print(ele)
        # 取消发送
        time.sleep(2)
        self.click(By.ID, self.cancerBtn)