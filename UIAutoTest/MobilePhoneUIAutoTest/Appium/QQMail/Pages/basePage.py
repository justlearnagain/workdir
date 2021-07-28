#from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

class basePage(object):
    trueUsername = "xxxxxx@163.com",
    truePassword = "xxxxxx",
    # 多个编辑窗口-关闭按钮
    closeBtn = "com.tencent.androidqqmail:id/bb5"
    # 同意邮箱协议
    hz = "com.tencent.androidqqmail:id/hz"
    # 同意按钮
    agreeBtn = "com.tencent.androidqqmail:id/aqa"
    # 163邮箱
    mailAccessibilityId = "163邮箱"
    mailXpath = "//android.widget.ImageView[@content-desc=\"163邮箱\"]"
    # 登录163邮箱文本
    mailText163 = "com.tencent.androidqqmail:id/az_"
    # 邮箱
    email = "com.tencent.androidqqmail:id/l"
    # 密码
    passWord = "com.tencent.androidqqmail:id/a1p"
    # 登录按钮
    enterBtn = "com.tencent.androidqqmail:id/az7"
    # 进入邮箱按钮
    enterMail = "com.tencent.androidqqmail:id/bd4"

    def __init__(self, driver):
        self.driver = driver

    def Login(self):
        self.driver.implicitly_wait(10)
        # 关闭多个编辑窗口
        self.driver.find_element(By.ID, self.closeBtn).click()
        # 同意用户协议
        self.driver.find_element(By.ID, self.hz).click()
        # 点击确定按钮
        self.driver.find_element(By.ID, self.agreeBtn).click()
        # 选择163邮箱
        self.driver.find_element(By.XPATH, self.mailXpath).click()

        # 输入账号密码登录
        self.driver.find_element(By.ID, self.email).click()
        self.driver.find_element(By.ID, self.email).send_keys(self.trueUsername)
        self.driver.find_element(By.ID, self.passWord).click()
        self.driver.find_element(By.ID, self.passWord).send_keys(self.truePassword)
        self.driver.find_element(By.ID, self.enterBtn).click()
        self.driver.find_element(By.ID, self.enterMail).click()

    def get_element(self, *loc):
        return self.driver.find_element(*loc)

    def get_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 通过find_element_by_accessibility_id找到元素
    def get_element_byAccId(self, AccID):
        return self.driver.find_element_by_accessibility_id(AccID)

    def click(self, *loc):
        self.driver.find_element(*loc).click()

    def send_keys(self, text, *loc):
        self.driver.find_element(*loc).send_keys(text)

    def clear(self, *loc):
        self.driver.find_element(*loc).clear()

    def get_text(self, *loc):
        return self.driver.find_element(*loc).text

    # 得到元素的属性值
    def get_att(self, att, *loc):
        return self.driver.find_element(*loc).get_attribute(att)

    # 按下按键
    def press(self, *loc):
        #self.driver.find_element(*loc).press()
        TouchAction(self.driver).press(*loc).release().perform()

    # 按下按键
    def tap(self, *loc):
        TouchAction(self.driver).tap(*loc).perform()